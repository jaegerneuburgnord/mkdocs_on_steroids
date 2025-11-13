# Core Classes

Fundamentale Klassen der C++ Advanced Library.

## String

UTF-8 String-Klasse mit optimierter Performance.

### Header

```cpp
#include <advlib/core/string.hpp>
```

### Declaration

```cpp
namespace advlib {
    class String {
    public:
        // Constructors
        String();
        String(const char* str);
        String(const std::string& str);
        String(StringView view);

        // Capacity
        size_t length() const noexcept;
        size_t size() const noexcept;
        size_t capacity() const noexcept;
        bool empty() const noexcept;

        // Element access
        char operator[](size_t pos) const;
        char& operator[](size_t pos);
        char at(size_t pos) const;
        char& at(size_t pos);

        // Modifiers
        void append(const String& str);
        void append(const char* str);
        void push_back(char c);
        void clear() noexcept;

        // Operations
        String substr(size_t pos, size_t len = npos) const;
        size_t find(const String& str, size_t pos = 0) const noexcept;
        String& replace(size_t pos, size_t len, const String& str);

        // Comparison
        int compare(const String& str) const noexcept;

        // Conversion
        const char* c_str() const noexcept;
        std::string to_std_string() const;

        // String specific
        String to_upper() const;
        String to_lower() const;
        bool starts_with(const String& prefix) const noexcept;
        bool ends_with(const String& suffix) const noexcept;

        static constexpr size_t npos = static_cast<size_t>(-1);
    };

    // Operators
    bool operator==(const String& lhs, const String& rhs);
    bool operator!=(const String& lhs, const String& rhs);
    bool operator<(const String& lhs, const String& rhs);
    String operator+(const String& lhs, const String& rhs);

    // Formatting
    template<typename... Args>
    String format(const char* fmt, Args&&... args);
}
```

### Examples

#### Basic Usage

```cpp
#include <advlib/core/string.hpp>

using namespace advlib;

// Construction
String s1;                          // Empty string
String s2("Hello");                 // From C-string
String s3(std::string("World"));    // From std::string

// Concatenation
String greeting = s2 + " " + s3;    // "Hello World"

// Length and access
size_t len = greeting.length();     // 11
char first = greeting[0];           // 'H'
char last = greeting.at(len - 1);   // 'd'

// Modification
greeting.append("!");               // "Hello World!"
greeting.push_back('?');            // "Hello World!?"

// Substring
String hello = greeting.substr(0, 5);  // "Hello"

// Find
size_t pos = greeting.find("World");   // 6

// Case conversion
String upper = greeting.to_upper();    // "HELLO WORLD!?"
String lower = greeting.to_lower();    // "hello world!?"

// Predicates
bool starts = greeting.starts_with("Hello");  // true
bool ends = greeting.ends_with("!?");         // true
```

#### String Formatting

```cpp
// Format strings with type-safe formatting
String name = "Alice";
int age = 30;

String message = format("User {} is {} years old", name, age);
// "User Alice is 30 years old"

// Advanced formatting
double pi = 3.14159265359;
String formatted = format("Pi = {:.2f}", pi);
// "Pi = 3.14"
```

#### Performance

```cpp
// Small String Optimization (SSO)
String small("short");  // Stored inline, no heap allocation

// Reserve capacity
String large;
large.reserve(1000);    // Pre-allocate
for (int i = 0; i < 1000; ++i) {
    large.push_back('x');  // No reallocation
}
```

---

## Result<T, E>

Type-safe error handling without exceptions.

### Header

```cpp
#include <advlib/core/result.hpp>
```

### Declaration

```cpp
namespace advlib {
    template<typename T, typename E>
    class Result {
    public:
        // Construction
        static Result Ok(T value);
        static Result Err(E error);

        // Queries
        bool is_ok() const noexcept;
        bool is_err() const noexcept;
        explicit operator bool() const noexcept;  // Same as is_ok()

        // Value access
        T& value() &;
        const T& value() const &;
        T&& value() &&;
        T value_or(T default_value) const &;

        E& error() &;
        const E& error() const &;
        E&& error() &&;

        // Monadic operations
        template<typename F>
        auto map(F&& func) -> Result<decltype(func(value())), E>;

        template<typename F>
        auto map_err(F&& func) -> Result<T, decltype(func(error()))>;

        template<typename F>
        auto and_then(F&& func) -> decltype(func(value()));

        template<typename F>
        auto or_else(F&& func) -> decltype(func(error()));

        // Pattern matching
        template<typename OnOk, typename OnErr>
        auto match(OnOk&& on_ok, OnErr&& on_err);
    };

    // Helper functions
    template<typename T>
    Result<T, E> Ok(T value);

    template<typename E>
    Result<T, E> Err(E error);
}
```

### Examples

#### Basic Usage

```cpp
#include <advlib/core/result.hpp>

using namespace advlib;

// Function returning Result
Result<int, String> divide(int a, int b) {
    if (b == 0) {
        return Err(String("Division by zero"));
    }
    return Ok(a / b);
}

// Check result
auto result = divide(10, 2);

if (result.is_ok()) {
    std::cout << "Result: " << result.value() << std::endl;
} else {
    std::cerr << "Error: " << result.error() << std::endl;
}

// Use value_or
int value = divide(10, 0).value_or(0);  // Returns 0 on error
```

#### Monadic Operations

```cpp
// map: Transform success value
auto result = divide(10, 2)
    .map([](int x) { return x * 2; });  // Result<int, String>

// map_err: Transform error value
auto result2 = divide(10, 0)
    .map_err([](const String& err) {
        return "ERROR: " + err;
    });

// and_then: Chain operations
auto result3 = divide(10, 2)
    .and_then([](int x) {
        return divide(x, 2);  // Returns Result
    })
    .and_then([](int x) {
        return divide(x, 2);
    });

// or_else: Fallback on error
auto result4 = divide(10, 0)
    .or_else([](const String& err) {
        log::warn("Division failed: {}", err);
        return Ok(0);  // Provide fallback
    });
```

#### Pattern Matching

```cpp
divide(10, 2).match(
    [](int value) {
        std::cout << "Success: " << value << std::endl;
    },
    [](const String& error) {
        std::cerr << "Error: " << error << std::endl;
    }
);
```

#### Complex Example

```cpp
Result<Config, String> load_and_validate_config(const String& path) {
    return open_file(path)
        .and_then([](File file) {
            return read_file(file);
        })
        .and_then([](const String& content) {
            return parse_json(content);
        })
        .and_then([](const Json& json) {
            return validate_config(json);
        })
        .map([](const Json& json) {
            return Config::from_json(json);
        })
        .map_err([&](const String& err) {
            return format("Failed to load config from {}: {}", path, err);
        });
}
```

---

## Optional<T>

Type for optional values.

### Header

```cpp
#include <advlib/core/optional.hpp>
```

### Declaration

```cpp
namespace advlib {
    template<typename T>
    class Optional {
    public:
        // Construction
        Optional();
        Optional(const T& value);
        Optional(T&& value);
        static Optional none();

        // Queries
        bool has_value() const noexcept;
        explicit operator bool() const noexcept;

        // Value access
        T& value() &;
        const T& value() const &;
        T&& value() &&;
        T value_or(T default_value) const &;

        T& operator*() &;
        const T& operator*() const &;
        T* operator->();
        const T* operator->() const;

        // Modifiers
        void reset() noexcept;
        template<typename... Args>
        T& emplace(Args&&... args);

        // Monadic operations
        template<typename F>
        auto map(F&& func) -> Optional<decltype(func(value()))>;

        template<typename F>
        auto and_then(F&& func) -> decltype(func(value()));

        template<typename F>
        auto or_else(F&& func) -> Optional<T>;
    };
}
```

### Examples

#### Basic Usage

```cpp
#include <advlib/core/optional.hpp>

using namespace advlib;

// Function returning Optional
Optional<String> find_user(int id) {
    if (database.has_user(id)) {
        return Optional<String>(database.get_user(id));
    }
    return Optional<String>::none();
}

// Check for value
auto user = find_user(42);

if (user.has_value()) {
    std::cout << "User: " << user.value() << std::endl;
}

// Or with operator bool
if (user) {
    std::cout << "User: " << *user << std::endl;
}

// value_or with default
String name = find_user(999).value_or("Anonymous");
```

#### Monadic Operations

```cpp
// map
auto upper_name = find_user(42)
    .map([](const String& name) {
        return name.to_upper();
    });

// and_then
auto email = find_user(42)
    .and_then([](const String& name) {
        return find_email(name);  // Returns Optional<String>
    });

// or_else
auto user_or_default = find_user(999)
    .or_else([]() {
        return Optional<String>("Default User");
    });
```

#### Pointer-like Operations

```cpp
struct User {
    String name;
    int age;

    void print() const {
        std::cout << name << " (" << age << ")" << std::endl;
    }
};

Optional<User> user = find_user_object(42);

// Arrow operator
if (user) {
    user->print();
    std::cout << user->name << std::endl;
}

// Dereference
if (user) {
    User& u = *user;
    u.age++;
}
```

---

## Smart Pointers

Memory-safe pointer types.

### UniquePtr<T>

```cpp
template<typename T, typename Deleter = DefaultDeleter<T>>
class UniquePtr {
public:
    // Construction
    UniquePtr() noexcept;
    explicit UniquePtr(T* ptr) noexcept;
    UniquePtr(T* ptr, Deleter deleter) noexcept;

    // Non-copyable
    UniquePtr(const UniquePtr&) = delete;
    UniquePtr& operator=(const UniquePtr&) = delete;

    // Movable
    UniquePtr(UniquePtr&& other) noexcept;
    UniquePtr& operator=(UniquePtr&& other) noexcept;

    // Access
    T* get() const noexcept;
    T& operator*() const;
    T* operator->() const noexcept;

    // Modifiers
    T* release() noexcept;
    void reset(T* ptr = nullptr) noexcept;
    void swap(UniquePtr& other) noexcept;

    // Observers
    explicit operator bool() const noexcept;
    Deleter& get_deleter() noexcept;
};

// Factory function
template<typename T, typename... Args>
UniquePtr<T> make_unique(Args&&... args);
```

#### UniquePtr Examples

```cpp
// Create
auto ptr = make_unique<MyClass>(42, "hello");

// Access
ptr->do_something();
(*ptr).member = 10;

// Transfer ownership
auto ptr2 = std::move(ptr);  // ptr is now nullptr

// Release raw pointer
T* raw = ptr2.release();  // Manual management now
delete raw;

// Reset with new value
ptr2.reset(new MyClass(100));

// Custom deleter
auto file = make_unique_with_deleter<FILE>(
    fopen("test.txt", "r"),
    [](FILE* f) { if (f) fclose(f); }
);
```

### SharedPtr<T>

```cpp
template<typename T>
class SharedPtr {
public:
    // Construction
    SharedPtr() noexcept;
    explicit SharedPtr(T* ptr);
    SharedPtr(const SharedPtr& other) noexcept;
    SharedPtr(SharedPtr&& other) noexcept;

    // Assignment
    SharedPtr& operator=(const SharedPtr& other) noexcept;
    SharedPtr& operator=(SharedPtr&& other) noexcept;

    // Access
    T* get() const noexcept;
    T& operator*() const;
    T* operator->() const noexcept;

    // Observers
    long use_count() const noexcept;
    bool unique() const noexcept;
    explicit operator bool() const noexcept;

    // Modifiers
    void reset() noexcept;
    void reset(T* ptr);
    void swap(SharedPtr& other) noexcept;
};

// Factory function
template<typename T, typename... Args>
SharedPtr<T> make_shared(Args&&... args);
```

#### SharedPtr Examples

```cpp
// Create
auto shared1 = make_shared<MyClass>(42);
auto shared2 = shared1;  // Reference count: 2

std::cout << "Use count: " << shared1.use_count() << std::endl;

// Weak reference
WeakPtr<MyClass> weak = shared1;

// Check if still alive
if (auto locked = weak.lock()) {
    locked->do_something();
} else {
    std::cout << "Object destroyed" << std::endl;
}
```

## See Also

- [Core Functions](core-functions.md)
- [Core Types](core-types.md)
- [Tutorials: Basic Concepts](../tutorials/beginner-concepts.md)
