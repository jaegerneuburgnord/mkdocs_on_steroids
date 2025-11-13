# Contributing Guide

Danke für dein Interesse, zur C++ Advanced Library beizutragen!

## Code of Conduct

Dieses Projekt folgt einem Code of Conduct. Durch Teilnahme akzeptierst du, respektvoll und konstruktiv zu sein.

## Wie kann ich beitragen?

Es gibt viele Wege beizutragen:

- 🐛 **Bug Reports**: Melde Bugs und Probleme
- 💡 **Feature Requests**: Schlage neue Features vor
- 📝 **Dokumentation**: Verbessere die Docs
- 🧪 **Tests**: Füge Tests hinzu
- 💻 **Code**: Implementiere Features oder Fixes
- 🌍 **Übersetzungen**: Übersetze Dokumentation

## Getting Started

### 1. Fork und Clone

```bash
# Fork das Repository auf GitHub
# Dann clone deinen Fork:
git clone https://github.com/YOUR_USERNAME/advlib.git
cd advlib
```

### 2. Development Environment Setup

```bash
# Installiere Dependencies
conan install . --build=missing

# Configure CMake
cmake -B build -DCMAKE_BUILD_TYPE=Debug \
    -DADVLIB_BUILD_TESTS=ON \
    -DADVLIB_BUILD_EXAMPLES=ON

# Build
cmake --build build -j$(nproc)
```

### 3. Run Tests

```bash
# Alle Tests ausführen
cd build
ctest --output-on-failure

# Spezifische Tests
./tests/core_tests
./tests/algorithms_tests
```

## Development Workflow

### 1. Erstelle einen Branch

```bash
git checkout -b feature/my-new-feature
# oder
git checkout -b bugfix/fix-issue-123
```

Branch-Naming Conventions:

- `feature/` - Neue Features
- `bugfix/` - Bug-Fixes
- `docs/` - Dokumentations-Änderungen
- `refactor/` - Code-Refactoring
- `perf/` - Performance-Verbesserungen
- `test/` - Test-Änderungen

### 2. Mache deine Änderungen

Befolge den [Code Style Guide](code-style.md):

```cpp
// Good
class MyClass {
public:
    void do_something() {
        // Implementation
    }

private:
    int member_variable_;
};

// Bad
class myClass {
public:
    void DoSomething() {
        // Implementation
    }

private:
    int memberVariable;
};
```

### 3. Schreibe Tests

Jede Änderung sollte Tests haben:

```cpp
#include <gtest/gtest.h>
#include <advlib/core/string.hpp>

TEST(StringTest, Concatenation) {
    advlib::String s1 = "Hello";
    advlib::String s2 = "World";
    advlib::String result = s1 + " " + s2;

    EXPECT_EQ(result, "Hello World");
}

TEST(StringTest, EmptyString) {
    advlib::String empty;
    EXPECT_TRUE(empty.empty());
    EXPECT_EQ(empty.length(), 0);
}
```

### 4. Update Dokumentation

Füge/Update Dokumentation:

```cpp
/**
 * @brief Calculate the square root of a number
 *
 * Computes the square root using Newton's method.
 *
 * @param x The input value (must be non-negative)
 * @return Result<double, Error> The square root on success
 *
 * @example
 * @code
 * auto result = safe_sqrt(16.0);
 * if (result.is_ok()) {
 *     std::cout << result.value() << std::endl;  // 4.0
 * }
 * @endcode
 *
 * @since 1.0.0
 */
Result<double, Error> safe_sqrt(double x);
```

### 5. Commit deine Änderungen

Commit Message Format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:

- `feat`: Neues Feature
- `fix`: Bug-Fix
- `docs`: Dokumentation
- `style`: Code-Style (keine Funktionsänderung)
- `refactor`: Code-Refactoring
- `perf`: Performance-Verbesserung
- `test`: Tests hinzufügen/ändern
- `chore`: Build, CI, Dependencies

Beispiele:

```bash
git commit -m "feat(core): add String::split() method"

git commit -m "fix(thread_pool): resolve race condition in task queue

The task queue had a race condition when multiple threads tried to
submit tasks simultaneously. This adds proper locking.

Fixes #123"

git commit -m "docs(tutorials): add concurrency tutorial"
```

### 6. Push und Pull Request

```bash
# Push zu deinem Fork
git push origin feature/my-new-feature

# Erstelle Pull Request auf GitHub
```

## Pull Request Guidelines

### PR Title Format

```
<type>: <description>
```

Beispiel:
```
feat: Add parallel sorting algorithm
fix: Resolve memory leak in thread pool
docs: Update installation guide
```

### PR Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature that changes existing functionality)
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review performed
- [ ] Commented complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing

## Related Issues
Closes #123
```

### Review Process

1. **Automated Checks**: CI muss grün sein
   - Compilation auf allen Plattformen
   - Alle Tests bestehen
   - Code-Style Check
   - Static Analysis

2. **Code Review**: Mindestens 1 Approval von Maintainer
   - Code-Qualität
   - Design-Entscheidungen
   - Test-Coverage
   - Dokumentation

3. **Merge**: Nach Approval wird gemerged

## Code Style

### Formatierung

Wir nutzen `clang-format`:

```bash
# Format alle Dateien
find src include -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
```

**`.clang-format`:**
```yaml
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
```

### Naming Conventions

```cpp
// Classes, Structs, Enums: PascalCase
class MyClass {};
struct MyStruct {};
enum class MyEnum {};

// Functions, Variables: snake_case
void my_function();
int my_variable;

// Member Variables: trailing underscore
class MyClass {
private:
    int member_variable_;
};

// Constants: kPascalCase
constexpr int kBufferSize = 1024;

// Macros: UPPER_CASE
#define ADVLIB_VERSION_MAJOR 1
```

### Best Practices

```cpp
// Use const correctness
void process_data(const Data& data);  // Good
void process_data(Data& data);        // Bad (if not modified)

// Use references over pointers when possible
void modify(MyClass& obj);            // Good
void modify(MyClass* obj);            // Bad (unless nullptr is valid)

// Use auto when type is obvious
auto value = compute_result();        // Good
ComplicatedType<T> value = compute(); // Bad

// Avoid naked pointers
auto ptr = std::make_unique<T>();     // Good
T* ptr = new T();                     // Bad
```

## Testing Guidelines

### Unit Tests

```cpp
// Test one thing per test
TEST(StringTest, LengthReturnsCorrectValue) {
    String s("hello");
    EXPECT_EQ(s.length(), 5);
}

// Use descriptive names
TEST(HttpClient, GetRequestReturns200OnSuccess) {
    // ...
}

// Test edge cases
TEST(VectorTest, EmptyVectorHasSizeZero) {
    Vector<int> v;
    EXPECT_EQ(v.size(), 0);
    EXPECT_TRUE(v.empty());
}
```

### Benchmarks

```cpp
// Performance-kritische Funktionen sollten Benchmarks haben
BENCHMARK(StringConcatenation) {
    String result;
    for (int i = 0; i < 1000; ++i) {
        result += "x";
    }
}

BENCHMARK(ParallelSort) {
    std::vector<int> data = generate_random_data(1000000);
    parallel_sort(data.begin(), data.end());
}
```

## Dokumentation

### Code-Dokumentation

Verwende Doxygen-Style:

```cpp
/**
 * @brief Short description
 *
 * Longer description with details
 *
 * @param param1 Description of parameter 1
 * @param param2 Description of parameter 2
 * @return Description of return value
 * @throws ExceptionType When and why
 *
 * @note Important notes
 * @warning Warnings
 * @see Related functions
 *
 * @example
 * @code
 * auto result = my_function(arg1, arg2);
 * @endcode
 */
ReturnType my_function(Type1 param1, Type2 param2);
```

### Markdown-Dokumentation

Füge Markdown-Docs in `docs/` hinzu:

```bash
docs/
├── tutorials/
│   └── my-new-tutorial.md
├── api-reference/
│   └── my-new-api.md
└── examples/
    └── my-example.md
```

Update Navigation in `mkdocs.yml`.

## Performance Considerations

- Profile vor Optimierung: `perf`, `valgrind`, `tracy`
- Benchmark-getriebene Entwicklung
- Zero-Cost Abstractions bevorzugen
- Vermeiden von unnötigen Kopien (Use Move Semantics)

## Security

### Reporting Security Issues

**NICHT** via Public Issue!

Kontaktiere: security@yourcompany.com

### Security Best Practices

- Keine Secrets im Code
- Input Validation
- Buffer Overflow Prevention
- Integer Overflow Checks

## Community

### Kommunikation

- **GitHub Discussions**: Allgemeine Diskussionen
- **Discord**: Real-time Chat
- **Issues**: Bug Reports und Feature Requests

### Getting Help

Fragen? Frag hier:

1. **Discord**: Schnelle Hilfe von Community
2. **GitHub Discussions**: Längere Diskussionen
3. **Stack Overflow**: Tag mit `advancedlib`

## Recognition

Contributors werden anerkannt:

- In [CONTRIBUTORS.md](../about/contributors.md)
- In Release Notes
- Auf der Website

## License

Durch Beiträge stimmst du zu, dass deine Beiträge unter der MIT License lizenziert werden.

---

**Danke für deinen Beitrag! 🎉**
