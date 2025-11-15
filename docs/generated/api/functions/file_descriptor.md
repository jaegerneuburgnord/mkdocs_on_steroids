# `file_descriptor` Class API Documentation

## Class Overview

The `file_descriptor` class is a RAII (Resource Acquisition Is Initialization) wrapper for file descriptors in C++. It manages the lifecycle of a file descriptor, ensuring that it is properly closed when the object goes out of scope. The class follows the Rule of Five (or Rule of Zero, since it manages a resource), and provides safe, exception-aware resource management.

## Public Member Functions

### `file_descriptor`

- **Signature**: `file_descriptor(int fd)`
- **Description**: Constructs a `file_descriptor` object that wraps the given file descriptor. The constructor takes ownership of the file descriptor and will ensure it is closed when the object is destroyed.
- **Parameters**:
  - `fd` (`int`): The file descriptor to wrap. Valid values are non-negative integers representing an open file descriptor. A value of -1 is invalid and should not be passed to this constructor.
- **Return Value**: None (constructor).
- **Exceptions/Errors**: 
  - No exceptions thrown by the constructor itself. However, if the `fd` parameter is invalid (e.g., negative or already closed), the behavior is undefined.
- **Example**:
```cpp
#include <libtorrent/aux_/file_descriptor.hpp>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("example.txt", O_RDONLY);
    if (fd == -1) {
        // Handle error
        return 1;
    }
    file_descriptor descriptor(fd); // Takes ownership of the file descriptor
    // Use descriptor
    return 0;
}
```
- **Preconditions**: The `fd` parameter must be a valid, open file descriptor.
- **Postconditions**: The `file_descriptor` object is constructed and owns the file descriptor. The file descriptor will be closed when the object is destroyed.
- **Thread Safety**: The constructor is thread-safe as long as the file descriptor is not accessed concurrently by other threads.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `~file_descriptor()`, `fd()`

### `~file_descriptor`

- **Signature**: `~file_descriptor()`
- **Description**: Destructor that closes the file descriptor if it is still valid. This ensures that the file descriptor is properly cleaned up when the `file_descriptor` object is destroyed, preventing resource leaks.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: 
  - If the file descriptor is invalid (e.g., negative), `::close()` may not be called or may result in undefined behavior. However, the class ensures that `m_fd >= 0` before calling `::close()`, so this is safe in normal usage.
- **Example**:
```cpp
#include <libtorrent/aux_/file_descriptor.hpp>

void example() {
    file_descriptor descriptor(1); // e.g., stdout
    // descriptor is automatically closed when it goes out of scope
}
```
- **Preconditions**: The object must be in a valid state (i.e., not already destroyed).
- **Postconditions**: The file descriptor is closed if it was valid. The file descriptor is no longer accessible through this object.
- **Thread Safety**: The destructor is thread-safe as long as no other thread is accessing the file descriptor.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `file_descriptor(int fd)`, `fd()`

### `file_descriptor`

- **Signature**: `file_descriptor(file_descriptor const&) = delete`
- **Description**: Deleted copy constructor. This prevents copying of `file_descriptor` objects, ensuring that each file descriptor is owned by exactly one object. This is a safety feature to prevent double-closing of file descriptors.
- **Parameters**: None (deleted function).
- **Return Value**: None.
- **Exceptions/Errors**: Not applicable (function is deleted).
- **Example**: Attempting to copy a `file_descriptor` object will result in a compile-time error:
```cpp
file_descriptor descriptor(1);
file_descriptor descriptor2 = descriptor; // Compilation error: copy constructor is deleted
```
- **Preconditions**: None.
- **Postconditions**: The object remains unchanged (no action taken).
- **Thread Safety**: Not applicable (function is deleted).
- **Complexity**: N/A.
- **See Also**: `file_descriptor(file_descriptor&&)`, `fd()`

### `file_descriptor`

- **Signature**: `file_descriptor(file_descriptor&& rhs)`
- **Description**: Move constructor that transfers ownership of the file descriptor from the source object to the new object. This allows efficient transfer of ownership without copying the file descriptor.
- **Parameters**:
  - `rhs` (`file_descriptor&&`): The source object whose file descriptor will be moved. After the move, the source object's file descriptor will be set to -1 to indicate that it no longer owns the file descriptor.
- **Return Value**: None (constructor).
- **Exceptions/Errors**: 
  - No exceptions thrown by the move constructor. The move operation is guaranteed to succeed as long as the source object is in a valid state.
- **Example**:
```cpp
#include <libtorrent/aux_/file_descriptor.hpp>

void example() {
    file_descriptor descriptor1(1);
    file_descriptor descriptor2(std::move(descriptor1)); // Move ownership
    // descriptor1 is now invalid (m_fd = -1)
    // descriptor2 now owns the file descriptor
}
```
- **Preconditions**: The source object (`rhs`) must be in a valid state (i.e., not already moved from).
- **Postconditions**: The new object owns the file descriptor, and the source object's file descriptor is set to -1.
- **Thread Safety**: The move constructor is thread-safe as long as the source object is not being accessed concurrently.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `file_descriptor(int fd)`, `fd()`

### `fd`

- **Signature**: `int fd() const`
- **Description**: Returns the underlying file descriptor value. This allows access to the raw file descriptor if needed, for example, when interfacing with system calls or other libraries that expect a file descriptor.
- **Parameters**: None.
- **Return Value**:
  - Returns the file descriptor value (`int`) if it is valid.
  - Returns -1 if the file descriptor is not valid (i.e., if it has been closed or moved from).
- **Exceptions/Errors**: 
  - No exceptions thrown by this function.
- **Example**:
```cpp
#include <libtorrent/aux_/file_descriptor.hpp>
#include <unistd.h>

void example() {
    file_descriptor descriptor(1);
    int fd = descriptor.fd(); // Get the file descriptor
    if (fd != -1) {
        // Use the file descriptor with system calls
        write(fd, "Hello, world!", 13);
    }
}
```
- **Preconditions**: The object must be in a valid state (i.e., not destroyed).
- **Postconditions**: The file descriptor value is returned without modifying the object.
- **Thread Safety**: This function is thread-safe as long as the underlying file descriptor is not being modified concurrently.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `file_descriptor(int fd)`, `~file_descriptor()`

## Usage Examples

### Basic Usage

```cpp
#include <libtorrent/aux_/file_descriptor.hpp>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("example.txt", O_RDONLY);
    if (fd == -1) {
        // Handle error
        return 1;
    }
    file_descriptor descriptor(fd); // Takes ownership of the file descriptor
    // Use descriptor
    return 0;
}
```

### Error Handling

```cpp
#include <libtorrent/aux_/file_descriptor.hpp>
#include <fcntl.h>
#include <unistd.h>
#include <cerrno>
#include <iostream>

int main() {
    int fd = open("nonexistent.txt", O_RDONLY);
    if (fd == -1) {
        std::cerr << "Failed to open file: " << strerror(errno) << std::endl;
        return 1;
    }
    file_descriptor descriptor(fd);
    // Use descriptor
    return 0;
}
```

### Edge Cases

```cpp
#include <libtorrent/aux_/file_descriptor.hpp>
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Edge case: file descriptor is already closed
    int fd = -1;
    file_descriptor descriptor(fd); // This is valid but not useful
    // The file descriptor will not be closed since m_fd < 0
    return 0;
}
```

## Best Practices

### How to Use These Functions Effectively

- Always ensure that the file descriptor passed to the constructor is valid and open.
- Use the move constructor to transfer ownership of file descriptors between objects.
- Avoid copying `file_descriptor` objects; use move semantics instead.
- Use the `fd()` method only when necessary, as it exposes the raw file descriptor.

### Common Mistakes to Avoid

- Passing an invalid file descriptor (e.g., -1) to the constructor, which may lead to undefined behavior.
- Attempting to copy a `file_descriptor` object, which will result in a compile-time error.
- Using the `fd()` method to access a file descriptor that has already been moved from or closed.

### Performance Tips

- Use move semantics to transfer ownership of file descriptors efficiently.
- Avoid unnecessary calls to `fd()` unless you need the raw file descriptor.
- Ensure that the file descriptor is closed when it is no longer needed to prevent resource leaks.

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `file_descriptor(int fd)`
**Issue**: No validation of the `fd` parameter. If `fd` is negative or invalid, the behavior is undefined.
**Severity**: Medium
**Impact**: Could lead to undefined behavior or crashes if an invalid file descriptor is passed.
**Fix**: Add validation and handle invalid file descriptors gracefully:
```cpp
file_descriptor(int fd) : m_fd(fd) {
    if (fd < 0) {
        // Handle invalid file descriptor (e.g., throw exception)
        throw std::invalid_argument("File descriptor must be non-negative");
    }
}
```

**Function**: `~file_descriptor()`
**Issue**: The destructor calls `::close(m_fd)` without checking if `m_fd` is already -1, which is safe but could be optimized.
**Severity**: Low
**Impact**: Minimal impact on performance or correctness.
**Fix**: No change needed; the current implementation is safe and correct.

**Function**: `file_descriptor(file_descriptor const&) = delete`
**Issue**: The deletion of the copy constructor is correct, but could be documented more clearly.
**Severity**: Low
**Impact**: None.
**Fix**: Add a comment to clarify the reason for deletion:
```cpp
// Deleted copy constructor to prevent double-closing of file descriptors
file_descriptor(file_descriptor const&) = delete;
```

**Function**: `file_descriptor(file_descriptor&& rhs)`
**Issue**: The move constructor is correct but could be optimized for performance by avoiding unnecessary checks.
**Severity**: Low
**Impact**: Minimal impact on performance.
**Fix**: No change needed; the current implementation is efficient and correct.

**Function**: `fd()`
**Issue**: The `fd()` method returns -1 when the file descriptor is invalid, but this could be documented more clearly.
**Severity**: Low
**Impact**: None.
**Fix**: Add a comment to clarify the return value:
```cpp
/// Returns the underlying file descriptor value.
/// Returns -1 if the file descriptor is invalid or has been moved from.
int fd() const { return m_fd; }
```

### Modernization Opportunities

**Function**: `file_descriptor(int fd)`
**Opportunity**: Use `[[nodiscard]]` to indicate that the constructor should not be ignored.
**Suggestion**: Add `[[nodiscard]]` to the constructor:
```cpp
[[nodiscard]] file_descriptor(int fd) : m_fd(fd) {}
```

**Function**: `fd()`
**Opportunity**: Use `std::expected` (C++23) for error handling.
**Suggestion**: Return `std::expected<int, std::error_code>` instead of `int` to indicate success or failure:
```cpp
std::expected<int, std::error_code> fd() const {
    if (m_fd == -1) {
        return std::unexpected<std::error_code>(std::errc::bad_file_descriptor);
    }
    return m_fd;
}
```

### Refactoring Suggestions

**Function**: `file_descriptor(int fd)`
**Suggestion**: Move the constructor into a factory function to centralize file descriptor creation.
**Reason**: This could make it easier to add validation or logging.
**Example**:
```cpp
file_descriptor create_file_descriptor(int fd) {
    if (fd < 0) {
        throw std::invalid_argument("File descriptor must be non-negative");
    }
    return file_descriptor(fd);
}
```

**Function**: `~file_descriptor()`
**Suggestion**: Move the destructor into a separate class to allow for more complex cleanup logic.
**Reason**: This could be useful if additional cleanup is needed in the future.
**Example**:
```cpp
class file_descriptor_cleaner {
public:
    ~file_descriptor_cleaner() {
        if (m_fd >= 0) {
            ::close(m_fd);
        }
    }
private:
    int m_fd;
};
```

### Performance Optimizations

**Function**: `file_descriptor(int fd)`
**Opportunity**: Use move semantics in the constructor to avoid unnecessary copies.
**Suggestion**: No change needed; the constructor already takes the file descriptor by value and is efficient.

**Function**: `fd()`
**Opportunity**: Use `std::span` for array parameters.
**Suggestion**: Not applicable; the `fd()` method does not take array parameters.

**Function**: `file_descriptor(file_descriptor&& rhs)`
**Opportunity**: Add `noexcept` to the move constructor.
**Suggestion**: Add `noexcept` to the move constructor:
```cpp
file_descriptor(file_descriptor&& rhs) noexcept : m_fd(rhs.m_fd) {
    rhs.m_fd = -1;
}
```