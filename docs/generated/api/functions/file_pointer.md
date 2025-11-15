# libtorrent File Pointer API Documentation

## file_pointer()

- **Signature**: `file_pointer()`
- **Description**: Default constructor for the `file_pointer` class. Initializes the file pointer to `nullptr`, indicating no file is currently open.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_pointer fp;
// fp is now initialized with nullptr
```
- **Preconditions**: None
- **Postconditions**: The `file_pointer` object is in a valid state with `ptr` set to `nullptr`
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `file_pointer(FILE*)`, `~file_pointer()`

## file_pointer()

- **Signature**: `explicit file_pointer(FILE* p)`
- **Description**: Constructor that takes an existing `FILE*` pointer and wraps it in a `file_pointer` object. The constructor is explicit to prevent implicit conversions from `FILE*` to `file_pointer`.
- **Parameters**:
  - `p` (FILE*): The file pointer to wrap. Must be a valid file pointer obtained from `fopen()`. Cannot be `nullptr`.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
FILE* file = fopen("example.txt", "r");
if (file) {
    file_pointer fp(file);
    // Use fp to manage the file
}
```
- **Preconditions**: `p` must be a valid, non-null file pointer
- **Postconditions**: The `file_pointer` object owns the provided `FILE*` pointer
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `~file_pointer()`, `file()`

## file_pointer()

- **Signature**: `~file_pointer()`
- **Description**: Destructor that ensures the wrapped file pointer is properly closed when the `file_pointer` object goes out of scope. If the file pointer is not `nullptr`, `::fclose()` is called to close the file.
- **Parameters**: None
- **Return Value**: None (destructor)
- **Exceptions/Errors**: None (but `::fclose()` may fail and set errno)
- **Example**:
```cpp
{
    file_pointer fp(fopen("example.txt", "r"));
    // File is automatically closed when fp goes out of scope
}
```
- **Preconditions**: None
- **Postconditions**: The file pointed to by `ptr` is closed if it was open
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `file()`, `~file_pointer()`

## file_pointer()

- **Signature**: `file_pointer(file_pointer const&) = delete;`
- **Description**: Deleted copy constructor prevents copying of `file_pointer` objects. This is to avoid double-closing of the same file pointer when a copy is made.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None (compilation error if attempted)
- **Example**:
```cpp
// This will cause a compilation error:
// file_pointer fp1(fopen("example.txt", "r"));
// file_pointer fp2 = fp1; // Error: copy constructor deleted
```
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `file_pointer(file_pointer&&)`, `operator=()`

## file_pointer()

- **Signature**: `file_pointer(file_pointer&& f)`
- **Description**: Move constructor that transfers ownership of the file pointer from the source object to the new object. The source object's pointer is set to `nullptr` to prevent double-closing.
- **Parameters**:
  - `f` (file_pointer&&): The source object whose file pointer will be moved. This is an rvalue reference.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_pointer fp1(fopen("example.txt", "r"));
file_pointer fp2(std::move(fp1)); // fp1's file pointer is moved to fp2
// fp1 now has ptr = nullptr
```
- **Preconditions**: `f` must be a valid `file_pointer` object
- **Postconditions**: The new `file_pointer` object owns the file pointer, and the source object's pointer is set to `nullptr`
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `operator=()`, `file_pointer(file_pointer const&)`

## swap()

- **Signature**: `file_pointer& operator=(file_pointer&& f)`
- **Description**: Move assignment operator that transfers ownership of the file pointer from the source object to the current object. The source object's pointer is swapped with the current object's pointer, and the source object's pointer is set to `nullptr`.
- **Parameters**:
  - `f` (file_pointer&&): The source object whose file pointer will be moved. This is an rvalue reference.
- **Return Value**: Reference to the current object (`*this`)
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_pointer fp1(fopen("example.txt", "r"));
file_pointer fp2;
fp2 = std::move(fp1); // fp1's file pointer is moved to fp2
// fp1 now has ptr = nullptr
```
- **Preconditions**: `f` must be a valid `file_pointer` object
- **Postconditions**: The current object owns the file pointer from the source object, and the source object's pointer is set to `nullptr`
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `file_pointer(file_pointer&&)`, `swap()`

## file()

- **Signature**: `FILE* file() const`
- **Description**: Returns the underlying `FILE*` pointer that this `file_pointer` object manages. This allows direct access to the file pointer when needed.
- **Parameters**: None
- **Return Value**: The underlying `FILE*` pointer. Returns `nullptr` if the file pointer is not open.
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_pointer fp(fopen("example.txt", "r"));
FILE* raw_file = fp.file();
if (raw_file != nullptr) {
    // Use raw_file directly
    fread(buffer, 1, size, raw_file);
}
```
- **Preconditions**: None
- **Postconditions**: Returns the current file pointer, or `nullptr` if none is set
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `file_pointer()`, `~file_pointer()`

## portable_fseeko()

- **Signature**: `inline int portable_fseeko(FILE* const f, std::int64_t const offset, int const whence)`
- **Description**: Portable implementation of `fseeko` that works across different platforms. This function attempts to seek to a specific position in a file, using the appropriate system call based on the platform.
- **Parameters**:
  - `f` (FILE* const): The file pointer to seek within. Must be a valid, open file pointer.
  - `offset` (std::int64_t const): The offset to seek to, in bytes. Can be positive (forward), negative (backward), or zero.
  - `whence` (int const): The reference point for the offset. Can be `SEEK_SET`, `SEEK_CUR`, or `SEEK_END`.
- **Return Value**: Returns 0 on success, -1 on failure. The actual return values depend on the underlying implementation.
- **Exceptions/Errors**: 
  - If the file pointer is invalid or closed, the function may fail
  - If the offset is too large or invalid, the function may fail
  - The underlying system call may set `errno` on error
- **Example**:
```cpp
FILE* file = fopen("example.txt", "r");
if (file) {
    // Seek to position 100 from the beginning of the file
    int result = portable_fseeko(file, 100, SEEK_SET);
    if (result == 0) {
        // Seek successful
        fread(buffer, 1, size, file);
    } else {
        // Seek failed
        perror("fseeko");
    }
    fclose(file);
}
```
- **Preconditions**: 
  - `f` must be a valid, open file pointer
  - `offset` must be within the valid range for the file
  - `whence` must be one of the standard constants: `SEEK_SET`, `SEEK_CUR`, or `SEEK_END`
- **Postconditions**: The file position indicator is set to the specified position, or remains unchanged if the function fails
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `fseeko()`, `lseek64()`, `_fseeki64()`

## Usage Examples

### Basic Usage

```cpp
#include <libtorrent/aux_/file_pointer.hpp>
#include <cstdio>

int main() {
    // Create a file pointer and open a file
    FILE* file = fopen("example.txt", "r");
    if (file) {
        // Wrap the file pointer in a file_pointer object
        libtorrent::aux::file_pointer fp(file);
        
        // Use the file pointer to read data
        char buffer[1024];
        size_t bytes_read = fread(buffer, 1, sizeof(buffer), fp.file());
        
        // The file pointer will be automatically closed when fp goes out of scope
    }
    
    return 0;
}
```

### Error Handling

```cpp
#include <libtorrent/aux_/file_pointer.hpp>
#include <cstdio>
#include <iostream>

int main() {
    // Attempt to open a file
    FILE* file = fopen("nonexistent.txt", "r");
    if (file == nullptr) {
        std::cerr << "Failed to open file" << std::endl;
        return 1;
    }
    
    // Wrap the file pointer
    libtorrent::aux::file_pointer fp(file);
    
    // Check if we can seek to the end of the file
    int result = portable_fseeko(fp.file(), 0, SEEK_END);
    if (result == -1) {
        std::cerr << "Failed to seek to end of file" << std::endl;
        return 1;
    }
    
    // Get the file size
    long file_size = ftell(fp.file());
    if (file_size == -1) {
        std::cerr << "Failed to get file size" << std::endl;
        return 1;
    }
    
    // Reset to beginning of file
    result = portable_fseeko(fp.file(), 0, SEEK_SET);
    if (result == -1) {
        std::cerr << "Failed to reset file position" << std::endl;
        return 1;
    }
    
    // Read data
    char buffer[1024];
    size_t bytes_read = fread(buffer, 1, sizeof(buffer), fp.file());
    if (bytes_read == 0 && ferror(fp.file())) {
        std::cerr << "Failed to read from file" << std::endl;
        return 1;
    }
    
    // The file pointer will be automatically closed when fp goes out of scope
    return 0;
}
```

### Edge Cases

```cpp
#include <libtorrent/aux_/file_pointer.hpp>
#include <cstdio>
#include <iostream>

int main() {
    // Test with zero-length file
    FILE* zero_file = fopen("zero.txt", "w");
    if (zero_file) {
        fclose(zero_file);
    }
    
    zero_file = fopen("zero.txt", "r");
    if (zero_file) {
        libtorrent::aux::file_pointer fp(zero_file);
        long size = ftell(fp.file());
        if (size == -1) {
            std::cerr << "Failed to get size of zero-length file" << std::endl;
        } else {
            std::cout << "Zero-length file size: " << size << std::endl;
        }
    }
    
    // Test with very large file
    const long long large_offset = 1000000000LL; // 1GB
    FILE* large_file = fopen("large.txt", "wb");
    if (large_file) {
        // Write some data to create a large file
        char buffer[1024];
        for (int i = 0; i < 1000; ++i) {
            fwrite(buffer, 1, sizeof(buffer), large_file);
        }
        fclose(large_file);
        
        large_file = fopen("large.txt", "rb");
        if (large_file) {
            libtorrent::aux::file_pointer fp(large_file);
            
            // Try to seek to a large offset
            int result = portable_fseeko(fp.file(), large_offset, SEEK_SET);
            if (result == 0) {
                std::cout << "Successfully sought to offset " << large_offset << std::endl;
            } else {
                std::cerr << "Failed to seek to offset " << large_offset << std::endl;
            }
        }
    }
    
    return 0;
}
```

## Best Practices

1. **Always use RAII**: Use `file_pointer` objects to manage file pointers, as they automatically close files when they go out of scope.

2. **Check file opening**: Always check if `fopen()` succeeds before wrapping a file pointer.

3. **Use move semantics**: Use `std::move()` when transferring ownership of file pointers between objects.

4. **Avoid direct FILE* manipulation**: Prefer using `file_pointer` methods instead of directly accessing the `FILE*` pointer when possible.

5. **Handle seek errors**: Always check the return value of `portable_fseeko()` and handle errors appropriately.

6. **Use the portable version**: Use `portable_fseeko()` instead of platform-specific functions like `fseeko()` or `_fseeki64()` for cross-platform compatibility.

7. **Check file position**: Use `ftell()` or `fseek()` to check file positions when needed.

8. **Close files explicitly**: If you need to close a file before the `file_pointer` object goes out of scope, use `fclose()` or `std::fclose()` on the `FILE*` pointer.

## Code Review & Improvement Suggestions

### file_pointer()

- **Function**: `file_pointer()`
- **Issue**: Missing explicit keyword for the default constructor
- **Severity**: Low
- **Impact**: Could potentially allow implicit conversions
- **Fix**: Add explicit keyword if needed, though this is typically not necessary for default constructors

### file_pointer()

- **Function**: `explicit file_pointer(FILE* p)`
- **Issue**: No null pointer check
- **Severity**: Medium
- **Impact**: Could lead to undefined behavior if a null pointer is passed
- **Fix**: Add a null pointer check and handle the error case
```cpp
explicit file_pointer(FILE* p) : ptr(p) {
    if (p == nullptr) {
        throw std::invalid_argument("Cannot create file_pointer with null pointer");
    }
}
```

### file_pointer()

- **Function**: `~file_pointer()`
- **Issue**: No error checking on fclose()
- **Severity**: Medium
- **Impact**: fclose() might fail, and the error would be silently ignored
- **Fix**: Check return value of fclose() and handle errors
```cpp
~file_pointer() {
    if (ptr != nullptr) {
        if (::fclose(ptr) != 0) {
            // Handle error, perhaps log it or throw
            // Note: this is a rare case and usually not worth crashing
        }
    }
}
```

### file_pointer()

- **Function**: `file_pointer(file_pointer&& f)`
- **Issue**: No move assignment operator documented
- **Severity**: Medium
- **Impact**: Users might not know about move assignment
- **Fix**: Document the move assignment operator and consider adding a move constructor if needed
```cpp
file_pointer& operator=(file_pointer&& f) {
    if (this != &f) {
        if (ptr != nullptr) {
            ::fclose(ptr);
        }
        ptr = f.ptr;
        f.ptr = nullptr;
    }
    return *this;
}
```

### swap()

- **Function**: `file_pointer& operator=(file_pointer&& f)`
- **Issue**: Name should be `operator=` instead of `swap()`
- **Severity**: High
- **Impact**: Misleading name, could cause confusion
- **Fix**: Rename the function to `operator=`
```cpp
file_pointer& operator=(file_pointer&& f) {
    std::swap(ptr, f.ptr);
    return *this;
}
```

### file()

- **Function**: `FILE* file() const`
- **Issue**: No null pointer check
- **Severity**: Low
- **Impact**: Could return a null pointer, but this is expected behavior
- **Fix**: Document that null pointer may be returned
```cpp
FILE* file() const {
    return ptr;
}
```

### portable_fseeko()

- **Function**: `portable_fseeko()`
- **Issue**: Incomplete implementation in the code provided
- **Severity**: Critical
- **Impact**: The function is not complete and won't compile
- **Fix**: Complete the implementation
```cpp
inline int portable_fseeko(FILE* const f, std::int64_t const offset, int const whence)
{
#ifdef TORRENT_WINDOWS
    return ::_fseeki64(f, offset, whence);
#elif TORRENT_HAS_FSEEKO
    return ::fseeko(f, offset, whence);
#else
    int const fd = ::fileno(f);
    return ::lseek64(fd, offset, whence) == -1 ? -1 : 0;
#endif
}
```

## Modernization Opportunities

### Add [[nodiscard]] attributes

```cpp
// Add to file_pointer constructors and destructor
[[nodiscard]] explicit file_pointer(FILE* p);
[[nodiscard]] ~file_pointer();
```

### Add constexpr for compile-time evaluation

