# libtorrent WinFileHandle API Documentation

## win_file_handle (Constructor)

- **Signature**: `win_file_handle(HANDLE h)`
- **Description**: Constructs a `win_file_handle` object from a Windows HANDLE. This constructor takes ownership of the provided file handle and will automatically close it when the `win_file_handle` object is destroyed.
- **Parameters**:
  - `h` (HANDLE): The Windows file handle to wrap. This handle must be valid and represent a file, pipe, or device. The function will take ownership of this handle.
- **Return Value**:
  - This is a constructor and does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown by this constructor.
- **Example**:
```cpp
HANDLE file_handle = CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
if (file_handle != INVALID_HANDLE_VALUE) {
    libtorrent::aux::win_file_handle handle(file_handle);
    // Use the handle
}
```
- **Preconditions**: The `h` parameter must be a valid Windows file handle (not INVALID_HANDLE_VALUE).
- **Postconditions**: The `win_file_handle` object is constructed and owns the provided handle. The handle is no longer available to the caller.
- **Thread Safety**: This function is not thread-safe as it involves construction of an object.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `~win_file_handle()`, `handle()`

## ~win_file_handle (Destructor)

- **Signature**: `~win_file_handle()`
- **Description**: Destructor that closes the underlying Windows file handle if it is valid. This ensures that file handles are properly cleaned up when the `win_file_handle` object goes out of scope.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown by this destructor.
- **Example**:
```cpp
{
    libtorrent::aux::win_file_handle handle(CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr));
    // handle is automatically closed when it goes out of scope
}
```
- **Preconditions**: The object must be in a valid state (not destroyed).
- **Postconditions**: The underlying file handle is closed if it was valid.
- **Thread Safety**: This function is thread-safe as long as the object is not being accessed by multiple threads concurrently.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `win_file_handle(HANDLE h)`, `handle()`

## win_file_handle (Copy Constructor)

- **Signature**: `win_file_handle(win_file_handle const&) = delete`
- **Description**: Deleted copy constructor that prevents copying of `win_file_handle` objects. This is because file handles cannot be duplicated safely in this context without proper synchronization.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - Attempting to copy a `win_file_handle` object will result in a compile-time error.
- **Example**:
```cpp
// This will cause a compile-time error:
// libtorrent::aux::win_file_handle handle1(CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr));
// libtorrent::aux::win_file_handle handle2 = handle1; // Error: cannot copy
```
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: This function is thread-safe as it's not callable.
- **Complexity**: N/A (function doesn't exist)
- **See Also**: `win_file_handle(win_file_handle&&)`, `handle()`

## win_file_handle (Move Constructor)

- **Signature**: `win_file_handle(win_file_handle&& rhs)`
- **Description**: Move constructor that transfers ownership of the file handle from the source object to the new object. This allows efficient transfer of ownership without copying the handle.
- **Parameters**:
  - `rhs` (win_file_handle&&): The source `win_file_handle` object from which to move the handle. The source object will be left in a valid but unspecified state.
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown by this constructor.
- **Example**:
```cpp
libtorrent::aux::win_file_handle handle1(CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr));
libtorrent::aux::win_file_handle handle2(std::move(handle1)); // Transfer ownership
// handle1 is now in a valid but unspecified state
```
- **Preconditions**: The `rhs` parameter must be in a valid state (not destroyed).
- **Postconditions**: The new object owns the file handle, and the source object no longer owns it.
- **Thread Safety**: This function is thread-safe as long as the source object is not being accessed by multiple threads concurrently.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `win_file_handle(HANDLE h)`, `handle()`

## handle

- **Signature**: `HANDLE handle() const`
- **Description**: Returns the underlying Windows file handle that this object owns. This allows access to the raw handle for use with Windows API functions.
- **Parameters**: None
- **Return Value**:
  - Returns the underlying HANDLE. The returned handle is valid as long as the `win_file_handle` object is alive.
- **Exceptions/Errors**:
  - No exceptions are thrown by this function.
- **Example**:
```cpp
libtorrent::aux::win_file_handle handle(CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr));
HANDLE raw_handle = handle.handle();
// Use raw_handle with Windows API functions
```
- **Preconditions**: The object must be in a valid state (not destroyed).
- **Postconditions**: The returned handle is valid and can be used with Windows API functions.
- **Thread Safety**: This function is thread-safe as it only reads a member variable.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `win_file_handle(HANDLE h)`, `~win_file_handle()`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/win_file_handle.hpp>
#include <windows.h>

// Create a file handle and wrap it in win_file_handle
HANDLE file_handle = CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
if (file_handle != INVALID_HANDLE_VALUE) {
    libtorrent::aux::win_file_handle handle(file_handle);
    
    // Use the handle with Windows API functions
    DWORD bytes_read;
    char buffer[1024];
    if (ReadFile(handle.handle(), buffer, sizeof(buffer), &bytes_read, nullptr)) {
        // Process the data
    }
    
    // handle is automatically closed when it goes out of scope
}
```

## Error Handling

```cpp
#include <libtorrent/aux_/win_file_handle.hpp>
#include <windows.h>
#include <iostream>

// Create a file handle and wrap it in win_file_handle
HANDLE file_handle = CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
if (file_handle == INVALID_HANDLE_VALUE) {
    std::cerr << "Failed to open file: " << GetLastError() << std::endl;
} else {
    libtorrent::aux::win_file_handle handle(file_handle);
    
    // Use the handle with Windows API functions
    DWORD bytes_read;
    char buffer[1024];
    if (!ReadFile(handle.handle(), buffer, sizeof(buffer), &bytes_read, nullptr)) {
        std::cerr << "Failed to read file: " << GetLastError() << std::endl;
    } else {
        // Process the data
        std::cout << "Read " << bytes_read << " bytes" << std::endl;
    }
    
    // handle is automatically closed when it goes out of scope
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/win_file_handle.hpp>
#include <windows.h>

// Test with a non-existent file
HANDLE file_handle = CreateFileA("nonexistent.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
if (file_handle == INVALID_HANDLE_VALUE) {
    std::cerr << "File does not exist or cannot be opened" << std::endl;
} else {
    libtorrent::aux::win_file_handle handle(file_handle);
    // The handle will be closed when handle goes out of scope
}

// Test with a file that is already open
HANDLE file_handle2 = CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
if (file_handle2 != INVALID_HANDLE_VALUE) {
    libtorrent::aux::win_file_handle handle2(file_handle2);
    // handle2 can be used to read the file
}

// Test with a moved handle
libtorrent::aux::win_file_handle handle3(CreateFileA("example.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr));
libtorrent::aux::win_file_handle handle4(std::move(handle3));
// handle3 is now in a valid but unspecified state
```

# Best Practices

1. **Always check for invalid handles**: Always verify that `CreateFile` or other Windows API functions return a valid handle before creating a `win_file_handle` object.

2. **Use RAII properly**: Let the `win_file_handle` object manage the file handle lifecycle. The destructor will automatically close the handle when the object goes out of scope.

3. **Avoid copying**: Since the copy constructor is deleted, avoid copying `win_file_handle` objects. Use move semantics instead.

4. **Use move semantics for transfer**: When you need to transfer ownership of a file handle, use the move constructor or `std::move`.

5. **Check return values**: Always check the return values of Windows API functions called on the handle to detect errors.

6. **Close handles properly**: Don't try to close the handle directly using `CloseHandle` when you have a `win_file_handle` object, as it will be closed automatically.

# Code Review & Improvement Suggestions

## win_file_handle (Constructor)

**Function**: `win_file_handle(HANDLE h)`
**Issue**: The function doesn't validate the handle parameter for security reasons.
**Severity**: Medium
**Impact**: Could lead to undefined behavior if an invalid handle is passed.
**Fix**: Add handle validation:
```cpp
win_file_handle(HANDLE h) : m_h(h) {
    if (h == INVALID_HANDLE_VALUE) {
        throw std::invalid_argument("Invalid handle provided");
    }
}
```

## ~win_file_handle (Destructor)

**Function**: `~win_file_handle()`
**Issue**: The destructor doesn't handle the case where `CloseHandle` fails.
**Severity**: Medium
**Impact**: Could result in resource leaks if `CloseHandle` fails.
**Fix**: Add error handling:
```cpp
~win_file_handle() {
    if (m_h != INVALID_HANDLE_VALUE) {
        if (!::CloseHandle(m_h)) {
            // Log error or handle it appropriately
            // Note: This is a best effort - we can't throw in destructor
        }
    }
}
```

## win_file_handle (Copy Constructor)

**Function**: `win_file_handle(win_file_handle const&) = delete`
**Issue**: The function name is the same as the class name, which can be confusing.
**Severity**: Low
**Impact**: Minor confusion for developers reading the code.
**Fix**: Consider renaming the class to avoid confusion with the constructor:
```cpp
class win_file_handle {
    // Implementation
};
```

## win_file_handle (Move Constructor)

**Function**: `win_file_handle(win_file_handle&& rhs)`
**Issue**: The function doesn't validate the source handle.
**Severity**: Medium
**Impact**: Could lead to undefined behavior if the source handle is invalid.
**Fix**: Add handle validation:
```cpp
win_file_handle(win_file_handle&& rhs) : m_h(rhs.m_h) {
    if (rhs.m_h == INVALID_HANDLE_VALUE) {
        throw std::invalid_argument("Invalid handle in source");
    }
    rhs.m_h = INVALID_HANDLE_VALUE;
}
```

## handle

**Function**: `HANDLE handle() const`
**Issue**: The function name could be more descriptive.
**Severity**: Low
**Impact**: Minor readability issue.
**Fix**: Consider renaming to `get_handle()`:
```cpp
HANDLE get_handle() const { return m_h; }
```

# Modernization Opportunities

1. **Add [[nodiscard]]**: Add `[[nodiscard]]` to the `handle()` function since the returned handle is important:
```cpp
[[nodiscard]] HANDLE handle() const { return m_h; }
```

2. **Use std::optional for error handling**: Consider returning `std::optional<HANDLE>` from the constructor to handle invalid handles:
```cpp
std::optional<win_file_handle> create_handle(const char* path) {
    HANDLE h = CreateFileA(path, GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
    if (h == INVALID_HANDLE_VALUE) {
        return std::nullopt;
    }
    return win_file_handle(h);
}
```

3. **Use std::unique_ptr for ownership**: Consider using `std::unique_ptr<win_file_handle>` for better ownership semantics:
```cpp
std::unique_ptr<libtorrent::aux::win_file_handle> create_handle(const char* path) {
    HANDLE h = CreateFileA(path, GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
    if (h == INVALID_HANDLE_VALUE) {
        return nullptr;
    }
    return std::make_unique<libtorrent::aux::win_file_handle>(h);
}
```

# Refactoring Suggestions

1. **Move to utility namespace**: Consider moving the `win_file_handle` class to a utility namespace:
```cpp
namespace libtorrent::util {
    class win_file_handle {
        // Implementation
    };
}
```

2. **Add RAII wrapper**: Create a higher-level RAII wrapper for file operations that uses `win_file_handle`:
```cpp
class file_reader {
    libtorrent::aux::win_file_handle m_handle;
public:
    file_reader(const char* path) : m_handle(CreateFileA(path, GENERIC_READ, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr)) {
        if (m_handle.handle() == INVALID_HANDLE_VALUE) {
            throw std::runtime_error("Failed to open file");
        }
    }
    
    // Read and other file operations
};
```

# Performance Optimizations

1. **Return by value for RVO**: The `handle()` function already returns by value, which allows return value optimization.

2. **Use move semantics**: The move constructor is already properly implemented.

3. **Add noexcept**: Consider adding `noexcept` to the destructor and move constructor:
```cpp
~win_file_handle() noexcept {
    if (m_h != INVALID_HANDLE_VALUE) {
        ::CloseHandle(m_h);
    }
}

win_file_handle(win_file_handle&& rhs) noexcept : m_h(rhs.m_h) {
    rhs.m_h = INVALID_HANDLE_VALUE;
}
```

4. **Use const references**: The `handle()` function already uses `const` correctly.

5. **Avoid unnecessary copies**: The copy constructor is deleted, which prevents unnecessary copies and ensures proper ownership semantics.