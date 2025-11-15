# Use Cases

Real-world use cases and application examples.

## Overview

This page provides complete, real-world examples of applications built with the library.

## Web Server

### Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        C1[Browser]
        C2[Mobile App]
        C3[API Client]
    end

    subgraph "Web Server"
        LB[Load Balancer]
        S1[Server Instance 1]
        S2[Server Instance 2]
        S3[Server Instance N]

        R[Router]
        H[HTTP Handler]
        MW[Middleware]
    end

    subgraph "Backend"
        BL[Business Logic]
        DB[Database]
        CACHE[Cache Layer]
    end

    C1 --> LB
    C2 --> LB
    C3 --> LB

    LB --> S1
    LB --> S2
    LB --> S3

    S1 --> R
    R --> MW
    MW --> H
    H --> BL

    BL --> DB
    BL --> CACHE

    style LB fill:#e1f5ff
    style H fill:#fff9c4
    style BL fill:#c8e6c9
```

### Request Flow

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant R as Router
    participant H as Handler
    participant DB as Database

    C->>S: HTTP Request
    activate S

    S->>R: Parse & Route
    R->>H: Dispatch to Handler

    activate H
    H->>H: Validate Request
    H->>DB: Query Data
    DB-->>H: Return Data
    H->>H: Process Response
    H-->>R: Response Data
    deactivate H

    R-->>S: HTTP Response
    S-->>C: Send Response
    deactivate S
```

### Implementation

```cpp
#include <advlib/net/http_server.hpp>
#include <advlib/async/task.hpp>

using namespace advlib;

class WebServer {
    HttpServer server_;
    Router router_;

public:
    WebServer(uint16_t port) : server_(port) {
        setup_routes();
    }

    void setup_routes() {
        // GET /api/users
        router_.get("/api/users", [](Request req) -> Task<Response> {
            auto users = co_await db::get_all_users();
            co_return Response::json(users);
        });

        // POST /api/users
        router_.post("/api/users", [](Request req) -> Task<Response> {
            auto user = co_await parse_json<User>(req.body());
            auto result = co_await db::create_user(user);
            co_return Response::json(result).status(201);
        });
    }

    void start() {
        server_.listen(router_);
    }
};
```

## Data Processing Pipeline

### Pipeline Architecture

```mermaid
graph LR
    A[Data Source] --> B[Ingestion]
    B --> C[Validation]
    C --> D[Transform]
    D --> E[Enrichment]
    E --> F[Aggregation]
    F --> G[Output]

    C -.->|Invalid| H[Error Queue]
    D -.->|Failed| H
    E -.->|Failed| H

    style A fill:#e1f5ff
    style D fill:#fff9c4
    style G fill:#c8e6c9
    style H fill:#ffccbc
```

### Parallel Processing

```mermaid
graph TD
    A[Large Dataset] --> B{Partition}

    B --> C1[Worker 1]
    B --> C2[Worker 2]
    B --> C3[Worker 3]
    B --> C4[Worker N]

    C1 --> D1[Process Chunk 1]
    C2 --> D2[Process Chunk 2]
    C3 --> D3[Process Chunk 3]
    C4 --> D4[Process Chunk N]

    D1 --> E[Merge Results]
    D2 --> E
    D3 --> E
    D4 --> E

    E --> F[Final Output]

    style A fill:#e1f5ff
    style E fill:#fff9c4
    style F fill:#c8e6c9
```

### Implementation

```cpp
#include <advlib/algorithms/parallel.hpp>
#include <advlib/containers/vector.hpp>

using namespace advlib;

class DataPipeline {
public:
    auto process(const Vector<RawData>& input) -> Result<Vector<ProcessedData>, Error> {
        // Step 1: Parallel validation
        auto validated = parallel_filter(input, [](const RawData& d) {
            return validate(d);
        });

        // Step 2: Parallel transformation
        Vector<TransformedData> transformed(validated.size());
        parallel_transform(
            validated.begin(), validated.end(),
            transformed.begin(),
            [](const RawData& d) { return transform(d); }
        );

        // Step 3: Parallel enrichment
        Vector<EnrichedData> enriched(transformed.size());
        parallel_transform(
            transformed.begin(), transformed.end(),
            enriched.begin(),
            [](const TransformedData& d) { return enrich(d); }
        );

        // Step 4: Aggregate
        auto result = parallel_reduce(
            enriched.begin(), enriched.end(),
            ProcessedData{},
            [](const ProcessedData& acc, const EnrichedData& d) {
                return aggregate(acc, d);
            }
        );

        return Ok(result);
    }
};
```

## Concurrent Task Scheduler

### Scheduler Architecture

```mermaid
graph TB
    subgraph "Task Submission"
        A1[User Tasks]
        A2[System Tasks]
        A3[Scheduled Tasks]
    end

    subgraph "Scheduler"
        B[Task Queue]
        C[Priority Queue]
        D[Delayed Queue]
        E[Scheduler Core]
    end

    subgraph "Execution"
        F[Thread Pool]
        G[Worker Threads]
    end

    A1 --> B
    A2 --> C
    A3 --> D

    B --> E
    C --> E
    D --> E

    E --> F
    F --> G

    style E fill:#fff9c4
    style F fill:#c8e6c9
```

### Task Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Submitted

    Submitted --> Pending: Enqueued
    Pending --> Running: Scheduled

    Running --> Completed: Success
    Running --> Failed: Error
    Running --> Cancelled: Cancel Request

    Completed --> [*]
    Failed --> Retry: Retriable
    Failed --> [*]: Give Up
    Cancelled --> [*]

    Retry --> Pending
```

### Implementation

```cpp
#include <advlib/concurrency/scheduler.hpp>
#include <advlib/async/task.hpp>

using namespace advlib;

class TaskScheduler {
    Scheduler scheduler_;
    ThreadPool pool_;

public:
    TaskScheduler() : pool_(std::thread::hardware_concurrency()) {}

    // Schedule immediate task
    auto schedule(Task<void> task) -> TaskHandle {
        return scheduler_.submit(std::move(task));
    }

    // Schedule delayed task
    auto schedule_after(Duration delay, Task<void> task) -> TaskHandle {
        return scheduler_.submit_delayed(delay, std::move(task));
    }

    // Schedule recurring task
    auto schedule_recurring(Duration interval, Task<void> task) -> TaskHandle {
        return scheduler_.submit_recurring(interval, std::move(task));
    }

    // Cancel task
    void cancel(TaskHandle handle) {
        scheduler_.cancel(handle);
    }
};
```

## Game Engine Component

### Entity Component System

```mermaid
graph TB
    subgraph "Entities"
        E1[Player]
        E2[Enemy]
        E3[Projectile]
    end

    subgraph "Components"
        C1[Transform]
        C2[Render]
        C3[Physics]
        C4[Health]
    end

    subgraph "Systems"
        S1[Render System]
        S2[Physics System]
        S3[Combat System]
    end

    E1 --> C1
    E1 --> C2
    E1 --> C3
    E1 --> C4

    E2 --> C1
    E2 --> C2
    E2 --> C4

    E3 --> C1
    E3 --> C3

    C1 --> S1
    C2 --> S1
    C3 --> S2
    C4 --> S3

    style E1 fill:#e1f5ff
    style S1 fill:#c8e6c9
```

### Game Loop

```mermaid
sequenceDiagram
    participant Main
    participant Input
    participant Physics
    participant Render
    participant Audio

    loop Every Frame
        Main->>Input: Process Input
        Main->>Physics: Update(deltaTime)
        activate Physics
        Physics->>Physics: Collision Detection
        Physics->>Physics: Update Positions
        deactivate Physics

        Main->>Render: Render Frame
        activate Render
        Render->>Render: Update Camera
        Render->>Render: Draw Entities
        deactivate Render

        Main->>Audio: Update Audio
    end
```

## Scientific Computing Application

### Computation Pipeline

```mermaid
graph LR
    A[Input Data] --> B[Preprocessing]
    B --> C[Numerical Solver]
    C --> D[Post-processing]
    D --> E[Visualization]
    E --> F[Results]

    C --> G[Parallel Computation]
    G --> H[GPU Acceleration]
    G --> I[SIMD Operations]

    style C fill:#fff9c4
    style G fill:#c8e6c9
```

### Matrix Operations

```cpp
#include <advlib/math/matrix.hpp>
#include <advlib/algorithms/parallel.hpp>

using namespace advlib;

class ScientificApp {
public:
    // Parallel matrix multiplication
    auto matrix_multiply(const Matrix& A, const Matrix& B) -> Matrix {
        Matrix C(A.rows(), B.cols());

        parallel_for_2d(0, A.rows(), 0, B.cols(), [&](size_t i, size_t j) {
            double sum = 0.0;
            for (size_t k = 0; k < A.cols(); ++k) {
                sum += A(i, k) * B(k, j);
            }
            C(i, j) = sum;
        });

        return C;
    }

    // Solve linear system using iterative method
    auto solve_linear_system(const Matrix& A, const Vector& b)
        -> Result<Vector, Error> {
        // Implementation here
        return Ok(Vector{});
    }
};
```

## See Also

- [Basic Examples](basic-examples.md) - Simple examples
- [Advanced Examples](advanced-examples.md) - Complex examples
- [Design Patterns](design-patterns.md) - Common patterns
- [API Reference](../api-reference/index.md) - Detailed API docs
