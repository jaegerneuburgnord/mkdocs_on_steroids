# libtorrent::aux::container_wrapper API Documentation

## Overview
The `container_wrapper` class template provides a safe, indexed container interface that wraps a base container type, enforcing bounds checking and type safety. It's designed to work with integer index types that may be smaller than the container's natural size type, ensuring that all operations respect the container's logical bounds.

## Function Reference

### container_wrapper

- **Signature**: `container_wrapper()`
- **Description**: Default constructor that creates an empty container wrapper.
- **Parameters**: None
- **Return Value**: A newly constructed `container_wrapper` instance
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto container = container_wrapper<int>();
```
- **Preconditions**: None
- **Postconditions**: The container is empty and ready for use
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `container_wrapper(Base&& b)`, `container_wrapper(IndexType const s)`

### container_wrapper

- **Signature**: `container_wrapper(Base&& b)`
- **Description**: Move constructor that wraps an existing container by moving it into the wrapper.
- **Parameters**:
  - `b` (Base&&): The container to wrap, will be moved into the wrapper
- **Return Value**: A newly constructed `container_wrapper` instance
- **Exceptions/Errors**: None
- **Example**:
```cpp
std::vector<int> vec = {1, 2, 3};
auto container = container_wrapper<int>(std::move(vec));
```
- **Preconditions**: The container must be valid
- **Postconditions**: The wrapped container is moved into the wrapper, and the original container is left in a valid but unspecified state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `container_wrapper()`, `container_wrapper(IndexType const s)`

### container_wrapper

- **Signature**: `container_wrapper(IndexType const s)`
- **Description**: Constructor that creates a container with the specified size.
- **Parameters**:
  - `s` (IndexType const): The initial size of the container
- **Return Value**: A newly constructed `container_wrapper` instance
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto container = container_wrapper<int>(10); // Creates container with 10 elements
```
- **Preconditions**: The index must be representable as a size_t
- **Postconditions**: The container has the specified size
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) where n is the size of the container
- **See Also**: `container_wrapper()`, `container_wrapper(Base&& b)`

### operator[] (const)

- **Signature**: `decltype(auto) operator[](IndexType idx) const`
- **Description**: Returns a const reference to the element at the specified index, with bounds checking.
- **Parameters**:
  - `idx` (IndexType): The index of the element to access
- **Return Value**: A const reference to the element at the specified index
- **Exceptions/Errors**: Throws an assertion failure if index is out of bounds
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container[0] = 42;
auto value = container[0]; // Returns 42
```
- **Preconditions**: `idx` must be >= 0 and < `end_index()`
- **Postconditions**: The element at the specified index is returned
- **Thread Safety**: Thread-safe for concurrent reads
- **Complexity**: O(1)
- **See Also**: `operator[] ()`, `end_index()`

### operator[]

- **Signature**: `decltype(auto) operator[](IndexType idx)`
- **Description**: Returns a reference to the element at the specified index, with bounds checking.
- **Parameters**:
  - `idx` (IndexType): The index of the element to access
- **Return Value**: A reference to the element at the specified index
- **Exceptions/Errors**: Throws an assertion failure if index is out of bounds
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container[0] = 42; // Assigns 42 to the first element
```
- **Preconditions**: `idx` must be >= 0 and < `end_index()`
- **Postconditions**: The element at the specified index is accessible and can be modified
- **Thread Safety**: Thread-safe for concurrent reads but not for writes
- **Complexity**: O(1)
- **See Also**: `operator[] () const`, `end_index()`

### end_index

- **Signature**: `IndexType end_index() const`
- **Description**: Returns the end index of the container, which is one past the last valid index.
- **Parameters**: None
- **Return Value**: The end index of the container
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto container = container_wrapper<int>(10);
auto last_valid_index = container.end_index() - 1; // 9
```
- **Preconditions**: None
- **Postconditions**: Returns the end index of the container
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `range()`, `size()`

### range

- **Signature**: `index_range<IndexType> range() const noexcept`
- **Description**: Returns an index range representing the entire valid range of the container.
- **Parameters**: None
- **Return Value**: An `index_range` object representing the valid range of indices
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto container = container_wrapper<int>(10);
auto range = container.range(); // {0, 10}
```
- **Preconditions**: None
- **Postconditions**: Returns a range that represents the valid indices of the container
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `end_index()`, `size()`

### resize

- **Signature**: `void resize(underlying_index s)`
- **Description**: Resizes the container to the specified size, with bounds checking.
- **Parameters**:
  - `s` (underlying_index): The new size of the container
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size is negative or exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.resize(10); // Resizes to 10 elements
```
- **Preconditions**: `s` must be >= 0 and <= maximum representable size
- **Postconditions**: The container has the specified size
- **Thread Safety**: Not thread-safe during resize operations
- **Complexity**: O(n) where n is the new size
- **See Also**: `resize(std::size_t s, T const& v)`, `size()`

### resize

- **Signature**: `void resize(underlying_index s, T const& v)`
- **Description**: Resizes the container to the specified size, filling new elements with the given value.
- **Parameters**:
  - `s` (underlying_index): The new size of the container
  - `v` (T const&): The value to fill new elements with
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size is negative or exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.resize(10, 42); // Resizes to 10 elements, fills with 42
```
- **Preconditions**: `s` must be >= 0 and <= maximum representable size
- **Postconditions**: The container has the specified size, with new elements filled with the given value
- **Thread Safety**: Not thread-safe during resize operations
- **Complexity**: O(n) where n is the new size
- **See Also**: `resize(underlying_index s)`, `size()`

### resize

- **Signature**: `void resize(std::size_t s)`
- **Description**: Resizes the container to the specified size, with bounds checking.
- **Parameters**:
  - `s` (std::size_t): The new size of the container
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.resize(10); // Resizes to 10 elements
```
- **Preconditions**: `s` must be <= maximum representable size
- **Postconditions**: The container has the specified size
- **Thread Safety**: Not thread-safe during resize operations
- **Complexity**: O(n) where n is the new size
- **See Also**: `resize(underlying_index s, T const& v)`, `size()`

### resize

- **Signature**: `void resize(std::size_t s, T const& v)`
- **Description**: Resizes the container to the specified size, filling new elements with the given value.
- **Parameters**:
  - `s` (std::size_t): The new size of the container
  - `v` (T const&): The value to fill new elements with
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.resize(10, 42); // Resizes to 10 elements, fills with 42
```
- **Preconditions**: `s` must be <= maximum representable size
- **Postconditions**: The container has the specified size, with new elements filled with the given value
- **Thread Safety**: Not thread-safe during resize operations
- **Complexity**: O(n) where n is the new size
- **See Also**: `resize(std::size_t s)`, `size()`

### reserve

- **Signature**: `void reserve(underlying_index s)`
- **Description**: Reserves space for at least the specified number of elements, with bounds checking.
- **Parameters**:
  - `s` (underlying_index): The number of elements to reserve space for
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size is negative or exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.reserve(100); // Reserves space for 100 elements
```
- **Preconditions**: `s` must be >= 0 and <= maximum representable size
- **Postconditions**: The container has reserved space for at least the specified number of elements
- **Thread Safety**: Not thread-safe during reserve operations
- **Complexity**: O(n) where n is the number of elements
- **See Also**: `reserve(std::size_t s)`, `size()`

### reserve

- **Signature**: `void reserve(std::size_t s)`
- **Description**: Reserves space for at least the specified number of elements, with bounds checking.
- **Parameters**:
  - `s` (std::size_t): The number of elements to reserve space for
- **Return Value**: None
- **Exceptions/Errors**: Throws an assertion failure if size exceeds the maximum representable size
- **Example**:
```cpp
auto container = container_wrapper<int>(5);
container.reserve(100); // Reserves space for 100 elements
```
- **Preconditions**: `s` must be <= maximum representable size
- **Postconditions**: The container has reserved space for at least the specified number of elements
- **Thread Safety**: Not thread-safe during reserve operations
- **Complexity**: O(n) where n is the number of elements
- **See Also**: `reserve(underlying_index s)`, `size()`

## Usage Examples

### Basic Usage

```cpp
#include <libtorrent/aux_/container_wrapper.hpp>
#include <vector>

int main() {
    // Create a container with default constructor
    libtorrent::aux::container_wrapper<int> container;
    
    // Create a container with initial size
    libtorrent::aux::container_wrapper<int> container2(10);
    
    // Create a container by moving an existing container
    std::vector<int> vec = {1, 2, 3, 4, 5};
    libtorrent::aux::container_wrapper<int> container3(std::move(vec));
    
    // Access elements
    container[0] = 42;
    int value = container[0];
    
    // Resize the container
    container.resize(10);
    
    // Reserve space
    container.reserve(100);
    
    // Get range of valid indices
    auto range = container.range();
    
    return 0;
}
```

### Error Handling

```cpp
#include <libtorrent/aux_/container_wrapper.hpp>
#include <iostream>
#include <vector>

int main() {
    libtorrent::aux::container_wrapper<int> container(5);
    
    try {
        // This will trigger an assertion failure
        container[10] = 42;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    try {
        // This will trigger an assertion failure
        container.resize(-1);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    // Check bounds before accessing
    if (container.size() > 0 && container[0] != 0) {
        std::cout << "First element: " << container[0] << std::endl;
    }
    
    return 0;
}
```

### Edge Cases

```cpp
#include <libtorrent/aux_/container_wrapper.hpp>
#include <iostream>

int main() {
    // Empty container
    libtorrent::aux::container_wrapper<int> empty;
    std::cout << "Empty container size: " << empty.size() << std::endl;
    
    // Container with maximum size
    // Note: This depends on the specific container type and system limits
    libtorrent::aux::container_wrapper<int> max_size(1000000);
    std::cout << "Max size container size: " << max_size.size() << std::endl;
    
    // Resize to zero
    libtorrent::aux::container_wrapper<int> container(5);
    container.resize(0);
    std::cout << "Container after resize to 0: " << container.size() << std::endl;
    
    // Reserve with maximum size
    container.reserve(1000000);
    std::cout << "Container after reserve: " << container.size() << std::endl;
    
    return 0;
}
```

## Best Practices

### Usage Patterns

1. **Use `container_wrapper` for indexed containers**: When you need a container that provides indexed access with bounds checking and type safety.

2. **Prefer `std::size_t` over `underlying_index`**: Use `std::size_t` parameters when possible for better portability and standard compliance.

3. **Use `reserve()` for known sizes**: When you know the approximate size of your container, use `reserve()` to avoid multiple reallocations.

4. **Check bounds before accessing**: Always ensure indices are within bounds before accessing elements, even though bounds checking is performed.

### Common Mistakes to Avoid

1. **Ignoring assertion failures**: The assertion failures in this code are typically for debug builds. Don't rely on them in production code without proper error handling.

2. **Using `underlying_index` for large sizes**: Be aware that `underlying_index` might have limitations compared to `std::size_t`.

3. **Not considering move semantics**: When creating containers from existing containers, prefer move semantics when possible.

### Performance Tips

1. **Use `reserve()` before bulk operations**: When adding multiple elements, reserve space to avoid multiple reallocations.

2. **Avoid unnecessary resizing**: Resizing operations are O(n) and can be expensive, so try to minimize them.

3. **Use `std::size_t` parameters when possible**: `std::size_t` is typically more efficient and portable than custom index types.

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `container_wrapper()`
**Issue**: No documentation for the constructor
**Severity**: Low
**Impact**: Users may not understand the purpose of the default constructor
**Fix**: Add detailed documentation for the constructor

**Function**: `operator[] (const)`
**Issue**: Uses `TORRENT_ASSERT` for bounds checking which may be disabled in release builds
**Severity**: Medium
**Impact**: In release builds, out-of-bounds access may occur without any detection
**Fix**: Consider using `std::range_error` exceptions for better error handling:
```cpp
decltype(auto) operator[](IndexType idx) const
{
    if (idx < IndexType(0) || idx >= end_index()) {
        throw std::range_error("Index out of bounds");
    }
    return this->Base::operator[](std::size_t(static_cast<underlying_index>(idx)));
}
```

**Function**: `resize(underlying_index s)`
**Issue**: No bounds checking on the maximum representable size
**Severity**: High
**Impact**: Could cause integer overflow or undefined behavior
**Fix**: Add proper bounds checking:
```cpp
void resize(underlying_index s)
{
    TORRENT_ASSERT(s >= 0);
    TORRENT_ASSERT(s <= std::size_t((std::numeric_limits<underlying_index>::max)()));
    this->Base::resize(std::size_t(s));
}
```

**Function**: `end_index()`
**Issue**: Repeated assertion with same condition
**Severity**: Medium
**Impact**: Redundant code that could be optimized
**Fix**: Move the assertion to a more logical place or remove it if not needed:
```cpp
IndexType end_index() const
{
    return IndexType(numeric_cast<underlying_index>(this->size()));
}
```

### Modernization Opportunities

**Function**: All functions
**Opportunity**: Use `[[nodiscard]]` for functions that return important values
**Benefit**: Prevents accidental discarding of important return values
**Implementation**:
```cpp
[[nodiscard]] IndexType end_index() const;
[[nodiscard]] index_range<IndexType> range() const noexcept;
```

**Function**: All functions