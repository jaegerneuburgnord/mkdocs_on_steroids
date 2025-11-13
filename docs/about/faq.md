# Frequently Asked Questions (FAQ)

Häufig gestellte Fragen zur C++ Advanced Library.

## Allgemein

### Was ist die C++ Advanced Library?

Die C++ Advanced Library (AdvLib) ist eine moderne, hochperformante C++ Bibliothek, die moderne C++17/20 Features nutzt, um Entwicklern leistungsstarke Werkzeuge für alltägliche und komplexe Programmieraufgaben bereitzustellen.

### Welche C++ Standards werden unterstützt?

AdvLib benötigt mindestens **C++17**. Volle Funktionalität mit **C++20** Features wie Concepts und Coroutines.

### Welche Compiler werden unterstützt?

- **GCC** 10.0 oder höher
- **Clang** 11.0 oder höher
- **MSVC** 19.28 (Visual Studio 2019 16.8) oder höher

### Ist AdvLib kostenlos?

Ja! AdvLib ist Open Source unter der MIT License und kann kostenlos in kommerziellen und privaten Projekten genutzt werden.

## Installation & Setup

### Wie installiere ich AdvLib?

Es gibt mehrere Methoden:

1. **Package Manager** (empfohlen):
   ```bash
   conan install advancedlib/1.0.0@
   # oder
   vcpkg install advancedlib
   ```

2. **Aus Quellcode**:
   ```bash
   git clone https://github.com/youruser/advlib.git
   cd advlib
   cmake -B build -DCMAKE_BUILD_TYPE=Release
   cmake --build build
   sudo cmake --install build
   ```

Siehe [Installation Guide](../getting-started/installation.md) für Details.

### Wie integriere ich AdvLib in mein CMake Projekt?

```cmake
find_package(AdvancedLib REQUIRED)
target_link_libraries(my_app PRIVATE AdvancedLib::Core)
```

Siehe [Build System Integration](../getting-started/build-system.md).

### Warum findet CMake AdvLib nicht?

Setze `CMAKE_PREFIX_PATH`:

```bash
cmake -DCMAKE_PREFIX_PATH=/usr/local/lib/cmake/AdvancedLib
```

## Features & Funktionalität

### Unterstützt AdvLib Multithreading?

Ja! AdvLib bietet:

- Thread Pools
- Async/Await mit Coroutines
- Lock-Free Data Structures
- Parallele Algorithmen

Siehe [Concurrency Tutorial](../tutorials/advanced-concurrency.md).

### Gibt es Networking-Support?

Ja! Das Networking-Modul bietet:

- HTTP Client/Server
- WebSocket Support
- Async IO

Siehe [Networking Examples](../examples/advanced-examples.md).

### Kann ich eigene Allocators verwenden?

Ja! AdvLib unterstützt Custom Allocators:

```cpp
PoolAllocator<int> alloc(1024);
Vector<int> vec(alloc);
```

Siehe [Memory Management Tutorial](../tutorials/intermediate-memory.md).

### Wirft AdvLib Exceptions?

Standardmäßig nutzt AdvLib `Result<T, E>` für Fehlerbehandlung statt Exceptions. Exceptions können optional aktiviert werden.

```cpp
Result<int, Error> divide(int a, int b);  // Keine Exceptions

// Pattern:
auto result = divide(10, 2);
if (result.is_ok()) {
    // Success
} else {
    // Handle error
}
```

## Performance

### Wie schnell ist AdvLib?

AdvLib nutzt Zero-Cost Abstractions. In Benchmarks:

- String-Operationen: Gleichauf oder schneller als std::string
- Container: Bis zu 30% schneller als STL
- Parallele Algorithmen: Near-linear Speedup auf Multi-Core

### Gibt es Performance-Overhead?

Nein! Durch Template-Metaprogramming und Inline-Functions entsteht kein Runtime-Overhead im Vergleich zu handgeschriebenem Code.

### Sollte ich Release-Builds verwenden?

Ja! Für Production immer Release-Builds:

```bash
cmake -DCMAKE_BUILD_TYPE=Release
```

Debug-Builds haben zusätzliche Checks und sind langsamer.

## Compatibility

### Ist AdvLib plattformübergreifend?

Ja! Unterstützte Plattformen:

- Linux (Ubuntu, Debian, Fedora, Arch)
- Windows 10/11
- macOS 11+
- Embedded Systems (ARM, RISC-V)

### Funktioniert AdvLib mit anderen Libraries?

Ja! AdvLib ist designed, um mit der STL und anderen Libraries zu kooperieren:

```cpp
// STL <-> AdvLib
std::vector<int> std_vec = {1, 2, 3};
advlib::Vector<int> adv_vec(std_vec.begin(), std_vec.end());
```

### Kann ich AdvLib mit C++11/14 verwenden?

Nein, AdvLib benötigt mindestens C++17 für Features wie:

- `if constexpr`
- Structured Bindings
- `std::optional` Integration

## Development

### Wie kann ich zu AdvLib beitragen?

1. Fork das Repository
2. Erstelle einen Feature Branch
3. Implementiere deine Änderungen mit Tests
4. Erstelle einen Pull Request

Siehe [Contributing Guide](../development/contributing.md).

### Wo melde ich Bugs?

Erstelle ein [GitHub Issue](https://github.com/youruser/advlib/issues) mit:

- Beschreibung des Problems
- Minimales reproduzierbares Beispiel
- Compiler & OS Version
- AdvLib Version

### Gibt es einen Code Style Guide?

Ja! Siehe [Code Style Guide](../development/code-style.md).

Kurz:

- Klassen: `PascalCase`
- Funktionen: `snake_case`
- Konstanten: `kPascalCase`
- Makros: `UPPER_CASE`

## Learning & Support

### Wo finde ich Tutorials?

Starte mit:

1. [Getting Started](../getting-started/index.md)
2. [Beginner Tutorials](../tutorials/index.md)
3. [Examples](../examples/index.md)

### Gibt es eine Community?

Ja!

- **Discord**: [Community Server](https://discord.gg/advlib)
- **Forum**: [Discussions](https://github.com/youruser/advlib/discussions)
- **Stack Overflow**: Tag mit `advancedlib`

### Wo finde ich API-Dokumentation?

Die vollständige API-Referenz ist hier: [API Reference](../api-reference/index.md)

### Gibt es Video-Tutorials?

Ja! Siehe [YouTube Playlist](https://youtube.com/advlib).

## Licensing

### Kann ich AdvLib kommerziell nutzen?

Ja! Die MIT License erlaubt kommerzielle Nutzung ohne Einschränkungen.

### Muss ich meinen Code Open Source machen?

Nein! Du musst nur die AdvLib License-Notice beibehalten.

### Kann ich AdvLib modifizieren?

Ja! Du kannst AdvLib nach Belieben modifizieren.

## Troubleshooting

### Linker-Fehler: undefined reference

Stelle sicher, dass du die Bibliothek linkst:

```cmake
target_link_libraries(my_app PRIVATE AdvancedLib::Core)
```

Oder manuell:

```bash
g++ main.cpp -ladvancedlib -pthread
```

### Compiler-Fehler: concept not found

Dein Compiler unterstützt C++20 nicht vollständig. Upgrade auf:

- GCC 10+
- Clang 11+
- MSVC 19.28+

### Runtime-Fehler: Segmentation Fault

Häufige Ursachen:

1. **Dangling References**: Lifetime-Issues mit Result/Optional
2. **Thread Safety**: Unsynchronisierter Zugriff auf shared state
3. **Memory Corruption**: Buffer Overflows

Nutze Address Sanitizer zum Debuggen:

```bash
cmake -DCMAKE_CXX_FLAGS="-fsanitize=address"
```

## Migration

### Wie migriere ich von std::string zu advlib::String?

```cpp
// Vorher
std::string str = "hello";

// Nachher
advlib::String str = "hello";

// Oder schrittweise:
advlib::String adv_str(std_string);  // Conversion
```

### Wie migriere ich von Exceptions zu Result?

```cpp
// Vorher
try {
    int result = risky_operation();
} catch (const std::exception& e) {
    // Handle error
}

// Nachher
auto result = risky_operation();  // Returns Result<int, Error>
if (result.is_ok()) {
    int value = result.value();
} else {
    // Handle error
}
```

## Weitere Fragen?

Deine Frage ist nicht dabei?

- Stelle sie im [Forum](https://github.com/youruser/advlib/discussions)
- Tritt dem [Discord](https://discord.gg/advlib) bei
- Erstelle ein [Issue](https://github.com/youruser/advlib/issues)

Wir helfen gerne! 😊
