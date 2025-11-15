# API Documentation for `file_mapping` and `file_mapping_handle`

## Overview
This documentation covers the `file_mapping` and `file_mapping_handle` classes used for memory-mapped file operations in the libtorrent library. These classes provide a safe and efficient way to map files into memory for reading and writing operations.

## Class: `file_mapping_handle`

### `file_mapping_handle(file_handle file, open_mode_t mode, std::int64_t size)`

- **Signature**: `file_mapping_handle(file_handle file, open_mode_t mode, std::int64_t size)`
- **Description**: Constructs a `file_mapping_handle` object that manages a memory-mapped file. This constructor creates a mapping of the specified file size with the given open mode.
- **Parameters**:
  - `file` (file_handle): The file handle to map. Must be valid and opened with appropriate permissions.
  - `mode` (open_mode_t): The access mode for the file (read-only, read-write, etc.).
  - `size` (std::int64_t): The size of the file to map in bytes. Must be non-negative.
- **Return Value**: None (constructor).
- **Exceptions/Errors**:
  - `std::runtime_error`: Thrown if the memory mapping fails (e.g., insufficient memory, file not found, or permission issues).
- **Example**:
```cpp
file_handle file = open_file("example.txt", open_mode::read_only);
file_mapping_handle mapping(file, open_mode::read_only, 1024);
```
- **Preconditions**: The file handle must be valid and opened with the correct mode.
- **Postconditions**: The object is constructed with a valid memory mapping if successful.
- **Thread Safety**: Not thread-safe during construction.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `~file_mapping_handle()`, `handle()`

### `~file_mapping_handle()`

- **Signature**: `~file_mapping_handle()`
- **Description**: Destructor that releases the memory mapping and closes the file handle. This ensures proper cleanup of system resources.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: None (if the mapping cannot be released, it may cause resource leaks).
- **Example**:
```cpp
file_mapping_handle mapping(file, open_mode::read_only, 1024);
// Use the mapping...
// Destructor is called when the object goes out of scope
```
- **Preconditions**: The object must be valid (constructed).
- **Postconditions**: The memory mapping is unmapped and the file handle is closed.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `file_mapping_handle()`

### `file_mapping_handle(file_mapping_handle const&) = delete`

- **Signature**: `file_mapping_handle(file_mapping_handle const&) = delete`
- **Description**: Deleted copy constructor prevents copying of `file_mapping_handle` objects. This ensures that memory mappings are not duplicated, which could lead to resource conflicts.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: None.
- **Example**: This function cannot be called directly as it's deleted.
- **Preconditions**: None.
- **Postconditions**: None.
- **Thread Safety**: Not applicable.
- **Complexity**: O(1).
- **See Also**: `operator=`

### `file_mapping_handle& operator=(file_mapping_handle const&) = delete`

- **Signature**: `file_mapping_handle& operator=(file_mapping_handle const&) = delete`
- **Description**: Deleted assignment operator prevents assignment of `file_mapping_handle` objects. This ensures that memory mappings are not duplicated or shared unintentionally.
- **Parameters**: `other` (file_mapping_handle const&): The object to assign from.
- **Return Value**: `file_mapping_handle&`: Reference to the current object.
- **Exceptions/Errors**: None.
- **Example**: This function cannot be called directly as it's deleted.
- **Preconditions**: None.
- **Postconditions**: None.
- **Thread Safety**: Not applicable.
- **Complexity**: O(1).
- **See Also**: `file_mapping_handle()`

### `handle()`

- **Signature**: `HANDLE handle() const`
- **Description**: Returns the underlying Windows handle (HANDLE) associated with the memory mapping. This can be used for low-level Windows API operations.
- **Parameters**: None.
- **Return Value**: `HANDLE`: The Windows handle to the memory mapping. Returns `nullptr` if no mapping exists.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
file_mapping_handle mapping(file, open_mode::read_only, 1024);
HANDLE h = mapping.handle();
if (h != nullptr) {
    // Use the handle with Windows API functions
}
```
- **Preconditions**: The object must be valid and constructed.
- **Postconditions**: The returned handle is valid if the mapping exists.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `fd()`

### `fd()`

- **Signature**: `handle_type fd() const`
- **Description**: Returns the file descriptor associated with the file handle. This provides access to the underlying file system resource.
- **Parameters**: None.
- **Return Value**: `handle_type`: The file descriptor. Returns an invalid descriptor if the file is not open.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
file_mapping_handle mapping(file, open_mode::read_only, 1024);
handle_type fd = mapping.fd();
if (fd != invalid_fd) {
    // Use the file descriptor with POSIX functions
}
```
- **Preconditions**: The object must be valid and constructed.
- **Postconditions**: The returned file descriptor is valid if the file is open.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `handle()`

## Class: `file_mapping`

### `file_mapping(file_handle file, open_mode_t mode, std::int64_t file_size, std::shared_ptr<std::mutex> open_unmap_lock = nullptr)`

- **Signature**: `file_mapping(file_handle file, open_mode_t mode, std::int64_t file_size, std::shared_ptr<std::mutex> open_unmap_lock = nullptr)`
- **Description**: Constructs a `file_mapping` object that manages a memory-mapped file. The object can be shared among multiple threads if needed, thanks to the optional mutex for synchronization.
- **Parameters**:
  - `file` (file_handle): The file handle to map. Must be valid and opened with appropriate permissions.
  - `mode` (open_mode_t): The access mode for the file (read-only, read-write, etc.).
  - `file_size` (std::int64_t): The size of the file to map in bytes. Must be non-negative.
  - `open_unmap_lock` (std::shared_ptr<std::mutex>): Optional mutex to synchronize access to the file mapping operations (open and unmap). This is useful in multi-threaded environments.
- **Return Value**: None (constructor).
- **Exceptions/Errors**:
  - `std::runtime_error`: Thrown if the memory mapping fails (e.g., insufficient memory, file not found, or permission issues).
- **Example**:
```cpp
file_handle file = open_file("example.txt", open_mode::read_write);
std::shared_ptr<std::mutex> lock = std::make_shared<std::mutex>();
file_mapping mapping(file, open_mode::read_write, 1024, lock);
```
- **Preconditions**: The file handle must be valid and opened with the correct mode.
- **Postconditions**: The object is constructed with a valid memory mapping if successful.
- **Thread Safety**: Thread-safe if the mutex is provided.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `~file_mapping()`, `fd()`, `has_memory_map()`

### `file_mapping(file_mapping const&) = delete`

- **Signature**: `file_mapping(file_mapping const&) = delete`
- **Description**: Deleted copy constructor prevents copying of `file_mapping` objects. This ensures that memory mappings are not duplicated, which could lead to resource conflicts.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: None.
- **Example**: This function cannot be called directly as it's deleted.
- **Preconditions**: None.
- **Postconditions**: None.
- **Thread Safety**: Not applicable.
- **Complexity**: O(1).
- **See Also**: `operator=`

### `fd()`

- **Signature**: `handle_type fd() const`
- **Description**: Returns the file descriptor associated with the file handle. This provides access to the underlying file system resource.
- **Parameters**: None.
- **Return Value**: `handle_type`: The file descriptor. Returns an invalid descriptor if the file is not open.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
file_mapping mapping(file, open_mode::read_only, 1024);
handle_type fd = mapping.fd();
if (fd != invalid_fd) {
    // Use the file descriptor with POSIX functions
}
```
- **Preconditions**: The object must be valid and constructed.
- **Postconditions**: The returned file descriptor is valid if the file is open.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `handle()`

### `has_memory_map()`

- **Signature**: `bool has_memory_map() const`
- **Description**: Checks whether a memory mapping has been established for this file. This is useful for determining if the file is currently mapped into memory.
- **Parameters**: None.
- **Return Value**: `bool`: Returns `true` if a memory mapping exists, `false` otherwise.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
file_mapping mapping(file, open_mode::read_only, 1024);
if (mapping.has_memory_map()) {
    // Memory mapping exists, proceed with operations
}
```
- **Preconditions**: The object must be valid and constructed.
- **Postconditions**: The returned value indicates the presence of a memory mapping.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `range()`, `has_memory_map()`

### `range()`

- **Signature**: `span<byte> range()`
- **Description**: Returns a span representing the memory-mapped range of the file. This allows direct access to the mapped memory region.
- **Parameters**: None.
- **Return Value**: `span<byte>`: A span pointing to the mapped memory region. The span is valid only if a memory mapping exists.
- **Exceptions/Errors**: 
  - `std::logic_error`: Thrown if the memory mapping does not exist (i.e., `has_memory_map()` returns `false`).
- **Example**:
```cpp
file_mapping mapping(file, open_mode::read_only, 1024);
if (mapping.has_memory_map()) {
    span<byte> data = mapping.range();
    // Use the data span
}
```
- **Preconditions**: The object must be valid and constructed, and a memory mapping must exist (`has_memory_map()` must return `true`).
- **Postconditions**: The returned span points to the mapped memory region.
- **Thread Safety**: Thread-safe if the memory mapping is not modified.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `has_memory_map()`, `fd()`

## Usage Examples

### Basic Usage
```cpp
#include "libtorrent/aux_/mmap.hpp"
#include "libtorrent/file.hpp"

int main() {
    // Open a file
    file_handle file = open_file("example.txt", open_mode::read_only);
    
    // Create a memory-mapped file
    file_mapping mapping(file, open_mode::read_only, 1024);
    
    // Access the mapped memory
    if (mapping.has_memory_map()) {
        span<byte> data = mapping.range();
        // Process the data
    }
    
    return 0;
}
```

### Error Handling
```cpp
#include "libtorrent/aux_/mmap.hpp"
#include "libtorrent/file.hpp"

int main() {
    try {
        file_handle file = open_file("example.txt", open_mode::read_only);
        if (!file.is_open()) {
            std::cerr << "Failed to open file" << std::endl;
            return 1;
        }
        
        file_mapping mapping(file, open_mode::read_only, 1024);
        
        if (!mapping.has_memory_map()) {
            std::cerr << "Failed to create memory mapping" << std::endl;
            return 1;
        }
        
        span<byte> data = mapping.range();
        // Process the data
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```

### Edge Cases
```cpp
#include "libtorrent/aux_/mmap.hpp"
#include "libtorrent/file.hpp"

int main() {
    // Case 1: File size is zero
    file_handle file = open_file("empty.txt", open_mode::read_only);
    file_mapping mapping(file, open_mode::read_only, 0);
    
    if (mapping.has_memory_map()) {
        span<byte> data = mapping.range();
        // data will be empty but valid
    }
    
    // Case 2: File does not exist
    try {
        file_handle file = open_file("nonexistent.txt", open_mode::read_only);
        file_mapping mapping(file, open_mode::read_only, 1024);
    } catch (const std::exception& e) {
        std::cerr << "File not found: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Best Practices

1. **Always check `has_memory_map()` before using `range()`**: Ensure the memory mapping exists before accessing the mapped memory.

2. **Use RAII for resource management**: Let the destructors handle cleanup of file mappings and file handles.

3. **Check file open status**: Always verify that the file was successfully opened before creating a mapping.

4. **Use appropriate file modes**: Ensure the open mode matches your intended operations (read-only vs read-write).

5. **Handle exceptions properly**: Wrap file operations in try-catch blocks to handle potential errors gracefully.

6. **Consider thread safety**: If using the mapping in multiple threads, ensure proper synchronization with the provided mutex.

## Code Review & Improvement Suggestions

### `file_mapping_handle(file_mapping_handle const&) = delete`

- **Function**: `file_mapping_handle(file_mapping_handle const&) = delete`
- **Issue**: The function is correctly deleted but could be more explicitly documented.
- **Severity**: Low
- **Impact**: Minimal
- **Fix**: Add a comment explaining why copying is prohibited:
```cpp
// Deleted copy constructor to prevent duplication of memory mappings
file_mapping_handle(file_mapping_handle const&) = delete;
```

### `handle()`

- **Function**: `handle()`
- **Issue**: The function name `handle()` is ambiguous as it could refer to either the file handle or the memory mapping handle.
- **Severity**: Medium
- **Impact**: Potential confusion for users
- **Fix**: Rename to `memory_mapping_handle()` for clarity:
```cpp
HANDLE memory_mapping_handle() const { return m_mapping; }
```

### `fd()`

- **Function**: `fd()`
- **Issue**: The function name `fd()` is too short and could be confused with other file descriptor operations.
- **Severity**: Medium
- **Impact**: Potential confusion for users
- **Fix**: Rename to `file_descriptor()` for clarity:
```cpp
handle_type file_descriptor() const { return m_file.fd(); }
```

### `range()`

- **Function**: `range()`
- **Issue**: The function name `range()` is too generic and could be confused with other range-related operations.
- **Severity**: Medium
- **Impact**: Potential confusion for users
- **Fix**: Rename to `mapped_range()` for clarity:
```cpp
span<byte> mapped_range() {
    TORRENT_ASSERT(m_mapping);
    return { static_cast<byte*>(m_mapping), static_cast<std::ptrdiff_t>(m_size) };
}
```

## Modernization Opportunities

1. **Use `[[nodiscard]]` for functions that return important values**:
```cpp
[[nodiscard]] span<byte> mapped_range();
```

2. **Use `std::span` for array parameters**:
```cpp
bool process_data(std::span<const byte> data);
```

3. **Use `constexpr` for compile-time evaluation**:
```cpp
constexpr std::int64_t MAX_FILE_SIZE = 1024 * 1024 * 1024;
```

4. **Use C++20 concepts for template constraints**:
```cpp
template <std::ranges::range Range>
void process_range(Range&& r);
```

5. **Use `std::expected` (C++23) for error handling**:
```cpp
std::expected<file_mapping, error_code> create_mapping(file_handle file, open_mode_t mode, std::int64_t size);
```

## Refactoring Suggestions

1. **Split `file_mapping` into separate classes for mapping and file operations**:
   - `MemoryMapping` class for memory mapping operations
   - `FileOperations` class for file system operations

2. **Move `file_mapping_handle` and `file_mapping` into a utility namespace**:
```cpp
namespace libtorrent::util {
    class memory_mapping;
    class file_mapping_handle;
}
```

3. **Combine similar functions**: The `handle()` and `fd()` functions could be combined into a single function with different return types.

## Performance Optimizations

1. **Use move semantics**: Ensure the class supports move operations for efficient transfers.
2. **Return by value for RVO**: Return `span<byte>` by value to enable return value optimization.
3. **Use `std::string_view` for read-only strings**: If any string parameters are used, consider using `std::string_view`.
4. **Add `noexcept` where applicable**: Mark functions that don't throw exceptions as `noexcept`.