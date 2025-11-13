# Hello World Tutorial

Dein erstes Programm mit der C++ Advanced Library!

## Lernziele

Nach diesem Tutorial kannst du:

- [x] Ein AdvLib-Projekt erstellen
- [x] Header-Dateien korrekt einbinden
- [x] Basis-Funktionen verwenden
- [x] Das Projekt kompilieren und ausführen

**Geschätzte Zeit:** 10 Minuten

## Voraussetzungen

- AdvLib installiert (siehe [Installation](../getting-started/installation.md))
- C++ Compiler (GCC 10+, Clang 11+, oder MSVC 2019+)
- CMake 3.16+

## Schritt 1: Projekt erstellen

Erstelle ein neues Verzeichnis für dein Projekt:

```bash
mkdir hello-advlib
cd hello-advlib
```

## Schritt 2: CMakeLists.txt erstellen

Erstelle eine `CMakeLists.txt` Datei:

```cmake
cmake_minimum_required(VERSION 3.16)
project(HelloAdvLib VERSION 1.0.0)

# C++20 Standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Finde AdvLib
find_package(AdvancedLib REQUIRED COMPONENTS Core)

# Executable erstellen
add_executable(hello main.cpp)

# AdvLib linken
target_link_libraries(hello PRIVATE AdvancedLib::Core)
```

!!! info "Warum CMake?"
    CMake ist das bevorzugte Build-System für AdvLib und bietet plattformübergreifende Kompatibilität.

## Schritt 3: main.cpp erstellen

Erstelle `main.cpp` mit folgendem Inhalt:

```cpp
#include <advlib/core.hpp>
#include <iostream>

int main() {
    // Initialisiere Logging
    advlib::log::init(advlib::log::Level::Info);

    // Gib eine Nachricht aus
    advlib::log::info("Hello, AdvLib!");

    // Verwende String-Klasse
    advlib::String message = "Welcome to C++ Advanced Library";
    std::cout << message << std::endl;

    // Zeige Version
    std::cout << "AdvLib Version: "
              << ADVLIB_VERSION_MAJOR << "."
              << ADVLIB_VERSION_MINOR << "."
              << ADVLIB_VERSION_PATCH << std::endl;

    return 0;
}
```

### Code-Erklärung

#### Include Statement

```cpp
#include <advlib/core.hpp>
```

Dies ist der Hauptheader für AdvLib Core-Funktionalität. Er enthält:

- Logging-System
- String-Klassen
- Result und Optional Types
- Basis-Utilities

#### Logging initialisieren

```cpp
advlib::log::init(advlib::log::Level::Info);
```

Initialisiert das Logging-System mit Info-Level. Verfügbare Levels:

- `Trace`: Sehr detailliert
- `Debug`: Debug-Informationen
- `Info`: Allgemeine Informationen
- `Warn`: Warnungen
- `Error`: Fehler
- `Critical`: Kritische Fehler

#### Log-Ausgabe

```cpp
advlib::log::info("Hello, AdvLib!");
```

Gibt eine Info-Nachricht mit Timestamp aus.

#### String-Klasse

```cpp
advlib::String message = "Welcome to C++ Advanced Library";
```

AdvLib String ist eine verbesserte String-Implementierung mit:

- UTF-8 Support
- Optimierter Performance
- Reichem API

## Schritt 4: Kompilieren

Kompiliere das Projekt mit CMake:

=== "Linux/macOS"

    ```bash
    cmake -B build -DCMAKE_BUILD_TYPE=Release
    cmake --build build
    ```

=== "Windows"

    ```powershell
    cmake -B build -G "Visual Studio 17 2022"
    cmake --build build --config Release
    ```

!!! tip "Tipp"
    Verwende `-j$(nproc)` für parallele Kompilierung:
    ```bash
    cmake --build build -j$(nproc)
    ```

## Schritt 5: Ausführen

Führe dein Programm aus:

=== "Linux/macOS"

    ```bash
    ./build/hello
    ```

=== "Windows"

    ```powershell
    .\build\Release\hello.exe
    ```

### Erwartete Ausgabe

```
[2025-11-13 10:30:45.123] [INFO] Hello, AdvLib!
Welcome to C++ Advanced Library
AdvLib Version: 1.0.0
```

!!! success "Glückwunsch!"
    Du hast dein erstes AdvLib-Programm erfolgreich erstellt und ausgeführt!

## Übung: Erweitere das Programm

Versuche folgende Erweiterungen:

### Übung 1: Mehrere Log-Levels

```cpp
advlib::log::info("Info message");
advlib::log::warn("Warning message");
advlib::log::error("Error message");
```

### Übung 2: String-Operationen

```cpp
advlib::String name = "World";
advlib::String greeting = "Hello, " + name + "!";
std::cout << greeting << std::endl;
```

### Übung 3: String-Utilities

```cpp
#include <advlib/utilities/string.hpp>

advlib::String text = "  hello world  ";
auto upper = advlib::string_utils::to_upper(text);
auto trimmed = advlib::string_utils::trim(text);

std::cout << "Original: '" << text << "'" << std::endl;
std::cout << "Upper: '" << upper << "'" << std::endl;
std::cout << "Trimmed: '" << trimmed << "'" << std::endl;
```

## Erweiterte Version

Hier ist eine erweiterte Version mit mehr Features:

```cpp
#include <advlib/core.hpp>
#include <advlib/utilities/string.hpp>
#include <iostream>

using namespace advlib;

int main() {
    // Initialisiere Logging mit Custom Format
    log::init(log::Level::Info, "[{time}] [{level}] {message}");

    log::info("Starting Hello World Example");

    // String-Operationen
    String firstName = "John";
    String lastName = "Doe";
    String fullName = firstName + " " + lastName;

    log::info("User: {}", fullName);

    // String Utilities
    String email = "  JOHN.DOE@EXAMPLE.COM  ";
    auto cleanEmail = string_utils::to_lower(string_utils::trim(email));

    log::info("Clean email: {}", cleanEmail);

    // Result Type für Fehlerbehandlung
    auto parseResult = parse_number<int>("42");

    if (parseResult.is_ok()) {
        log::info("Parsed number: {}", parseResult.value());
    } else {
        log::error("Parse error: {}", parseResult.error());
    }

    // Optional Type
    Optional<int> maybeValue = Optional<int>(100);

    if (maybeValue.has_value()) {
        log::info("Optional value: {}", maybeValue.value());
    }

    log::info("Example completed successfully!");

    return 0;
}
```

## Häufige Probleme

### Header nicht gefunden

!!! failure "Problem"
    ```
    fatal error: advlib/core.hpp: No such file or directory
    ```

!!! success "Lösung"
    Stelle sicher, dass AdvLib korrekt installiert ist:
    ```bash
    find_package(AdvancedLib REQUIRED)
    ```

### Linker-Fehler

!!! failure "Problem"
    ```
    undefined reference to 'advlib::log::init'
    ```

!!! success "Lösung"
    Verlinke die Bibliothek korrekt:
    ```cmake
    target_link_libraries(hello PRIVATE AdvancedLib::Core)
    ```

### C++ Standard

!!! failure "Problem"
    ```
    error: 'concept' does not name a type
    ```

!!! success "Lösung"
    Setze C++20 Standard:
    ```cmake
    set(CMAKE_CXX_STANDARD 20)
    ```

## Zusammenfassung

In diesem Tutorial hast du gelernt:

- Ein AdvLib-Projekt mit CMake zu erstellen
- Den Core-Header einzubinden
- Das Logging-System zu verwenden
- String-Klassen zu nutzen
- Ein Programm zu kompilieren und auszuführen

## Nächste Schritte

- [Basic Concepts](beginner-concepts.md) - Lerne fundamentale Konzepte
- [First Application](beginner-first-app.md) - Erstelle eine vollständige App
- [API Reference](../api-reference/core-classes.md) - Detaillierte API-Dokumentation

!!! tip "Challenge"
    Versuche, ein Programm zu schreiben, das Benutzereingaben entgegennimmt und verarbeitet!
