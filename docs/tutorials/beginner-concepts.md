# Basic Concepts

Verstehe die fundamentalen Konzepte der C++ Advanced Library.

## Lernziele

- [x] Namespaces und Module verstehen
- [x] Error Handling mit Result<T, E>
- [x] Optional<T> für optionale Werte
- [x] Smart Pointers und Ownership
- [x] RAII Patterns

**Geschätzte Zeit:** 30 Minuten

## Namespace-Struktur

AdvLib organisiert Code in logische Namespaces:

```cpp
namespace advlib {
    // Core Funktionalität
    namespace log { /* Logging System */ }
    namespace mem { /* Memory Management */ }

    // Utilities
    namespace string_utils { /* String Helpers */ }
    namespace math { /* Math Functions */ }

    // Algorithms
    namespace algo { /* Algorithms */ }

    // Networking
    namespace net { /* Networking */ }
}
```

### Namespace-Verwendung

```cpp
// Methode 1: Voll qualifiziert
advlib::log::info("Message");

// Methode 2: Using Declaration
using advlib::log::info;
info("Message");

// Methode 3: Using Namespace (in Funktionen OK)
void myFunction() {
    using namespace advlib::log;
    info("Message");
}

// Methode 4: Namespace Alias
namespace alog = advlib::log;
alog::info("Message");
```

!!! warning "Vorsicht"
    Vermeide `using namespace advlib;` in Header-Dateien!

## Error Handling mit Result<T, E>

Result ist ein Type für Fehlerbehandlung ohne Exceptions.

### Grundkonzept

```cpp
#include <advlib/core/result.hpp>

using namespace advlib;

// Funktion die fehlschlagen kann
Result<int, String> divide(int a, int b) {
    if (b == 0) {
        return Err(String("Division by zero"));
    }
    return Ok(a / b);
}
```

### Result verwenden

=== "Explizite Prüfung"

    ```cpp
    auto result = divide(10, 2);

    if (result.is_ok()) {
        int value = result.value();
        std::cout << "Result: " << value << std::endl;
    } else {
        String error = result.error();
        std::cerr << "Error: " << error << std::endl;
    }
    ```

=== "Pattern Matching"

    ```cpp
    result.match(
        [](int value) {
            std::cout << "Success: " << value << std::endl;
        },
        [](const String& error) {
            std::cerr << "Error: " << error << std::endl;
        }
    );
    ```

=== "Operatoren"

    ```cpp
    // value_or: Liefere Wert oder Default
    int value = divide(10, 2).value_or(0);

    // map: Transformiere Erfolg
    auto doubled = divide(10, 2).map([](int x) {
        return x * 2;
    });

    // and_then: Verkette Operations
    auto result = divide(10, 2)
        .and_then([](int x) {
            return divide(x, 2);
        });
    ```

### Komplexes Beispiel

```cpp
Result<Config, String> load_config(const String& path) {
    // Datei öffnen
    auto file = open_file(path);
    if (file.is_err()) {
        return Err("Cannot open file: " + path);
    }

    // Parse JSON
    auto json = parse_json(file.value());
    if (json.is_err()) {
        return Err("Invalid JSON: " + json.error());
    }

    // Validiere Config
    auto config = validate_config(json.value());
    if (config.is_err()) {
        return Err("Invalid config: " + config.error());
    }

    return Ok(config.value());
}

// Verwendung
auto config_result = load_config("config.json");
config_result.match(
    [](const Config& cfg) {
        log::info("Config loaded successfully");
        use_config(cfg);
    },
    [](const String& error) {
        log::error("Failed to load config: {}", error);
        use_default_config();
    }
);
```

## Optional<T>

Optional für Werte, die vorhanden sein können oder nicht.

### Grundlagen

```cpp
#include <advlib/core/optional.hpp>

using namespace advlib;

Optional<String> find_user(int id) {
    if (database.has_user(id)) {
        return Optional<String>(database.get_user(id));
    }
    return Optional<String>::none();  // Kein Wert
}
```

### Optional verwenden

```cpp
auto user = find_user(42);

// Methode 1: has_value() prüfen
if (user.has_value()) {
    std::cout << "User: " << user.value() << std::endl;
}

// Methode 2: value_or mit Default
std::cout << "User: " << user.value_or("Anonymous") << std::endl;

// Methode 3: map und transform
auto upper_name = user.map([](const String& name) {
    return name.to_upper();
});

// Methode 4: and_then für Verkettung
auto email = user.and_then([](const String& name) {
    return find_email(name);
});
```

### Optional vs Pointer

!!! success "Optional verwenden"
    ```cpp
    Optional<User> find_user(int id);  // Klar: kann leer sein
    ```

!!! failure "Pointer vermeiden"
    ```cpp
    User* find_user(int id);  // Unklar: nullptr? Ownership?
    ```

### Komplexes Beispiel

```cpp
class UserService {
public:
    Optional<User> authenticate(const String& username, const String& password) {
        // Finde User
        auto user_opt = find_user_by_name(username);
        if (!user_opt.has_value()) {
            log::warn("User not found: {}", username);
            return Optional<User>::none();
        }

        // Prüfe Passwort
        auto& user = user_opt.value();
        if (!verify_password(user, password)) {
            log::warn("Invalid password for user: {}", username);
            return Optional<User>::none();
        }

        log::info("User authenticated: {}", username);
        return user_opt;
    }

private:
    Optional<User> find_user_by_name(const String& username) {
        // Database lookup...
        return Optional<User>::none();
    }

    bool verify_password(const User& user, const String& password) {
        // Password verification...
        return false;
    }
};
```

## Smart Pointers

AdvLib erweitert Standard Smart Pointers mit zusätzlichen Features.

### UniquePtr<T>

Eindeutige Ownership:

```cpp
#include <advlib/memory/smart_ptr.hpp>

using namespace advlib;

// Erstelle unique pointer
auto ptr = make_unique<MyClass>(42, "hello");

// Ownership Transfer
auto ptr2 = std::move(ptr);  // ptr ist nun nullptr

// Custom Deleter
auto file = make_unique_with_deleter<FILE>(
    fopen("test.txt", "r"),
    [](FILE* f) { if (f) fclose(f); }
);
```

### SharedPtr<T>

Geteilte Ownership:

```cpp
// Erstelle shared pointer
auto shared1 = make_shared<MyClass>(42);
auto shared2 = shared1;  // Reference count erhöht

std::cout << "Use count: " << shared1.use_count() << std::endl;  // 2

// Weak Reference (bricht Zyklus)
WeakPtr<MyClass> weak = shared1;

if (auto locked = weak.lock()) {
    // Objekt existiert noch
    locked->do_something();
}
```

### IntrusivePtr<T>

Effizientere shared ownership mit intrusive reference counting:

```cpp
class MyRefCounted : public RefCounted {
public:
    MyRefCounted(int val) : value_(val) {}

    void do_something() {
        std::cout << "Value: " << value_ << std::endl;
    }

private:
    int value_;
};

// Verwende IntrusivePtr
auto ptr = make_intrusive<MyRefCounted>(42);
auto ptr2 = ptr;  // Effizient, keine extra Allokation
```

### Smart Pointer Guidelines

!!! tip "Best Practices"
    - **Prefer UniquePtr**: Standardwahl für Ownership
    - **SharedPtr wenn nötig**: Nur bei geteilter Ownership
    - **WeakPtr für Caches**: Verhindere Zyklische Referenzen
    - **IntrusivePtr für Performance**: Wenn Effizienz kritisch ist

## RAII (Resource Acquisition Is Initialization)

RAII ist ein fundamentales C++ Pattern für Resource Management.

### Konzept

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
            fclose(file_);  // Automatisch geschlossen
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

### Verwendung

```cpp
void process_file(const char* filename) {
    FileHandle file(filename);  // Ressource erworben

    // Nutze Datei...
    char buffer[1024];
    fread(buffer, 1, sizeof(buffer), file.get());

    // ... auch bei frühem Return
    if (error_condition) {
        return;  // Datei wird automatisch geschlossen
    }

    // ... oder Exception
    if (critical_error) {
        throw std::runtime_error("Error");  // Datei wird geschlossen
    }

}  // Destruktor schließt Datei garantiert
```

### AdvLib RAII Helpers

```cpp
// Scoped Lock
{
    auto lock = make_scoped_lock(mutex);
    // Kritischer Bereich
}  // Automatisch entsperrt

// Scoped Timer
{
    auto timer = make_scoped_timer("Operation");
    expensive_operation();
}  // Zeit wird automatisch geloggt

// Scope Guard
{
    auto guard = make_scope_guard([]() {
        cleanup_resources();
    });

    do_risky_operation();

}  // cleanup_resources() wird garantiert aufgerufen
```

## Type Safety

AdvLib fördert Type Safety durch starke Typen.

### Strong Types

```cpp
// Schwach: Verwechslungsgefahr
void transfer(int from_account, int to_account, double amount);

// Stark: Keine Verwechslung möglich
struct AccountId { int value; };
struct Money { double amount; String currency; };

void transfer(AccountId from, AccountId to, Money amount);
```

### AdvLib Strong Types

```cpp
using UserId = StrongType<int, struct UserIdTag>;
using ProductId = StrongType<int, struct ProductIdTag>;

UserId user(42);
ProductId product(42);

// user = product;  // Compiler Fehler!
```

## Zusammenfassung

In diesem Tutorial hast du gelernt:

- **Namespaces**: Organisiere Code mit Namespaces
- **Result<T, E>**: Robustes Error Handling
- **Optional<T>**: Sichere optionale Werte
- **Smart Pointers**: Automatisches Memory Management
- **RAII**: Resource Management Pattern

## Übungen

1. Schreibe eine Funktion mit Result für sicheres File-Reading
2. Implementiere einen Cache mit Optional für Miss-Cases
3. Erstelle eine RAII-Klasse für einen Custom Resource-Typ
4. Refactore Code mit Raw Pointers zu Smart Pointers

## Nächste Schritte

- [First Application](beginner-first-app.md) - Wende das Gelernte an
- [Memory Management](intermediate-memory.md) - Vertiefe Memory-Konzepte
- [API Reference](../api-reference/core-classes.md) - Detaillierte Dokumentation
