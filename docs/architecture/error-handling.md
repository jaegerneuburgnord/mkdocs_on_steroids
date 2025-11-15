# Error Handling

Error handling strategies and patterns used throughout the library.

## Overview

This document describes the error handling philosophy and mechanisms in the library.

## Error Handling Architecture

```mermaid
graph TB
    A[Operation] --> B{Success?}

    B -->|Yes| C[Return Result<T>]
    B -->|No| D[Error Occurred]

    D --> E{Error Type}

    E -->|Recoverable| F[Return Err<E>]
    E -->|Fatal| G[Terminate/Panic]

    F --> H[Caller Handles]
    H --> I{Can Recover?}

    I -->|Yes| J[Retry/Fallback]
    I -->|No| K[Propagate Up]

    J --> A
    K --> L[Higher Level Handler]

    style C fill:#c8e6c9
    style F fill:#fff9c4
    style G fill:#ffccbc
```

## Error Categories

```mermaid
mindmap
  root((Error Types))
    System Errors
      File Not Found
      Permission Denied
      Out of Memory
    Logic Errors
      Invalid Input
      Precondition Failed
      Assertion Failed
    Runtime Errors
      Network Timeout
      Parse Error
      Resource Exhausted
    User Errors
      Invalid Config
      Bad Request
      Auth Failed
```

## Error Handling Strategy

### Result Type Pattern

```mermaid
classDiagram
    class Result~T,E~ {
        -variant: Ok(T) | Err(E)
        +is_ok() bool
        +is_err() bool
        +value() T
        +error() E
        +map(f: T->U) Result~U,E~
        +and_then(f: T->Result~U,E~)
        +map_err(f: E->F) Result~T,F~
    }

    class Ok~T~ {
        +value: T
    }

    class Err~E~ {
        +error: E
    }

    Result <|-- Ok
    Result <|-- Err
```

### Error Propagation Flow

```mermaid
sequenceDiagram
    participant L1 as Low Level
    participant L2 as Mid Level
    participant L3 as High Level
    participant U as User

    U->>L3: Request Operation
    L3->>L2: Call Function

    alt Operation Succeeds
        L2->>L1: Process
        L1-->>L2: Ok(result)
        L2-->>L3: Ok(result)
        L3-->>U: Success
    else Operation Fails
        L2->>L1: Process
        L1-->>L2: Err(low_error)
        Note over L2: Transform Error
        L2-->>L3: Err(mid_error)
        Note over L3: Handle or Propagate
        L3-->>U: Error Response
    end
```

## Exception Types Hierarchy

```mermaid
graph TD
    A[Exception] --> B[RuntimeError]
    A --> C[LogicError]
    A --> D[SystemError]

    B --> B1[NullPointerError]
    B --> B2[OutOfBoundsError]
    B --> B3[TimeoutError]

    C --> C1[InvalidArgument]
    C --> C2[PreconditionFailed]
    C --> C3[AssertionFailed]

    D --> D1[FileSystemError]
    D --> D2[NetworkError]
    D --> D3[MemoryError]

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#ffccbc
    style D fill:#ffe0b2
```

## Error Context Chain

```mermaid
graph LR
    A[Original Error] --> B[Add Context 1]
    B --> C[Add Context 2]
    C --> D[Add Context 3]
    D --> E[Final Error]

    B -.->|"File: foo.cpp:42"| B
    C -.->|"Function: parse_config"| C
    D -.->|"Action: Loading settings"| D

    style A fill:#ffccbc
    style E fill:#e1f5ff
```

## Error Recovery Strategies

```mermaid
stateDiagram-v2
    [*] --> Attempt

    Attempt --> Success: Operation OK
    Attempt --> Error: Operation Failed

    Success --> [*]

    Error --> Retry: Transient Error
    Error --> Fallback: Use Default
    Error --> Propagate: Cannot Handle
    Error --> Abort: Fatal Error

    Retry --> Attempt: Try Again
    Fallback --> [*]: Continue
    Propagate --> [*]: Return Error
    Abort --> [*]: Terminate
```

## Error Logging Flow

```mermaid
sequenceDiagram
    participant Code
    participant ErrorHandler
    participant Logger
    participant AlertSystem

    Code->>ErrorHandler: Error Occurred
    activate ErrorHandler

    ErrorHandler->>ErrorHandler: Classify Error

    alt Critical Error
        ErrorHandler->>Logger: Log with HIGH priority
        ErrorHandler->>AlertSystem: Send Alert
        AlertSystem-->>ErrorHandler: Alert Sent
    else Warning
        ErrorHandler->>Logger: Log with WARN priority
    else Info
        ErrorHandler->>Logger: Log with INFO priority
    end

    Logger-->>ErrorHandler: Logged
    ErrorHandler-->>Code: Error Handled

    deactivate ErrorHandler
```

## Best Practices

### Error Handling Decision Tree

```mermaid
graph TD
    A[Error Occurred] --> B{Can You Handle It?}

    B -->|Yes| C{Can Recover?}
    B -->|No| D[Propagate Up]

    C -->|Yes| E[Handle & Continue]
    C -->|No| F[Log & Return Error]

    D --> G[Add Context]
    G --> H[Return Result<T,E>]

    E --> I[Success Path]

    style E fill:#c8e6c9
    style D fill:#fff9c4
    style F fill:#ffe0b2
```

### When to Use Each Approach

```mermaid
graph LR
    subgraph "Use Result<T,E>"
        A1[Expected Errors]
        A2[Recoverable Errors]
        A3[Business Logic Errors]
    end

    subgraph "Use Exceptions"
        B1[Unexpected Errors]
        B2[Fatal Errors]
        B3[System Errors]
    end

    subgraph "Use Error Codes"
        C1[C API Interop]
        C2[Performance Critical]
        C3[Simple APIs]
    end

    style A1 fill:#c8e6c9
    style B1 fill:#fff9c4
    style C1 fill:#e1f5ff
```

## Error Message Guidelines

### Error Message Structure

```mermaid
graph LR
    A[Error Message] --> B[What Happened]
    B --> C[Why It Failed]
    C --> D[How to Fix]

    B -.->|"File not found"| B
    C -.->|"Path does not exist"| C
    D -.->|"Check file path"| D

    style A fill:#e1f5ff
    style D fill:#c8e6c9
```

## Error Types Comparison

| Feature | Result<T,E> | Exceptions | Error Codes |
|---------|------------|------------|-------------|
| **Performance** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Type Safety** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Composability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Error Context** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **C Interop** | ⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ |

## Example Patterns

### Layered Error Handling

```mermaid
graph TB
    subgraph "Application Layer"
        A[User Request]
    end

    subgraph "Business Logic Layer"
        B[Validate & Process]
        B2[Business Errors]
    end

    subgraph "Service Layer"
        C[Service Operations]
        C2[Service Errors]
    end

    subgraph "Data Layer"
        D[Database Operations]
        D2[Data Errors]
    end

    A --> B
    B --> C
    C --> D

    D -.->|Map Error| D2
    D2 -.->|Transform| C2
    C2 -.->|Enhance| B2
    B2 -.->|User-Friendly| A

    style A fill:#e1f5ff
    style D2 fill:#ffccbc
```

## See Also

- [Architecture Overview](index.md) - System design
- [Components](components.md) - Component interactions
- [Data Flow](data-flow.md) - Error flow patterns
- [Development: Debugging](../development/debugging.md) - Debugging techniques
