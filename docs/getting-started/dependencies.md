# Dependencies Management

Lerne, wie du Abhängigkeiten für die C++ Advanced Library verwaltest.

## Übersicht der Abhängigkeiten

AdvLib hat minimale externe Abhängigkeiten für maximale Portabilität:

### Erforderliche Dependencies

| Dependency | Version | Zweck |
|------------|---------|-------|
| C++ Compiler | C++17+ | Kernfunktionalität |
| CMake | 3.16+ | Build-System |

### Optionale Dependencies

| Dependency | Version | Zweck | CMake Option |
|------------|---------|-------|--------------|
| Boost | 1.75+ | Extended Utilities | `ADVLIB_USE_BOOST` |
| OpenSSL | 1.1.1+ | SSL/TLS Support | `ADVLIB_ENABLE_SSL` |
| libcurl | 7.68+ | HTTP Client | `ADVLIB_ENABLE_NETWORKING` |
| zlib | 1.2.11+ | Kompression | `ADVLIB_ENABLE_COMPRESSION` |
| fmt | 8.0+ | String Formatting | `ADVLIB_USE_FMT` |
| spdlog | 1.9+ | Advanced Logging | `ADVLIB_USE_SPDLOG` |

## Conan Integration

### conanfile.txt

```ini
[requires]
advancedlib/1.0.0

# Optionale Dependencies
boost/1.79.0
openssl/1.1.1q
libcurl/7.84.0
zlib/1.2.12
fmt/9.0.0
spdlog/1.10.0

[generators]
CMakeDeps
CMakeToolchain

[options]
# AdvLib Optionen
advancedlib:shared=True
advancedlib:with_networking=True
advancedlib:with_ssl=True
advancedlib:with_compression=True

# Dependency Optionen
boost:shared=False
openssl:shared=True
```

### conanfile.py

Für fortgeschrittene Setups:

```python
from conan import ConanFile
from conan.tools.cmake import cmake_layout

class MyAdvLibProject(ConanFile):
    name = "my_advlib_project"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    requires = [
        "advancedlib/1.0.0",
        "boost/1.79.0",
        "openssl/1.1.1q",
    ]

    default_options = {
        "advancedlib:shared": True,
        "advancedlib:with_networking": True,
        "boost:shared": False,
    }

    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        if self.options["advancedlib"].with_networking:
            self.requires("libcurl/7.84.0")

        if self.settings.os == "Linux":
            self.requires("libuuid/1.0.3")
```

Installation:

```bash
conan install . --build=missing
cmake --preset conan-release
cmake --build --preset conan-release
```

## vcpkg Integration

### vcpkg.json

```json
{
    "name": "my-advlib-project",
    "version": "1.0.0",
    "dependencies": [
        "advancedlib",
        {
            "name": "boost",
            "features": ["system", "thread", "filesystem"]
        },
        "openssl",
        "curl",
        "zlib",
        "fmt",
        "spdlog"
    ],
    "builtin-baseline": "2023-05-01"
}
```

### Manifest Mode

Mit vcpkg manifest mode:

```bash
vcpkg install
cmake -B build -S . \
    -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake
cmake --build build
```

## CMake FetchContent

Für Header-Only Dependencies:

```cmake
include(FetchContent)

# fmt Library
FetchContent_Declare(
    fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG 9.0.0
)

# spdlog Library
FetchContent_Declare(
    spdlog
    GIT_REPOSITORY https://github.com/gabime/spdlog.git
    GIT_TAG v1.10.0
)

FetchContent_MakeAvailable(fmt spdlog)

target_link_libraries(my_app
    PRIVATE
        AdvancedLib::Core
        fmt::fmt
        spdlog::spdlog
)
```

## Git Submodules

Für Dependencies als Submodules:

```bash
# Füge Dependencies hinzu
git submodule add https://github.com/fmtlib/fmt.git external/fmt
git submodule add https://github.com/gabime/spdlog.git external/spdlog

# Initialisiere Submodules
git submodule update --init --recursive
```

**CMakeLists.txt:**

```cmake
# Füge Submodule hinzu
add_subdirectory(external/fmt)
add_subdirectory(external/spdlog)

target_link_libraries(my_app
    PRIVATE
        AdvancedLib::Core
        fmt::fmt
        spdlog::spdlog
)
```

## System Package Manager

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install \
    libboost-all-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    zlib1g-dev \
    libfmt-dev \
    libspdlog-dev
```

### Fedora

```bash
sudo dnf install \
    boost-devel \
    openssl-devel \
    libcurl-devel \
    zlib-devel \
    fmt-devel \
    spdlog-devel
```

### macOS (Homebrew)

```bash
brew install \
    boost \
    openssl \
    curl \
    zlib \
    fmt \
    spdlog
```

### Windows (vcpkg)

```powershell
vcpkg install boost:x64-windows openssl:x64-windows curl:x64-windows
```

## Dependency Isolation

### Docker Container

**Dockerfile:**

```dockerfile
FROM ubuntu:22.04

# System Dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libboost-all-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/*

# AdvLib installieren
RUN git clone https://github.com/youruser/advlib.git && \
    cd advlib && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build

WORKDIR /workspace
```

Build und Run:

```bash
docker build -t advlib-dev .
docker run -v $(pwd):/workspace -it advlib-dev
```

### Nix

**shell.nix:**

```nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    cmake
    ninja
    gcc
    boost
    openssl
    curl
    zlib
    fmt
    spdlog
  ];

  shellHook = ''
    export CMAKE_PREFIX_PATH="${pkgs.boost}/lib/cmake:$CMAKE_PREFIX_PATH"
  '';
}
```

Verwendung:

```bash
nix-shell
```

## Version Management

### Version Constraints in CMake

```cmake
find_package(AdvancedLib 1.0 REQUIRED)  # Mindestens 1.0
find_package(AdvancedLib 1.0 EXACT REQUIRED)  # Exakt 1.0
find_package(Boost 1.75...<1.80 REQUIRED)  # Bereich
```

### Conan Version Ranges

```ini
[requires]
advancedlib/[>=1.0.0 <2.0.0]
boost/[>=1.75.0]
```

### vcpkg Version Constraints

```json
{
    "dependencies": [
        {
            "name": "advancedlib",
            "version>=": "1.0.0"
        }
    ]
}
```

## Transitive Dependencies

AdvLib handhabt transitive Dependencies automatisch:

```cmake
find_package(AdvancedLib REQUIRED)

# Transitive Dependencies werden automatisch eingebunden
target_link_libraries(my_app PRIVATE AdvancedLib::Core)
```

Manuelle Kontrolle:

```cmake
# Zeige alle transitiven Dependencies
get_target_property(DEPS AdvancedLib::Core INTERFACE_LINK_LIBRARIES)
message(STATUS "AdvLib Dependencies: ${DEPS}")

# Deaktiviere transitive Dependencies
set_target_properties(AdvancedLib::Core PROPERTIES
    INTERFACE_LINK_LIBRARIES ""
)
```

## Dependency Graph

Visualisiere Dependencies mit CMake:

```bash
# Generiere Dependency Graph
cmake --graphviz=deps.dot build
dot -Tpng deps.dot -o deps.png
```

Mit Conan:

```bash
conan graph info . --format=html > graph.html
```

## Build From Source

Falls du Dependencies selbst bauen musst:

**build_deps.sh:**

```bash
#!/bin/bash
set -e

INSTALL_PREFIX="${HOME}/local"
BUILD_DIR="build_deps"

mkdir -p $BUILD_DIR
cd $BUILD_DIR

# Boost
wget https://boostorg.jfrog.io/artifactory/main/release/1.79.0/source/boost_1_79_0.tar.gz
tar xzf boost_1_79_0.tar.gz
cd boost_1_79_0
./bootstrap.sh --prefix=$INSTALL_PREFIX
./b2 install -j$(nproc)
cd ..

# fmt
git clone --depth 1 --branch 9.0.0 https://github.com/fmtlib/fmt.git
cd fmt
cmake -B build -DCMAKE_INSTALL_PREFIX=$INSTALL_PREFIX
cmake --build build -j$(nproc)
cmake --install build
cd ..

echo "Dependencies installed to: $INSTALL_PREFIX"
```

Verwendung:

```bash
chmod +x build_deps.sh
./build_deps.sh

# CMake mit custom prefix
cmake -B build -DCMAKE_PREFIX_PATH=$HOME/local
```

## Konfliktauflösung

### Version Konflikte

```cmake
# Erzwinge spezifische Version
find_package(Boost 1.79.0 EXACT REQUIRED)

# Oder bevorzuge neuere Versionen
find_package(Boost 1.75 REQUIRED)
if(Boost_VERSION VERSION_LESS 1.79.0)
    message(WARNING "Boost version ${Boost_VERSION} is old, consider upgrading")
endif()
```

### ABI Kompatibilität

```cmake
# Prüfe C++ Standard
if(CMAKE_CXX_STANDARD LESS 17)
    message(FATAL_ERROR "AdvLib requires C++17 or later")
endif()

# Prüfe Compiler
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" AND CMAKE_CXX_COMPILER_VERSION VERSION_LESS 10.0)
    message(FATAL_ERROR "GCC 10.0+ required")
endif()
```

## Best Practices

1. **Pin Versions**: Nutze spezifische Versionen in Production
2. **Lock Files**: Verwende Lock-Files (conan.lock, vcpkg.lock)
3. **Vendor Critical Deps**: Vendore kritische Dependencies als Fallback
4. **Test Upgrades**: Teste Dependency-Updates in CI
5. **Document Dependencies**: Halte README aktuell

## Troubleshooting

### Dependency nicht gefunden

```bash
# CMake Debug Output
cmake -B build --debug-find-pkg=AdvancedLib

# Überprüfe CMAKE_PREFIX_PATH
cmake -B build -DCMAKE_PREFIX_PATH=/usr/local
```

### Version Mismatch

```bash
# Zeige installierte Versionen
conan search advancedlib
vcpkg list

# Update Dependencies
conan install . --update
vcpkg upgrade
```

### Linker Errors

```cmake
# Verbose Linker Output
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--verbose")

# Zeige Link Libraries
get_target_property(LINK_LIBS my_app LINK_LIBRARIES)
message(STATUS "Link libraries: ${LINK_LIBS}")
```

## Weitere Ressourcen

- [Build System Integration](build-system.md)
- [Development Guide](../development/contributing.md)
- [Conan Documentation](https://docs.conan.io/)
- [vcpkg Documentation](https://vcpkg.io/)
