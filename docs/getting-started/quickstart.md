# Quick Start

Erstelle deine erste Anwendung mit der C++ Advanced Library in wenigen Minuten!

## 5-Minuten Schnellstart

### Schritt 1: Projekt erstellen

Erstelle ein neues Verzeichnis für dein Projekt:

```bash
mkdir my-advlib-project
cd my-advlib-project
```

### Schritt 2: CMakeLists.txt erstellen

Erstelle eine `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyAdvLibProject VERSION 1.0.0)

# C++20 Standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Finde AdvancedLib
find_package(AdvancedLib REQUIRED COMPONENTS Core Algorithms Utilities)

# Hauptprogramm
add_executable(my_app main.cpp)

target_link_libraries(my_app
    PRIVATE
        AdvancedLib::Core
        AdvancedLib::Algorithms
        AdvancedLib::Utilities
)

# Compiler Warnings
if(MSVC)
    target_compile_options(my_app PRIVATE /W4)
else()
    target_compile_options(my_app PRIVATE -Wall -Wextra -Wpedantic)
endif()
```

### Schritt 3: Hauptprogramm erstellen

Erstelle `main.cpp`:

```cpp
#include <advlib/core.hpp>
#include <advlib/algorithms/sort.hpp>
#include <advlib/utilities/string.hpp>
#include <iostream>
#include <vector>

using namespace advlib;

int main() {
    // 1. Logging initialisieren
    log::init(log::Level::Info);
    log::info("Starting AdvLib Quick Start Example");

    // 2. String Utilities
    String greeting = "  Hello, AdvLib!  ";
    auto trimmed = string_utils::trim(greeting);
    log::info("Trimmed string: '{}'", trimmed);

    // 3. Vector mit paralleler Sortierung
    std::vector<int> numbers = {42, 17, 8, 93, 23, 5, 67, 11};
    log::info("Original: {}", numbers);

    parallel_sort(numbers.begin(), numbers.end());
    log::info("Sorted: {}", numbers);

    // 4. Result Type für Fehlerbehandlung
    auto parse_result = parse_number<int>("12345");
    if (parse_result.is_ok()) {
        log::info("Parsed number: {}", parse_result.value());
    } else {
        log::error("Parsing failed: {}", parse_result.error());
    }

    // 5. Optional Type
    Optional<String> maybe_value = find_in_config("database.url");
    if (maybe_value.has_value()) {
        log::info("Config value: {}", maybe_value.value());
    } else {
        log::warn("Config value not found");
    }

    // 6. Smart Pointers und Memory Management
    auto unique = make_unique<MyClass>(42);
    auto shared = make_shared<MyClass>(100);

    log::info("Quick Start completed successfully!");
    return 0;
}

// Hilfsfunktion
Optional<String> find_in_config(const String& key) {
    // Simuliere Config-Lookup
    if (key == "database.url") {
        return Optional<String>("postgresql://localhost:5432/mydb");
    }
    return Optional<String>::none();
}

// Beispielklasse
class MyClass {
public:
    explicit MyClass(int val) : value_(val) {
        log::debug("MyClass constructed with value: {}", val);
    }

    ~MyClass() {
        log::debug("MyClass destroyed");
    }

private:
    int value_;
};
```

### Schritt 4: Bauen und Ausführen

```bash
# Build
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build

# Ausführen
./build/my_app
```

**Erwartete Ausgabe:**

```
[INFO] Starting AdvLib Quick Start Example
[INFO] Trimmed string: 'Hello, AdvLib!'
[INFO] Original: [42, 17, 8, 93, 23, 5, 67, 11]
[INFO] Sorted: [5, 8, 11, 17, 23, 42, 67, 93]
[INFO] Parsed number: 12345
[INFO] Config value: postgresql://localhost:5432/mydb
[INFO] Quick Start completed successfully!
```

## Kernkonzepte

### 1. Namespaces

Alle AdvLib-Komponenten sind im `advlib` Namespace:

```cpp
namespace advlib {
    // Alle Library-Features
}

// Verwendung
using namespace advlib;           // Ganzer Namespace
using advlib::String;             // Einzelner Type
using namespace advlib::log;      // Sub-Namespace
```

### 2. Error Handling

AdvLib verwendet `Result<T, E>` für Fehlerbehandlung:

```cpp
Result<int, String> divide(int a, int b) {
    if (b == 0) {
        return Err("Division by zero");
    }
    return Ok(a / b);
}

auto result = divide(10, 2);
if (result.is_ok()) {
    std::cout << "Result: " << result.value() << std::endl;
} else {
    std::cerr << "Error: " << result.error() << std::endl;
}

// Oder mit Pattern Matching
result.match(
    [](int value) { std::cout << "Success: " << value << std::endl; },
    [](const String& err) { std::cerr << "Error: " << err << std::endl; }
);
```

### 3. Optional Values

Für optionale Werte statt Null-Pointer:

```cpp
Optional<String> find_user(int id) {
    if (user_exists(id)) {
        return Optional<String>("John Doe");
    }
    return Optional<String>::none();
}

// Verwendung
auto user = find_user(42);

// Methode 1: Explizite Prüfung
if (user.has_value()) {
    std::cout << "User: " << user.value() << std::endl;
}

// Methode 2: value_or mit Default
std::cout << "User: " << user.value_or("Anonymous") << std::endl;

// Methode 3: map und and_then
user.map([](const String& name) {
    return name.to_upper();
}).and_then([](const String& name) {
    return send_email(name);
});
```

### 4. Smart Pointers

Modern C++ Memory Management:

```cpp
// Unique Ownership
auto unique_ptr = make_unique<LargeObject>(args);

// Shared Ownership
auto shared_ptr = make_shared<LargeObject>(args);

// Weak Reference
WeakPtr<LargeObject> weak_ptr = shared_ptr;

// Custom Deleters
auto file_ptr = UniquePtr<FILE, FileDeleter>(fopen("test.txt", "r"));
```

### 5. Ranges und Iteratoren

Modern Range-basierte APIs:

```cpp
std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

// Filter und Transform
auto evens = numbers
    | views::filter([](int n) { return n % 2 == 0; })
    | views::transform([](int n) { return n * n; });

for (int n : evens) {
    std::cout << n << " ";  // 4 16 36 64 100
}
```

## Häufige Patterns

### Pattern 1: RAII Resource Management

```cpp
class FileHandle {
public:
    explicit FileHandle(const char* filename)
        : file_(fopen(filename, "r")) {
        if (!file_) {
            throw std::runtime_error("Failed to open file");
        }
    }

    ~FileHandle() {
        if (file_) {
            fclose(file_);
        }
    }

    // Non-copyable
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Movable
    FileHandle(FileHandle&& other) noexcept
        : file_(other.file_) {
        other.file_ = nullptr;
    }

    FILE* get() const { return file_; }

private:
    FILE* file_;
};
```

### Pattern 2: Builder Pattern

```cpp
auto config = ConfigBuilder()
    .with_host("localhost")
    .with_port(8080)
    .with_timeout(std::chrono::seconds(30))
    .with_ssl(true)
    .build();
```

### Pattern 3: Async Operations

```cpp
Task<Response> fetch_data() {
    HttpClient client;

    // Asynchroner Request
    auto response = co_await client.get("https://api.example.com/data");

    // Verarbeite Response
    if (response.status() == 200) {
        co_return response;
    }

    throw std::runtime_error("Request failed");
}

// Verwendung
auto future = fetch_data();
auto response = future.get();
```

## Nächste Schritte

Jetzt, wo du die Grundlagen kennst:

- :material-book-open: Lerne mehr in den [Tutorials](../tutorials/index.md)
- :material-file-document: Erkunde die [API Reference](../api-reference/index.md)
- :material-code-braces: Schau dir [Beispiele](../examples/index.md) an

## Vollständiges Beispielprojekt

Ein vollständiges Beispielprojekt mit Build-System, Tests und CI/CD findest du im [examples](../examples/) Verzeichnis:

```bash
git clone https://github.com/youruser/advlib-examples
cd advlib-examples
```

!!! tip "Pro-Tipp"
    Nutze die mitgelieferten CMake Presets für schnellere Konfiguration:

    ```bash
    cmake --preset=release
    cmake --build --preset=release
    ```
