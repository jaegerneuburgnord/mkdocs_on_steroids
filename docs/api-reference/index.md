# API Reference

Vollständige API-Dokumentation für die C++ Advanced Library.

## Module Overview

Die AdvLib API ist in mehrere spezialisierte Module organisiert:

### Core Module

| Komponente | Beschreibung | Header |
|------------|--------------|--------|
| [Classes](core-classes.md) | Fundamentale Klassen (String, Result, Optional) | `<advlib/core.hpp>` |
| [Functions](core-functions.md) | Utility-Funktionen und Helpers | `<advlib/core/functions.hpp>` |
| [Types](core-types.md) | Type Aliases und Traits | `<advlib/core/types.hpp>` |

### Utilities

| Komponente | Beschreibung | Header |
|------------|--------------|--------|
| [String Utilities](utils-string.md) | String-Manipulation und Parsing | `<advlib/utilities/string.hpp>` |
| [Math Utilities](utils-math.md) | Mathematische Funktionen | `<advlib/utilities/math.hpp>` |
| [IO Utilities](utils-io.md) | Input/Output Helpers | `<advlib/utilities/io.hpp>` |

### Containers

| Komponente | Beschreibung | Header |
|------------|--------------|--------|
| [Custom Containers](containers.md) | Hochperformante Container | `<advlib/containers.hpp>` |
| [Iterators](iterators.md) | Iterator-Interfaces | `<advlib/containers/iterator.hpp>` |

### Algorithms

| Komponente | Beschreibung | Header |
|------------|--------------|--------|
| [Sorting](algo-sorting.md) | Sortier-Algorithmen | `<advlib/algorithms/sort.hpp>` |
| [Search](algo-search.md) | Such-Algorithmen | `<advlib/algorithms/search.hpp>` |
| [Transform](algo-transform.md) | Transformations-Algorithmen | `<advlib/algorithms/transform.hpp>` |

## Quick Reference

### Commonly Used Types

```cpp
// String handling
advlib::String              // UTF-8 String
advlib::StringView          // Non-owning string view

// Error handling
advlib::Result<T, E>        // Result type
advlib::Optional<T>         // Optional value

// Smart pointers
advlib::UniquePtr<T>        // Unique ownership
advlib::SharedPtr<T>        // Shared ownership
advlib::WeakPtr<T>          // Weak reference

// Containers
advlib::FastVector<T>       // Optimized vector
advlib::HashMap<K, V>       // Hash map
advlib::SmallVector<T, N>   // Stack-allocated vector
```

### Commonly Used Functions

```cpp
// Logging
advlib::log::init(Level)
advlib::log::info(fmt, args...)
advlib::log::error(fmt, args...)

// String utilities
advlib::string_utils::trim(str)
advlib::string_utils::split(str, delim)
advlib::string_utils::to_upper(str)

// Memory
advlib::make_unique<T>(args...)
advlib::make_shared<T>(args...)

// Algorithms
advlib::parallel_sort(begin, end)
advlib::parallel_for(start, end, func)
```

## Naming Conventions

### Types

```cpp
// Classes: PascalCase
class String { };
class ThreadPool { };

// Templates: PascalCase
template<typename T>
class Optional { };

// Enums: PascalCase, Values: PascalCase
enum class LogLevel {
    Debug,
    Info,
    Warning,
    Error
};
```

### Functions

```cpp
// Functions: snake_case
void process_data();
int compute_result();

// Member functions: snake_case
class MyClass {
    void do_something();
    int get_value() const;
};
```

### Constants

```cpp
// Compile-time constants: kPascalCase
constexpr int kBufferSize = 1024;
constexpr char kVersion[] = "1.0.0";

// Macros: UPPER_CASE
#define ADVLIB_VERSION_MAJOR 1
#define ADVLIB_NO_EXCEPTIONS
```

## API Stability

### Stable API

Komponenten mit garantierter Rückwärtskompatibilität:

- `advlib::String`
- `advlib::Result<T, E>`
- `advlib::Optional<T>`
- `advlib::log::*`
- `advlib::ThreadPool`

### Experimental API

Features mit möglichen Breaking Changes:

!!! warning "Experimental"
    - `advlib::experimental::*` - Alle experimental features
    - `advlib::net::*` - Networking (Beta)
    - `advlib::graphics::*` - Graphics (Alpha)

Markiert mit:
```cpp
ADVLIB_EXPERIMENTAL
ADVLIB_UNSTABLE
```

## Version Macros

```cpp
// Version checks
#if ADVLIB_VERSION_MAJOR >= 1
    // Use v1.x features
#endif

// Feature detection
#ifdef ADVLIB_HAS_COROUTINES
    // Use coroutine features
#endif

#ifdef ADVLIB_HAS_CONCEPTS
    // Use C++20 concepts
#endif
```

## Platform-Specific APIs

### Platform Detection

```cpp
#ifdef ADVLIB_PLATFORM_WINDOWS
    // Windows-specific code
#endif

#ifdef ADVLIB_PLATFORM_LINUX
    // Linux-specific code
#endif

#ifdef ADVLIB_PLATFORM_MACOS
    // macOS-specific code
#endif

#ifdef ADVLIB_PLATFORM_EMBEDDED
    // Embedded systems code
#endif
```

### Compiler Detection

```cpp
#ifdef ADVLIB_COMPILER_GCC
    // GCC-specific code
#endif

#ifdef ADVLIB_COMPILER_CLANG
    // Clang-specific code
#endif

#ifdef ADVLIB_COMPILER_MSVC
    // MSVC-specific code
#endif
```

## Error Codes

Standard error codes in AdvLib:

```cpp
namespace advlib {
    enum class ErrorCode {
        Success = 0,
        InvalidArgument = 1,
        OutOfMemory = 2,
        NotFound = 3,
        PermissionDenied = 4,
        AlreadyExists = 5,
        Timeout = 6,
        Cancelled = 7,
        Unknown = 999
    };
}
```

## Deprecation Policy

Deprecated APIs sind markiert:

```cpp
// Deprecated function
ADVLIB_DEPRECATED("Use new_function() instead")
void old_function();

// Deprecated class
class ADVLIB_DEPRECATED("Use NewClass instead") OldClass {
    // ...
};
```

Deprecation Timeline:

1. **v1.x**: Feature wird als deprecated markiert
2. **v1.x+1**: Deprecation Warning
3. **v2.0**: Feature wird entfernt

## Thread Safety

Thread-Safety ist dokumentiert:

```cpp
// Thread-safe function
/// @threadsafe This function is thread-safe
void concurrent_function();

// Not thread-safe
/// @note This function is not thread-safe
void sequential_function();

// Conditionally thread-safe
/// @threadsafe Thread-safe if different instances
class MyClass { };
```

## Documentation Format

API-Dokumentation folgt diesem Format:

```cpp
/// @brief Brief description (one line)
///
/// Detailed description with multiple paragraphs if needed.
/// Can include code examples and usage notes.
///
/// @tparam T Template parameter description
/// @param arg Parameter description
/// @return Return value description
/// @throws ExceptionType When it throws
///
/// @note Additional notes
/// @warning Important warnings
/// @see Related functions or types
///
/// @example
/// @code
/// // Usage example
/// auto result = my_function(42);
/// @endcode
///
/// @since 1.0.0
template<typename T>
Result<T, Error> my_function(T arg);
```

## Navigation

### By Category

- **Core**: [Classes](core-classes.md) | [Functions](core-functions.md) | [Types](core-types.md)
- **Utilities**: [String](utils-string.md) | [Math](utils-math.md) | [IO](utils-io.md)
- **Containers**: [Containers](containers.md) | [Iterators](iterators.md)
- **Algorithms**: [Sorting](algo-sorting.md) | [Search](algo-search.md) | [Transform](algo-transform.md)

### By Use Case

- **Error Handling**: [Result Type](core-classes.md#result), [Optional Type](core-classes.md#optional)
- **String Processing**: [String Class](core-classes.md#string), [String Utils](utils-string.md)
- **Memory Management**: [Smart Pointers](core-classes.md#smart-pointers)
- **Concurrency**: [Thread Pool](../tutorials/advanced-concurrency.md), [Async](../tutorials/advanced-concurrency.md#asyncawait)
- **Performance**: [Parallel Algorithms](algo-sorting.md#parallel-sort), [SIMD](../tutorials/advanced-performance.md)

## Index

[Alphabetical Index of all APIs →](#)

## Contributing

Fehler in der Dokumentation gefunden?

- [Report Issue](https://github.com/youruser/advlib/issues)
- [Edit on GitHub](https://github.com/youruser/advlib/edit/main/docs/api-reference/)
