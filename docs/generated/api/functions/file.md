# libtorrent File Handle API Documentation

## file_handle

- **Signature**: `file_handle()`
- **Description**: Default constructor for the file_handle class. Initializes the file handle with an invalid file descriptor, representing an uninitialized or closed file.
- **Parameters**: None
- **Return Value**: A default-constructed file_handle object with an invalid file descriptor.
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_handle handle;
// handle is now valid but not associated with any file
```
- **Preconditions**: None
- **Postconditions**: The returned file_handle object is in a valid state but not associated with any file.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`

## file_handle

- **Signature**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
- **Description**: Constructor that creates a file handle for the specified file name, size, and open mode. This constructor opens the file and initializes the file handle with the resulting file descriptor.
- **Parameters**:
  - `name` (string_view): The path to the file to open. Must be a valid file path.
  - `size` (std::int64_t): The size of the file in bytes. This is used for validation and internal bookkeeping.
  - `mode` (open_mode_t): The open mode for the file (e.g., read-only, write-only, read-write).
- **Return Value**: A file_handle object initialized with the file descriptor of the opened file.
- **Exceptions/Errors**: 
  - Could throw std::system_error if the file cannot be opened
  - Could throw std::invalid_argument if the parameters are invalid
- **Example**:
```cpp
try {
    file_handle handle("data.txt", 1024, open_mode_t::read_write);
    // handle is now associated with the file
} catch (const std::system_error& e) {
    // handle file opening failure
}
```
- **Preconditions**: 
  - The file path must be valid and accessible
  - The size parameter should match the actual file size
  - The open mode must be valid
- **Postconditions**: The file is opened and the file handle is associated with the file descriptor.
- **Thread Safety**: Not thread-safe during construction (file opening is not atomic)
- **Complexity**: O(1) for initialization, O(log n) for file system operations
- **See Also**: `fd()`, `file_handle(file_handle const& rhs)`

## file_handle

- **Signature**: `file_handle(file_handle const& rhs) = delete`
- **Description**: Deleted copy constructor. Prevents copying of file_handle objects to avoid duplicate file descriptor management and potential resource leaks.
- **Parameters**: 
  - `rhs` (file_handle const&): The right-hand side file handle to copy (not actually used due to deletion)
- **Return Value**: None (function is deleted)
- **Exceptions/Errors**: None (function is deleted, so no exception can be thrown)
- **Example**: 
```cpp
// This will cause a compile-time error:
// file_handle handle1("file.txt", 1024, open_mode_t::read_only);
// file_handle handle2 = handle1; // Error: copy constructor is deleted
```
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Thread-safe (but function is deleted)
- **Complexity**: N/A (function is deleted)
- **See Also**: `file_handle(file_handle&& rhs)`, `operator=(file_handle const& rhs)`

## file_handle

- **Signature**: `file_handle(file_handle&& rhs)`
- **Description**: Move constructor for file_handle. Transfers ownership of the file descriptor from the source file handle to the new file handle, leaving the source in a valid but empty state.
- **Parameters**:
  - `rhs` (file_handle&&): The right-hand side file handle to move from
- **Return Value**: A new file_handle object with the moved file descriptor
- **Exceptions/Errors**: None (nothrow)
- **Example**:
```cpp
file_handle handle1("data.txt", 1024, open_mode_t::read_write);
file_handle handle2 = std::move(handle1); // handle1 is now empty
// handle2 now owns the file descriptor
```
- **Preconditions**: The source file handle must be in a valid state
- **Postconditions**: The destination file handle owns the file descriptor, and the source file handle is left in a valid but empty state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `operator=(file_handle&& rhs)`, `fd()`

## fd

- **Signature**: `handle_type fd() const`
- **Description**: Returns the file descriptor associated with this file handle. This is the raw file descriptor that can be used with standard POSIX or Windows file operations.
- **Parameters**: None
- **Return Value**: The file descriptor (handle_type) associated with this file handle. Returns an invalid handle value if the file handle is not associated with a file.
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_handle handle("data.txt", 1024, open_mode_t::read_only);
if (handle.fd() != invalid_handle) {
    // Use the file descriptor with system calls
    // For example: ::read(handle.fd(), buffer, sizeof(buffer));
}
```
- **Preconditions**: The file handle must be in a valid state
- **Postconditions**: The file descriptor remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `file_handle()`, `file_handle(string_view name, std::int64_t size, open_mode_t mode)`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/file.hpp>
#include <iostream>

int main() {
    try {
        // Create a file handle for reading
        file_handle handle("example.txt", 2048, open_mode_t::read_only);
        
        // Check if the file handle is valid
        if (handle.fd() != invalid_handle) {
            std::cout << "File opened successfully with fd: " 
                      << handle.fd() << std::endl;
        } else {
            std::cerr << "Failed to open file" << std::endl;
        }
        
        // Use the file handle (in real code, this would involve file operations)
        // For example: read from the file using the fd
        
    } catch (const std::system_error& e) {
        std::cerr << "System error opening file: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Error Handling

```cpp
#include <libtorrent/file.hpp>
#include <iostream>
#include <string>

void processFile(const std::string& filename) {
    try {
        // Attempt to open the file
        file_handle handle(filename, 0, open_mode_t::read_write);
        
        if (handle.fd() == invalid_handle) {
            std::cerr << "Failed to open file: " << filename << std::endl;
            return;
        }
        
        // File opened successfully
        std::cout << "Successfully opened file: " << filename << std::endl;
        
        // Perform operations on the file
        // ...
        
    } catch (const std::system_error& e) {
        std::cerr << "Failed to open file '" << filename 
                  << "' due to system error: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Unexpected error processing file '" << filename 
                  << "': " << e.what() << std::endl;
    }
}

int main() {
    processFile("data.txt");
    processFile("nonexistent.txt"); // This will fail
    return 0;
}
```

## Edge Cases

```cpp
#include <libtorrent/file.hpp>
#include <iostream>

void demonstrateEdgeCases() {
    // Edge case 1: Empty file name
    try {
        file_handle handle("", 0, open_mode_t::read_only);
        std::cout << "Empty filename handled successfully" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Failed to handle empty filename: " << e.what() << std::endl;
    }
    
    // Edge case 2: Very large file size
    try {
        file_handle handle("huge_file.dat", 1LL << 40, open_mode_t::read_write);
        std::cout << "Large file opened successfully" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Failed to open large file: " << e.what() << std::endl;
    }
    
    // Edge case 3: Move semantics
    file_handle source("move_test.txt", 1024, open_mode_t::read_only);
    file_handle destination = std::move(source); // Source is now empty
    if (destination.fd() != invalid_handle) {
        std::cout << "Move successful, destination owns file" << std::endl;
    }
}

int main() {
    demonstrateEdgeCases();
    return 0;
}
```

# Best Practices

## Effective Usage

1. **Always check file handle validity** after construction:
```cpp
file_handle handle("file.txt", 1024, open_mode_t::read_only);
if (handle.fd() == invalid_handle) {
    // Handle error appropriately
}
```

2. **Use move semantics for efficient transfers**:
```cpp
file_handle createHandle(const std::string& filename) {
    return file_handle(filename, 0, open_mode_t::read_only);
}

file_handle handle = createHandle("data.txt");
```

3. **Don't copy file handles** - use move semantics instead:
```cpp
// Bad - would fail to compile
// file_handle handle1("file.txt", 1024, open_mode_t::read_write);
// file_handle handle2 = handle1; // Error: copy constructor deleted

// Good - use move semantics
file_handle handle1("file.txt", 1024, open_mode_t::read_write);
file_handle handle2 = std::move(handle1);
```

## Common Mistakes to Avoid

1. **Assuming file opening always succeeds**:
```cpp
// Bad - doesn't handle errors
file_handle handle("data.txt", 1024, open_mode_t::read_write);

// Good - handles potential errors
try {
    file_handle handle("data.txt", 1024, open_mode_t::read_write);
    // Use handle
} catch (const std::exception& e) {
    // Handle error
}
```

2. **Using moved-from objects**:
```cpp
// Bad - undefined behavior
file_handle handle1("file.txt", 1024, open_mode_t::read_only);
file_handle handle2 = std::move(handle1);
// handle1 is now empty and should not be used
int fd = handle1.fd(); // Undefined behavior
```

3. **Not closing files explicitly**:
```cpp
// Bad - file handle may not be closed properly
{
    file_handle handle("file.txt", 1024, open_mode_t::read_write);
    // File operations
} // handle destructor may not clean up properly

// Good - ensure proper cleanup
{
    file_handle handle("file.txt", 1024, open_mode_t::read_write);
    // File operations
    // handle will be properly destroyed when it goes out of scope
}
```

## Performance Tips

1. **Minimize file handle creation/destruction**:
```cpp
// Bad - creates and destroys multiple file handles
for (int i = 0; i < 1000; ++i) {
    file_handle handle("data.txt", 1024, open_mode_t::read_write);
    // Use handle
}

// Good - reuse the same file handle
file_handle handle("data.txt", 1024, open_mode_t::read_write);
for (int i = 0; i < 1000; ++i) {
    // Use handle
}
```

2. **Use move semantics for passing file handles**:
```cpp
// Bad - would copy (but copy is deleted anyway)
void processFile(file_handle handle);

// Good - pass by move
void processFile(file_handle&& handle) {
    // Use handle
}
```

3. **Close files when no longer needed**:
```cpp
{
    file_handle handle("data.txt", 1024, open_mode_t::read_write);
    // Use handle
    // handle will be destroyed and closed properly
} // file closed automatically
```

# Code Review & Improvement Suggestions

## Potential Issues

### Security

**Function**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
**Issue**: No input validation for the file name, which could lead to security vulnerabilities like path traversal attacks.
**Severity**: High
**Impact**: Could allow access to sensitive files or execute arbitrary code.
**Fix**: Add validation for the file name to prevent path traversal:
```cpp
// Add this validation in the constructor
if (name.find("..") != std::string_view::npos || name.find('/') != 0) {
    throw std::invalid_argument("Invalid file name: contains path traversal");
}
```

### Performance

**Function**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
**Issue**: File opening could be slow for large files, and the size parameter is not validated against actual file size.
**Severity**: Medium
**Impact**: Could lead to performance degradation and incorrect file handling.
**Fix**: Add size validation and consider asynchronous file opening:
```cpp
// Add size validation
struct stat file_stat;
if (stat(name.data(), &file_stat) == 0 && file_stat.st_size != size) {
    throw std::invalid_argument("File size mismatch");
}
```

### Correctness

**Function**: `file_handle(file_handle&& rhs)`
**Issue**: The move constructor doesn't check for self-move, though it's unlikely to be an issue in practice.
**Severity**: Low
**Impact**: Could lead to subtle bugs in edge cases.
**Fix**: Add self-move check:
```cpp
file_handle(file_handle&& rhs) : m_fd(rhs.m_fd) {
    if (this != &rhs) {
        rhs.m_fd = invalid_handle;
    }
}
```

### Code Quality

**Function**: `file_handle(file_handle const& rhs) = delete`
**Issue**: The comment for the deleted copy constructor is missing.
**Severity**: Low
**Impact**: Reduced code clarity.
**Fix**: Add a comment explaining why the copy constructor is deleted:
```cpp
// Deleted copy constructor to prevent duplicate file descriptor management
file_handle(file_handle const& rhs) = delete;
```

### Modernization Opportunities

**Function**: `fd()`
**Issue**: The function could benefit from being marked as `[[nodiscard]]` since the file descriptor is important.
**Severity**: Low
**Impact**: Could lead to silent bugs if the return value is ignored.
**Fix**: Mark the function as `[[nodiscard]]`:
```cpp
[[nodiscard]] handle_type fd() const { return m_fd; }
```

**Function**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
**Issue**: The function could benefit from using `std::expected` (C++23) for error handling instead of exceptions.
**Severity**: Medium
**Impact**: Could improve error handling in cases where exceptions are not desired.
**Fix**: Replace with a function that returns `std::expected<file_handle, std::error_code>`:
```cpp
[[nodiscard]] std::expected<file_handle, std::error_code> create_file_handle(
    std::string_view name, std::int64_t size, open_mode_t mode);
```

### Refactoring Suggestions

**Function**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
**Suggestion**: Split the file handle creation into separate functions for different use cases (e.g., create_read_handle, create_write_handle).

**Function**: `file_handle(file_handle&& rhs)`
**Suggestion**: Consider making this a class method instead of a standalone function, though it's already properly implemented as a move constructor.

### Performance Optimizations

**Function**: `file_handle(string_view name, std::int64_t size, open_mode_t mode)`
**Opportunity**: Use move semantics for the string_view parameter to avoid copying.
**Fix**: The parameter is already a const reference, so it's already optimized. However, consider using `std::string_view` instead of `string_view` if available.

**Function**: `fd()`
**Opportunity**: Consider adding a `noexcept` specifier since this function doesn't throw exceptions.
**Fix**: Add `noexcept` specifier:
```cpp
handle_type fd() const noexcept { return m_fd; }
```