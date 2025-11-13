# Examples

Praktische Beispiele für häufige Anwendungsfälle mit der C++ Advanced Library.

## Übersicht

Lerne anhand von vollständigen, lauffähigen Beispielen:

### :beginner: [Basic Examples](basic-examples.md)

Einfache Beispiele für Einsteiger:

- Hello World Varianten
- String-Verarbeitung
- Datei-IO
- Einfaches Logging
- Error Handling

### :rocket: [Advanced Examples](advanced-examples.md)

Fortgeschrittene Anwendungsfälle:

- Async HTTP Client
- Thread Pool Anwendungen
- Custom Allocators
- Performance-Optimierungen
- Komplexe Datenstrukturen

### :art: [Design Patterns](design-patterns.md)

Implementierung klassischer Design Patterns:

- Factory Pattern
- Builder Pattern
- Observer Pattern
- Strategy Pattern
- RAII Patterns

### :briefcase: [Real-World Use Cases](use-cases.md)

Vollständige Anwendungen:

- REST API Client
- Log Analyzer
- Configuration Manager
- Data Processing Pipeline
- Web Server

## Quick Examples

### HTTP Client

```cpp
#include <advlib/net/http_client.hpp>

Task<void> fetch_data() {
    HttpClient client;

    auto response = co_await client.get("https://api.github.com/users/github");

    if (response.status() == 200) {
        log::info("Success: {}", response.body());
    }
}
```

### Parallel Processing

```cpp
#include <advlib/algorithms/parallel.hpp>

std::vector<int> data(1000000);
std::iota(data.begin(), data.end(), 0);

// Parallel transformation
parallel_transform(data.begin(), data.end(), data.begin(), [](int x) {
    return expensive_computation(x);
});

// Parallel reduce
auto sum = parallel_reduce(data.begin(), data.end(), 0, std::plus<>());
```

### Error Handling Pipeline

```cpp
#include <advlib/core.hpp>

Result<Config, Error> load_config(const String& path) {
    return read_file(path)
        .and_then(parse_json)
        .and_then(validate_schema)
        .map(Config::from_json)
        .map_err(log_and_wrap_error);
}

auto config = load_config("config.json")
    .value_or(Config::default_config());
```

### Thread Pool Example

```cpp
#include <advlib/concurrency/thread_pool.hpp>

ThreadPool pool(8);

// Submit tasks
std::vector<Future<int>> futures;
for (int i = 0; i < 100; ++i) {
    futures.push_back(pool.submit([i]() {
        return compute(i);
    }));
}

// Collect results
std::vector<int> results;
for (auto& future : futures) {
    results.push_back(future.get());
}
```

### Custom Container

```cpp
#include <advlib/containers.hpp>

// Vector with custom allocator
using MyVector = Vector<int, PoolAllocator<int>>;

PoolAllocator<int> allocator(1024);
MyVector vec(allocator);

for (int i = 0; i < 1000; ++i) {
    vec.push_back(i);  // Fast pool allocation
}
```

## Example Categories

### By Complexity

| Level | Examples | Count |
|-------|----------|-------|
| Beginner | Basic operations, simple I/O | 15 |
| Intermediate | Multi-threading, networking | 20 |
| Advanced | Performance tuning, metaprogramming | 10 |

### By Topic

| Topic | Description | Examples |
|-------|-------------|----------|
| **Core** | String, Result, Optional | 8 |
| **Concurrency** | Threading, Async/Await | 12 |
| **Networking** | HTTP, WebSocket | 6 |
| **Algorithms** | Sorting, Searching, Parallel | 10 |
| **Containers** | Custom containers, Allocators | 8 |
| **Patterns** | Design patterns | 11 |

## Running Examples

### Prerequisites

```bash
# Clone examples repository
git clone https://github.com/youruser/advlib-examples.git
cd advlib-examples

# Install dependencies
conan install . --build=missing
```

### Build All Examples

```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
```

### Run Specific Example

```bash
# Run HTTP client example
./build/examples/networking/http_client

# Run parallel processing example
./build/examples/algorithms/parallel_sort

# Run thread pool example
./build/examples/concurrency/thread_pool
```

## Example Structure

Jedes Beispiel folgt dieser Struktur:

```
examples/
├── category/
│   ├── example_name/
│   │   ├── main.cpp           # Hauptprogramm
│   │   ├── README.md          # Beschreibung
│   │   ├── CMakeLists.txt     # Build-Konfiguration
│   │   └── data/              # Testdaten (optional)
│   └── ...
└── ...
```

## Interactive Examples

### Online Compiler Explorer

Viele Beispiele sind auf Compiler Explorer verfügbar:

- [String Processing Examples](https://godbolt.org/z/example1)
- [Parallel Algorithms](https://godbolt.org/z/example2)
- [Error Handling](https://godbolt.org/z/example3)

### Docker Environment

Teste Beispiele in isolierter Umgebung:

```bash
# Pull Docker image mit allen Dependencies
docker pull advlib/examples:latest

# Run interaktive Shell
docker run -it advlib/examples:latest bash

# Compile und run examples
cd /examples
./build.sh
./run_example.sh http_client
```

## Code Snippets Library

Häufig verwendete Code-Schnipsel:

### Config Loading

```cpp
Result<Config, String> load_config(const String& path) {
    auto content = read_file(path);
    if (content.is_err()) {
        return Err("Cannot read file: " + path);
    }

    auto json = parse_json(content.value());
    if (json.is_err()) {
        return Err("Invalid JSON: " + json.error());
    }

    return Ok(Config::from_json(json.value()));
}
```

### Async File Processing

```cpp
Task<Result<String, Error>> process_file_async(const String& path) {
    auto content = co_await async_read_file(path);
    if (content.is_err()) {
        co_return Err(content.error());
    }

    auto processed = co_await async_process(content.value());
    co_return Ok(processed);
}
```

### Thread-Safe Singleton

```cpp
template<typename T>
class Singleton {
public:
    static T& instance() {
        static T instance;
        return instance;
    }

    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;

protected:
    Singleton() = default;
};
```

## Performance Comparisons

Beispiele mit Performance-Vergleichen:

### String Concatenation

```cpp
// Naive (slow)
String result;
for (int i = 0; i < 10000; ++i) {
    result = result + "x";  // O(n²) reallocations
}

// Optimized (fast)
String result;
result.reserve(10000);      // Pre-allocate
for (int i = 0; i < 10000; ++i) {
    result.push_back('x');  // O(n)
}

// Best (fastest)
String result(10000, 'x');  // Direct construction
```

### Parallel vs Sequential

```cpp
std::vector<int> data(10'000'000);

// Sequential: ~500ms
std::sort(data.begin(), data.end());

// Parallel: ~80ms
parallel_sort(data.begin(), data.end());

// SIMD-optimized: ~40ms
simd_sort(data.begin(), data.end());
```

## Example Tests

Alle Beispiele haben Tests:

```cpp
TEST(HttpClientExample, FetchData) {
    auto result = run_http_example();
    EXPECT_TRUE(result.is_ok());
}

TEST(ParallelSortExample, CorrectResult) {
    auto sorted = run_parallel_sort_example();
    EXPECT_TRUE(std::is_sorted(sorted.begin(), sorted.end()));
}
```

## Contributing Examples

Möchtest du ein Beispiel beitragen?

1. Fork das [Examples Repository](https://github.com/youruser/advlib-examples)
2. Erstelle ein neues Beispiel in der passenden Kategorie
3. Füge README.md mit Erklärung hinzu
4. Füge Tests hinzu
5. Erstelle Pull Request

Siehe [Contributing Guide](../development/contributing.md) für Details.

## Example Downloads

Einzelne Beispiele als ZIP:

- [HTTP Client Example](examples/http_client.zip) (5 KB)
- [Thread Pool Example](examples/thread_pool.zip) (3 KB)
- [Parallel Algorithms](examples/parallel_algos.zip) (8 KB)
- [All Examples](examples/all_examples.zip) (150 KB)

## Video Walkthroughs

Video-Tutorials für ausgewählte Beispiele:

- [Building a REST API Client](https://youtube.com/watch?v=example1) (15 min)
- [Parallel Data Processing](https://youtube.com/watch?v=example2) (20 min)
- [Custom Allocators in Practice](https://youtube.com/watch?v=example3) (25 min)

## Next Steps

- Starte mit [Basic Examples](basic-examples.md)
- Vertiefe mit [Advanced Examples](advanced-examples.md)
- Lerne [Design Patterns](design-patterns.md)
- Erkunde [Real-World Use Cases](use-cases.md)
