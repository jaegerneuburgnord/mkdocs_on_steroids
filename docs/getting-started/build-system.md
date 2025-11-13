# Build System Integration

Dieser Guide zeigt, wie du die C++ Advanced Library in verschiedene Build-Systeme integrieren kannst.

## CMake (Empfohlen)

CMake ist das native Build-System für AdvLib und bietet die beste Integration.

### Basis-Integration

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyProject)

set(CMAKE_CXX_STANDARD 20)

# Finde AdvLib
find_package(AdvancedLib 1.0 REQUIRED)

add_executable(my_app main.cpp)
target_link_libraries(my_app PRIVATE AdvancedLib::Core)
```

### Mit spezifischen Komponenten

```cmake
find_package(AdvancedLib REQUIRED
    COMPONENTS
        Core
        Algorithms
        Networking
        Utilities
)

target_link_libraries(my_app
    PRIVATE
        AdvancedLib::Core
        AdvancedLib::Algorithms
        AdvancedLib::Networking
        AdvancedLib::Utilities
)
```

### FetchContent (Header-Only)

Für Header-Only Komponenten:

```cmake
include(FetchContent)

FetchContent_Declare(
    AdvancedLib
    GIT_REPOSITORY https://github.com/youruser/advlib.git
    GIT_TAG v1.0.0
)

FetchContent_MakeAvailable(AdvancedLib)

target_link_libraries(my_app PRIVATE AdvancedLib::Core)
```

### ExternalProject

Für komplexere Setups:

```cmake
include(ExternalProject)

ExternalProject_Add(
    AdvancedLib
    GIT_REPOSITORY https://github.com/youruser/advlib.git
    GIT_TAG v1.0.0
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/external
        -DCMAKE_BUILD_TYPE=Release
        -DADVLIB_BUILD_TESTS=OFF
)

# Verwende die installierte Library
link_directories(${CMAKE_BINARY_DIR}/external/lib)
include_directories(${CMAKE_BINARY_DIR}/external/include)
```

### CMake Presets

Erstelle `CMakePresets.json`:

```json
{
    "version": 3,
    "cmakeMinimumRequired": {
        "major": 3,
        "minor": 21,
        "patch": 0
    },
    "configurePresets": [
        {
            "name": "default",
            "hidden": true,
            "generator": "Ninja",
            "binaryDir": "${sourceDir}/build/${presetName}",
            "cacheVariables": {
                "CMAKE_CXX_STANDARD": "20"
            }
        },
        {
            "name": "debug",
            "inherits": "default",
            "displayName": "Debug",
            "cacheVariables": {
                "CMAKE_BUILD_TYPE": "Debug",
                "ADVLIB_ENABLE_SANITIZERS": "ON"
            }
        },
        {
            "name": "release",
            "inherits": "default",
            "displayName": "Release",
            "cacheVariables": {
                "CMAKE_BUILD_TYPE": "Release",
                "ADVLIB_ENABLE_SIMD": "ON"
            }
        }
    ],
    "buildPresets": [
        {
            "name": "debug",
            "configurePreset": "debug"
        },
        {
            "name": "release",
            "configurePreset": "release"
        }
    ]
}
```

Verwendung:

```bash
cmake --preset=release
cmake --build --preset=release
```

## Meson

Integration mit Meson Build-System:

**meson.build:**

```meson
project('my_advlib_project', 'cpp',
    version: '1.0.0',
    default_options: ['cpp_std=c++20']
)

# Abhängigkeit deklarieren
advlib_dep = dependency('advancedlib', version: '>=1.0.0')

# Executable
executable('my_app',
    'main.cpp',
    dependencies: advlib_dep
)
```

Build:

```bash
meson setup build
meson compile -C build
```

## Bazel

**WORKSPACE:**

```python
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "advancedlib",
    remote = "https://github.com/youruser/advlib.git",
    tag = "v1.0.0",
)
```

**BUILD:**

```python
cc_binary(
    name = "my_app",
    srcs = ["main.cpp"],
    deps = [
        "@advancedlib//advlib:core",
        "@advancedlib//advlib:algorithms",
    ],
)
```

Build:

```bash
bazel build //:my_app
```

## Make

Für traditionelle Makefiles:

**Makefile:**

```makefile
CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -O3
INCLUDES = -I/usr/local/include
LDFLAGS = -L/usr/local/lib
LIBS = -ladvancedlib -pthread

SOURCES = main.cpp utils.cpp
OBJECTS = $(SOURCES:.cpp=.o)
TARGET = my_app

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all clean
```

Build:

```bash
make -j$(nproc)
```

## xmake

**xmake.lua:**

```lua
add_rules("mode.debug", "mode.release")

set_languages("cxx20")

add_requires("advancedlib")

target("my_app")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("advancedlib")
```

Build:

```bash
xmake
xmake run my_app
```

## Premake

**premake5.lua:**

```lua
workspace "MyAdvLibProject"
    configurations { "Debug", "Release" }

project "my_app"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++20"

    files { "src/**.cpp", "src/**.h" }

    includedirs { "/usr/local/include" }
    libdirs { "/usr/local/lib" }
    links { "advancedlib", "pthread" }

    filter "configurations:Debug"
        defines { "DEBUG" }
        symbols "On"

    filter "configurations:Release"
        defines { "NDEBUG" }
        optimize "On"
```

Build:

```bash
premake5 gmake2
make config=release
```

## Visual Studio (MSBuild)

Für Visual Studio Projekte:

1. Öffne Projekt-Eigenschaften
2. Navigiere zu **C/C++** → **General** → **Additional Include Directories**
3. Füge hinzu: `C:\Program Files\AdvancedLib\include`
4. Navigiere zu **Linker** → **General** → **Additional Library Directories**
5. Füge hinzu: `C:\Program Files\AdvancedLib\lib`
6. Navigiere zu **Linker** → **Input** → **Additional Dependencies**
7. Füge hinzu: `advancedlib.lib`

## Compiler-spezifische Flags

### GCC

```bash
g++ -std=c++20 -O3 -march=native -flto \
    -Wall -Wextra -Wpedantic \
    -I/usr/local/include \
    -L/usr/local/lib \
    main.cpp -ladvancedlib -pthread \
    -o my_app
```

### Clang

```bash
clang++ -std=c++20 -O3 -march=native -flto \
    -Wall -Wextra -Wpedantic \
    -I/usr/local/include \
    -L/usr/local/lib \
    main.cpp -ladvancedlib -pthread \
    -o my_app
```

### MSVC

```cmd
cl /std:c++20 /O2 /EHsc /W4 ^
   /I"C:\Program Files\AdvancedLib\include" ^
   main.cpp ^
   /link /LIBPATH:"C:\Program Files\AdvancedLib\lib" advancedlib.lib
```

## Package Config

AdvLib installiert eine `.pc` Datei für pkg-config:

```bash
pkg-config --cflags advancedlib
pkg-config --libs advancedlib

# In Makefile
CXXFLAGS += $(shell pkg-config --cflags advancedlib)
LDFLAGS += $(shell pkg-config --libs advancedlib)
```

## Cross-Compilation

### Für ARM (Raspberry Pi)

**toolchain-arm.cmake:**

```cmake
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(CMAKE_C_COMPILER arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER arm-linux-gnueabihf-g++)

set(CMAKE_FIND_ROOT_PATH /usr/arm-linux-gnueabihf)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
```

Build:

```bash
cmake -B build-arm -DCMAKE_TOOLCHAIN_FILE=toolchain-arm.cmake
cmake --build build-arm
```

### Für Windows von Linux

```bash
x86_64-w64-mingw32-g++ -std=c++20 \
    main.cpp -ladvancedlib \
    -o my_app.exe
```

## Build-Optimierungen

### Link-Time Optimization (LTO)

```cmake
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
```

### Unity Builds

```cmake
set(CMAKE_UNITY_BUILD ON)
set(CMAKE_UNITY_BUILD_BATCH_SIZE 16)
```

### Precompiled Headers

```cmake
target_precompile_headers(my_app
    PRIVATE
        <advlib/core.hpp>
        <vector>
        <string>
)
```

### Ccache Integration

```cmake
find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
    set(CMAKE_CXX_COMPILER_LAUNCHER "${CCACHE_PROGRAM}")
endif()
```

## Fehlerbehebung

### CMake findet AdvLib nicht

```bash
# Setze CMAKE_PREFIX_PATH
cmake -DCMAKE_PREFIX_PATH=/usr/local/lib/cmake/AdvancedLib
```

### Linker-Fehler

```cmake
# Explizite Link-Abhängigkeiten
target_link_libraries(my_app
    PRIVATE
        AdvancedLib::Core
        pthread
        dl
)
```

## Weitere Ressourcen

- [CMake Dokumentation](https://cmake.org/documentation/)
- [Dependencies](dependencies.md)
- [Development Setup](../development/contributing.md)
