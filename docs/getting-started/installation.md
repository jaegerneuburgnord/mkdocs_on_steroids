# Installation

Diese Seite beschreibt verschiedene Methoden zur Installation der C++ Advanced Library.

## Methode 1: Package Manager (Empfohlen)

### Conan

Der einfachste Weg ist die Verwendung von Conan:

```bash
# Füge das Remote Repository hinzu
conan remote add advlib https://conan.advlib.io

# Installiere die Bibliothek
conan install advancedlib/1.0.0@
```

**conanfile.txt:**

```ini
[requires]
advancedlib/1.0.0

[generators]
CMakeDeps
CMakeToolchain

[options]
advancedlib:shared=True
advancedlib:with_networking=True
advancedlib:with_simd=True
```

### vcpkg

Für vcpkg Benutzer:

```bash
# Installiere vcpkg (falls noch nicht geschehen)
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh  # Linux/macOS
# oder
.\bootstrap-vcpkg.bat  # Windows

# Installiere die Bibliothek
./vcpkg install advancedlib
```

**Integriere vcpkg in CMake:**

```bash
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake
```

## Methode 2: Aus Quellcode bauen

### Repository klonen

```bash
git clone https://github.com/youruser/cpp-advanced-library.git
cd cpp-advanced-library
git checkout v1.0.0  # Oder gewünschte Version
```

### Build mit CMake

=== "Linux/macOS"

    ```bash
    # Debug Build
    cmake -B build -DCMAKE_BUILD_TYPE=Debug
    cmake --build build

    # Release Build
    cmake -B build-release -DCMAKE_BUILD_TYPE=Release
    cmake --build build-release

    # Installation
    sudo cmake --install build-release
    ```

=== "Windows"

    ```powershell
    # Visual Studio 2022
    cmake -B build -G "Visual Studio 17 2022" -A x64
    cmake --build build --config Release

    # Installation (als Administrator)
    cmake --install build --config Release
    ```

=== "Mit Ninja"

    ```bash
    # Schnellerer Build mit Ninja
    cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
    ninja -C build

    # Installation
    sudo ninja -C build install
    ```

### Build-Optionen

Konfiguriere den Build mit folgenden CMake-Optionen:

```bash
cmake -B build \
    -DADVLIB_BUILD_TESTS=ON \           # Build Tests
    -DADVLIB_BUILD_EXAMPLES=ON \        # Build Beispiele
    -DADVLIB_BUILD_DOCS=ON \            # Build Dokumentation
    -DADVLIB_ENABLE_SIMD=ON \           # SIMD Optimierungen
    -DADVLIB_ENABLE_NETWORKING=ON \     # Networking Module
    -DADVLIB_ENABLE_ASYNC=ON \          # Async/Await Support
    -DADVLIB_USE_SANITIZERS=OFF \       # Address/UB Sanitizers
    -DCMAKE_CXX_STANDARD=20             # C++ Standard (17 oder 20)
```

## Methode 3: System Package Manager

### Ubuntu/Debian

```bash
# Füge PPA hinzu
sudo add-apt-repository ppa:advlib/stable
sudo apt update

# Installiere
sudo apt install libadvancedlib-dev
```

### Fedora

```bash
sudo dnf install advancedlib-devel
```

### Arch Linux

```bash
yay -S advancedlib  # oder dein AUR helper
```

### macOS (Homebrew)

```bash
brew tap advlib/tap
brew install advancedlib
```

## Verifizierung der Installation

Erstelle eine Testdatei `test.cpp`:

```cpp
#include <advlib/core.hpp>
#include <iostream>

int main() {
    std::cout << "AdvLib Version: "
              << ADVLIB_VERSION_MAJOR << "."
              << ADVLIB_VERSION_MINOR << "."
              << ADVLIB_VERSION_PATCH << std::endl;

    advlib::log::info("Installation successful!");
    return 0;
}
```

Kompiliere und führe aus:

=== "Mit CMake"

    **CMakeLists.txt:**
    ```cmake
    cmake_minimum_required(VERSION 3.16)
    project(TestAdvLib)

    set(CMAKE_CXX_STANDARD 20)

    find_package(AdvancedLib REQUIRED)

    add_executable(test test.cpp)
    target_link_libraries(test PRIVATE AdvancedLib::Core)
    ```

    ```bash
    cmake -B build
    cmake --build build
    ./build/test
    ```

=== "Direkt"

    ```bash
    # Linux/macOS
    g++ -std=c++20 test.cpp -ladvancedlib -o test
    ./test

    # Windows (MSVC)
    cl /std:c++20 /EHsc test.cpp advancedlib.lib
    test.exe
    ```

Erwartete Ausgabe:

```
AdvLib Version: 1.0.0
[INFO] Installation successful!
```

## Fehlerbehebung

### Compiler findet Header nicht

!!! failure "Problem"
    ```
    fatal error: advlib/core.hpp: No such file or directory
    ```

!!! success "Lösung"
    Stelle sicher, dass der Include-Pfad korrekt ist:

    ```bash
    g++ -std=c++20 -I/usr/local/include test.cpp -ladvancedlib
    ```

### Linker-Fehler

!!! failure "Problem"
    ```
    undefined reference to 'advlib::...'
    ```

!!! success "Lösung"
    Füge die Bibliothek zum Linker hinzu:

    ```bash
    g++ test.cpp -L/usr/local/lib -ladvancedlib -pthread
    ```

### Version-Mismatch

!!! failure "Problem"
    ```
    Version mismatch: expected 1.0.0, found 0.9.0
    ```

!!! success "Lösung"
    Aktualisiere die Bibliothek oder passe deine Anforderungen an:

    ```bash
    conan install advancedlib/1.0.0@ --update
    ```

## Nächste Schritte

Jetzt, wo die Bibliothek installiert ist, kannst du mit dem [Quick Start](quickstart.md) fortfahren!

## Erweiterte Installation

Für erweiterte Installationsoptionen siehe:

- [Build System Integration](build-system.md)
- [Dependency Management](dependencies.md)
- [Development Setup](../development/contributing.md)
