# Data Flow

Understanding how data flows through the system.

## Overview

This document describes how data moves through the various components of the library, including synchronous and asynchronous patterns.

## General Data Flow Architecture

```mermaid
graph TB
    A[Input Source] --> B[Validation Layer]
    B --> C{Valid?}

    C -->|Yes| D[Processing Pipeline]
    C -->|No| E[Error Handler]

    D --> F[Transform]
    F --> G[Business Logic]
    G --> H[Persist/Output]

    E --> I[Log Error]
    I --> J[Error Response]

    H --> K[Success Response]

    style A fill:#e1f5ff
    style D fill:#c8e6c9
    style E fill:#ffccbc
    style H fill:#fff9c4
```

## Data Flow Patterns

### 1. Request-Response Pattern

The most common synchronous data flow pattern.

```mermaid
sequenceDiagram
    participant C as Client
    participant V as Validator
    participant P as Processor
    participant D as Database
    participant L as Logger

    C->>V: Send Request
    activate V

    V->>V: Validate Input

    alt Input Valid
        V->>P: Forward Request
        activate P

        P->>D: Query Data
        activate D
        D-->>P: Return Data
        deactivate D

        P->>P: Process Data
        P->>L: Log Success
        P-->>V: Return Result
        deactivate P

        V-->>C: Success Response
    else Input Invalid
        V->>L: Log Error
        V-->>C: Error Response
    end

    deactivate V
```

### 2. Pipeline Pattern

Data flows through a series of transformation stages.

```mermaid
graph LR
    A[Raw Data] --> B[Stage 1: Parse]
    B --> C[Stage 2: Validate]
    C --> D[Stage 3: Transform]
    D --> E[Stage 4: Enrich]
    E --> F[Stage 5: Format]
    F --> G[Output]

    B -.->|Error| H[Error Handler]
    C -.->|Error| H
    D -.->|Error| H
    E -.->|Error| H
    F -.->|Error| H

    style A fill:#e1f5ff
    style G fill:#c8e6c9
    style H fill:#ffccbc
```

**Example:**
```cpp
auto result = load_data("input.json")
    | parse_json()
    | validate_schema()
    | transform_fields()
    | enrich_with_defaults()
    | format_output();
```

### 3. Pub-Sub Pattern

Event-driven data flow with publishers and subscribers.

```mermaid
graph TD
    P1[Publisher 1] -->|Event A| EB[Event Bus]
    P2[Publisher 2] -->|Event B| EB
    P3[Publisher 3] -->|Event C| EB

    EB -->|Event A| S1[Subscriber 1]
    EB -->|Event A| S2[Subscriber 2]
    EB -->|Event B| S2
    EB -->|Event C| S3[Subscriber 3]
    EB -->|Event C| S4[Subscriber 4]

    style EB fill:#fff9c4
    style P1 fill:#e1f5ff
    style P2 fill:#e1f5ff
    style P3 fill:#e1f5ff
```

### 4. Stream Processing

Continuous data flow for real-time processing.

```mermaid
graph LR
    A[Data Stream] --> B[Buffer]
    B --> C[Batch]

    C --> D{Filter}
    D -->|Pass| E[Map]
    D -->|Reject| F[Discard]

    E --> G[Reduce]
    G --> H[Aggregate]

    H --> I[Windowing]
    I --> J[Output Stream]

    style A fill:#e1f5ff
    style H fill:#fff9c4
    style J fill:#c8e6c9
```

## Asynchronous Data Flow

### Async Request Flow

```mermaid
sequenceDiagram
    participant App
    participant RT as Runtime
    participant H1 as Handler 1
    participant H2 as Handler 2
    participant DB

    App->>RT: Async Request
    RT->>H1: Process Part 1

    Note over H1: Non-blocking operation
    H1->>RT: Suspend & Yield

    RT->>H2: Process Other Tasks

    DB-->>RT: Data Ready
    RT->>H1: Resume

    H1->>DB: Fetch Data
    DB-->>H1: Return Data

    H1->>RT: Complete
    RT-->>App: Result
```

### Parallel Data Flow

Multiple data streams processed concurrently.

```mermaid
graph TD
    A[Input Data] --> B{Split}

    B --> C1[Thread 1]
    B --> C2[Thread 2]
    B --> C3[Thread 3]
    B --> C4[Thread 4]

    C1 --> D[Process Chunk 1]
    C2 --> E[Process Chunk 2]
    C3 --> F[Process Chunk 3]
    C4 --> G[Process Chunk 4]

    D --> H{Merge}
    E --> H
    F --> H
    G --> H

    H --> I[Combined Result]

    style A fill:#e1f5ff
    style H fill:#fff9c4
    style I fill:#c8e6c9
```

## State Management

### State Transitions

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> Loading: Load Data
    Loading --> Processing: Data Loaded
    Loading --> Error: Load Failed

    Processing --> Validating: Process Complete
    Validating --> Saving: Valid
    Validating --> Error: Invalid

    Saving --> Success: Save Complete
    Saving --> Error: Save Failed

    Success --> Idle: Reset
    Error --> Idle: Retry
    Error --> [*]: Abort

    Success --> [*]: Done
```

### State Storage Flow

```mermaid
graph LR
    A[Application State] --> B{Storage Strategy}

    B -->|Memory| C[In-Memory Store]
    B -->|Disk| D[File System]
    B -->|Database| E[DB Connection]
    B -->|Cache| F[Cache Layer]

    C --> G[Read/Write]
    D --> G
    E --> G
    F --> G

    G --> H[State Updated]

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style H fill:#c8e6c9
```

## Event Handling

### Event Lifecycle

```mermaid
sequenceDiagram
    participant S as Source
    participant D as Dispatcher
    participant F as Filter
    participant H as Handler
    participant L as Logger

    S->>D: Emit Event
    D->>F: Check Filters

    alt Event Passes Filter
        F->>H: Dispatch to Handler
        activate H

        H->>H: Process Event

        alt Success
            H->>L: Log Success
            H-->>D: Event Handled
        else Error
            H->>L: Log Error
            H-->>D: Handler Failed
        end

        deactivate H
    else Event Filtered
        F->>L: Log Filtered
        F-->>D: Event Dropped
    end
```

### Event Bus Architecture

```mermaid
graph TB
    subgraph "Event Sources"
        E1[User Action]
        E2[System Event]
        E3[Timer Event]
        E4[Network Event]
    end

    E1 --> EB[Event Bus]
    E2 --> EB
    E3 --> EB
    E4 --> EB

    EB --> Q1[Priority Queue]
    EB --> Q2[Standard Queue]

    Q1 --> D[Dispatcher]
    Q2 --> D

    D --> H1[Handler A]
    D --> H2[Handler B]
    D --> H3[Handler C]

    style EB fill:#fff9c4
    style D fill:#c8e6c9
```

## Data Transformation Patterns

### Map-Reduce Flow

```mermaid
graph TB
    A[Input Dataset] --> B[Split into Chunks]

    B --> M1[Map: Chunk 1]
    B --> M2[Map: Chunk 2]
    B --> M3[Map: Chunk 3]
    B --> M4[Map: Chunk 4]

    M1 --> S1[Shuffle & Sort]
    M2 --> S1
    M3 --> S1
    M4 --> S1

    S1 --> R1[Reduce: Group 1]
    S1 --> R2[Reduce: Group 2]
    S1 --> R3[Reduce: Group 3]

    R1 --> F[Final Result]
    R2 --> F
    R3 --> F

    style A fill:#e1f5ff
    style S1 fill:#fff9c4
    style F fill:#c8e6c9
```

### Filter-Map-Reduce Chain

```mermaid
graph LR
    A[Collection] --> B[Filter]
    B --> C[Map]
    C --> D[Reduce]
    D --> E[Result]

    B -.->|Predicate| F[Keep/Discard]
    C -.->|Transform| G[New Type]
    D -.->|Accumulate| H[Single Value]

    style A fill:#e1f5ff
    style E fill:#c8e6c9
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

## Memory Flow

### Object Lifetime

```mermaid
graph TD
    A[Object Created] --> B[Stack/Heap?]

    B -->|Stack| C[Stack Frame]
    B -->|Heap| D[Heap Allocation]

    C --> E[Automatic Lifetime]
    D --> F[Manual Management]

    E --> G[Scope Exit]
    G --> H[Destructor Called]
    H --> I[Memory Released]

    F --> J{Smart Pointer?}
    J -->|Yes| K[Ref Count]
    J -->|No| L[Manual Delete]

    K --> M[Last Ref Dropped]
    M --> H
    L --> H

    I --> N[Memory Available]

    style A fill:#e1f5ff
    style I fill:#c8e6c9
```

### Memory Pool Flow

```mermaid
sequenceDiagram
    participant A as Application
    participant P as Memory Pool
    participant M as Memory Block

    A->>P: Request Memory
    activate P

    alt Pool Has Free Block
        P->>M: Get Free Block
        M-->>P: Block Address
        P-->>A: Return Memory
    else Pool Empty
        P->>P: Allocate New Chunk
        P->>M: Get Block from Chunk
        M-->>P: Block Address
        P-->>A: Return Memory
    end

    deactivate P

    Note over A: Use Memory

    A->>P: Return Memory
    P->>M: Mark as Free
```

## Caching Flow

### Multi-Level Cache

```mermaid
graph TD
    A[Request] --> B{L1 Cache?}

    B -->|Hit| C[Return from L1]
    B -->|Miss| D{L2 Cache?}

    D -->|Hit| E[Return from L2]
    D -->|Miss| F{L3 Cache?}

    F -->|Hit| G[Return from L3]
    F -->|Miss| H[Load from Source]

    H --> I[Update Caches]
    I --> J[Return Data]

    E --> K[Promote to L1]
    G --> L[Promote to L2]

    style C fill:#c8e6c9
    style E fill:#c8e6c9
    style G fill:#c8e6c9
    style H fill:#ffccbc
```

## Best Practices

### 1. Minimize Data Copies

```mermaid
graph LR
    A[Source] -->|Move| B[Destination]
    A -.->|Copy Avoided| C[Original Destroyed]

    D[Source] -->|Copy| E[Destination]
    D -.->|Keep| F[Original Preserved]

    style A fill:#e1f5ff
    style B fill:#c8e6c9
    style D fill:#e1f5ff
    style E fill:#c8e6c9
```

**Prefer Move Semantics:**
```cpp
// Good: Move
Vector<int> data = create_large_vector();

// Avoid: Copy
Vector<int> data = Vector<int>(create_large_vector());
```

### 2. Pipeline Optimization

```mermaid
graph TD
    A[Unoptimized] --> B[Step 1: Load]
    B --> C[Step 2: Parse]
    C --> D[Step 3: Validate]
    D --> E[Step 4: Process]

    F[Optimized] --> G[Step 1: Load & Parse]
    G --> H[Step 2: Validate & Process]

    style F fill:#c8e6c9
    style A fill:#ffccbc
```

### 3. Lazy Evaluation

```mermaid
graph LR
    A[Define Operation] --> B[Build Pipeline]
    B --> C[No Execution Yet]
    C --> D[Trigger Evaluation]
    D --> E[Execute All Steps]
    E --> F[Return Result]

    style A fill:#e1f5ff
    style D fill:#fff9c4
    style F fill:#c8e6c9
```

## See Also

- [Components](components.md) - Component interactions
- [Threading Model](threading.md) - Concurrent data flow
- [Error Handling](error-handling.md) - Error propagation
- [Performance Tips](../tutorials/advanced-performance.md) - Optimization techniques
