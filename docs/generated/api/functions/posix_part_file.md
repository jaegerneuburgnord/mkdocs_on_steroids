# API Documentation

## posix_part_file

- **Signature**: `posix_part_file(std::string path, std::string name, int num_pieces, int piece_size)`
- **Description**: Constructs a new `posix_part_file` object that represents a partial file on the filesystem. This object manages a file that can store data for a specific number of pieces, each of a specified size. The file is created at the given path with the provided name. The constructor initializes the file structure and prepares it for writing piece data.
- **Parameters**:
  - `path` (std::string): The directory path where the part file will be created. This must be a valid directory path that the application has write permissions to. The path should not contain special characters that could cause filesystem issues.
  - `name` (std::string): The filename for the part file. This should be a valid filename without path separators. The name will be used as the base name for the file.
  - `num_pieces` (int): The number of pieces that the part file can store. This must be a positive integer. The total file size will be calculated as `num_pieces * piece_size + header_size`.
  - `piece_size` (int): The size of each piece in bytes. This must be a positive integer that aligns with the filesystem block size for optimal performance.
- **Return Value**:
  - This is a constructor and does not return a value in the traditional sense. It constructs and initializes the `posix_part_file` object.
- **Exceptions/Errors**:
  - Throws `std::runtime_error` if the file cannot be created due to insufficient permissions, invalid path, or disk full.
  - Throws `std::bad_alloc` if memory allocation fails during object construction.
  - Throws `std::invalid_argument` if `num_pieces` or `piece_size` are non-positive.
- **Example**:
```cpp
try {
    posix_part_file file("/tmp/torrent_data", "file.part", 100, 1048576);
    // File is now ready for writing
} catch (const std::exception& e) {
    std::cerr << "Failed to create part file: " << e.what() << std::endl;
}
```
- **Preconditions**:
  - The application must have write permissions to the specified path.
  - The `path` must be a valid directory.
  - `num_pieces` and `piece_size` must be positive integers.
- **Postconditions**:
  - The `posix_part_file` object is fully constructed and ready for use.
  - A file with the specified name exists at the specified path.
  - The file has sufficient space allocated for the specified number of pieces.
- **Thread Safety**: This function is not thread-safe. Multiple threads should not call this constructor simultaneously on the same file.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `~posix_part_file()`, `write()`

## slot_offset

- **Signature**: `std::int64_t slot_offset(slot_index_t const slot) const`
- **Description**: Calculates the offset in bytes from the beginning of the part file where the data for a specific slot should be written. This function takes a slot index and returns the byte offset where the slot's data begins, accounting for both the header size and the piece size. This is used internally to determine where to write data for each piece in the file.
- **Parameters**:
  - `slot` (slot_index_t const): The slot index for which to calculate the offset. This must be a valid slot index that corresponds to a piece in the file. The value should be non-negative and less than the total number of pieces.
- **Return Value**:
  - Returns the byte offset as `std::int64_t`. The offset is calculated as `slot * piece_size + header_size`. The value will always be non-negative and will be in the range [header_size, header_size + num_pieces * piece_size).
- **Exceptions/Errors**:
  - This function does not throw exceptions under normal circumstances. However, if `slot` is invalid (e.g., negative or greater than the maximum number of slots), it may result in undefined behavior or incorrect offset calculation.
- **Example**:
```cpp
posix_part_file file("/tmp/torrent_data", "file.part", 100, 1048576);
std::int64_t offset = file.slot_offset(42);
std::cout << "Offset for slot 42: " << offset << " bytes" << std::endl;
```
- **Preconditions**:
  - The `posix_part_file` object must be properly constructed and initialized.
  - The `slot` parameter must be a valid slot index within the range of available pieces.
- **Postconditions**:
  - The returned offset is correct for the given slot index.
  - The calculation is consistent with the file's internal structure.
- **Thread Safety**: This function is thread-safe as long as the `posix_part_file` object is not being modified concurrently.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `posix_part_file()`, `write()`

## Usage Examples

### Basic Usage
```cpp
#include <libtorrent/aux_/posix_part_file.hpp>
#include <iostream>

int main() {
    try {
        // Create a part file with 100 pieces of 1MB each
        posix_part_file file("/tmp/torrent_data", "example.part", 100, 1048576);
        
        // Get the offset for slot 0 (first piece)
        std::int64_t offset = file.slot_offset(0);
        std::cout << "Offset for first piece: " << offset << " bytes" << std::endl;
        
        // Write data to the file (assuming we have data to write)
        // file.write(...);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

### Error Handling
```cpp
#include <libtorrent/aux_/posix_part_file.hpp>
#include <iostream>
#include <fstream>

int main() {
    std::string path = "/tmp/torrent_data";
    std::string name = "error_test.part";
    int num_pieces = 50;
    int piece_size = 524288; // 512KB
    
    try {
        // Try to create the part file
        posix_part_file file(path, name, num_pieces, piece_size);
        
        // Verify the file was created
        std::ifstream check_file(path + "/" + name);
        if (!check_file.is_open()) {
            std::cerr << "Failed to verify file creation" << std::endl;
            return 1;
        }
        
        // Test slot offset calculation
        for (int i = 0; i < num_pieces; ++i) {
            std::int64_t offset = file.slot_offset(i);
            if (offset < 0) {
                std::cerr << "Invalid offset for slot " << i << std::endl;
                return 1;
            }
        }
        
        std::cout << "Successfully created and verified part file" << std::endl;
        
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime error: " << e.what() << std::endl;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Unknown exception: " << e.what() << std::endl;
    }
    
    return 0;
}
```

### Edge Cases
```cpp
#include <libtorrent/aux_/posix_part_file.hpp>
#include <iostream>
#include <vector>

int main() {
    try {
        // Test with minimum values
        posix_part_file small_file("/tmp", "small.part", 1, 1);
        std::cout << "Minimum file created successfully" << std::endl;
        
        // Test with maximum values (theoretical)
        const int MAX_PIECES = 1000000;
        const int MAX_PIECE_SIZE = 1048576; // 1MB
        
        // This might fail due to memory constraints, but we'll test the calculation
        posix_part_file large_file("/tmp", "large.part", MAX_PIECES, MAX_PIECE_SIZE);
        
        // Check slot offset calculation for maximum values
        std::int64_t max_offset = large_file.slot_offset(MAX_PIECES - 1);
        if (max_offset < 0) {
            std::cout << "Maximum offset calculation failed" << std::endl;
        } else {
            std::cout << "Maximum offset: " << max_offset << " bytes" << std::endl;
        }
        
        // Test with edge slot values
        for (int slot : {0, MAX_PIECES - 1, MAX_PIECES}) {
            try {
                std::int64_t offset = large_file.slot_offset(slot);
                if (slot == MAX_PIECES) {
                    // This should be out of bounds
                    std::cout << "Unexpectedly got offset for slot " << slot << std::endl;
                } else {
                    std::cout << "Offset for slot " << slot << ": " << offset << std::endl;
                }
            } catch (const std::exception& e) {
                std::cout << "Error calculating offset for slot " << slot << ": " << e.what() << std::endl;
            }
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Edge case test failed: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Best Practices

### Usage Tips
- Always check for exceptions when creating a `posix_part_file` object.
- Use meaningful names for the part file to help with debugging and file management.
- Consider the total file size when determining `num_pieces` and `piece_size` to avoid exceeding disk space.
- Use the `slot_offset` function to determine where to write data for each piece.
- Keep track of the file's current state and ensure operations are performed in the correct order.

### Common Mistakes to Avoid
- **Invalid parameters**: Never pass negative values for `num_pieces` or `piece_size`.
- **Missing error handling**: Always wrap file creation in try-catch blocks to handle potential exceptions.
- **Concurrent access**: Avoid multiple threads accessing the same `posix_part_file` object simultaneously without proper synchronization.
- **Ignoring return values**: While this constructor doesn't return a value, ensure you're not expecting a return value in other contexts.

### Performance Tips
- Pre-calculate offsets when processing multiple pieces to avoid redundant calculations.
- Use appropriate piece sizes that align with filesystem block sizes for optimal performance.
- Consider the impact of `num_pieces` on memory usage, especially for very large files.
- Use `std::string_view` or similar types if you're passing the same path and name repeatedly.

## Code Review & Improvement Suggestions

### Modernization Opportunities

```markdown
**Function**: `posix_part_file`
**Issue**: The function signature uses `std::string` for path and name parameters, which can lead to unnecessary string copying.
**Severity**: Medium
**Impact**: Performance overhead due to string copying, especially when creating multiple part files.
**Fix**: Use `std::string_view` for read-only string parameters:
```cpp
posix_part_file(std::string_view path, std::string_view name, int num_pieces, int piece_size);
```

**Function**: `slot_offset`
**Issue**: The function returns `std::int64_t` but the calculation involves `int` types that could overflow for large values.
**Severity**: Medium
**Impact**: Potential integer overflow leading to incorrect offset calculation.
**Fix**: Use `std::int64_t` for the `slot` parameter and ensure the calculation uses appropriate types:
```cpp
std::int64_t slot_offset(std::int64_t slot) const
```

**Function**: `posix_part_file`
**Issue**: The function signature doesn't indicate that it might throw exceptions.
**Severity**: Medium
**Impact**: Developers might not expect exceptions and fail to handle them properly.
**Fix**: Use the `[[nodiscard]]` attribute and consider adding a noexcept specifier if applicable:
```cpp
[[nodiscard]] posix_part_file(std::string_view path, std::string_view name, int num_pieces, int piece_size);
```

### Refactoring Suggestions

**Function**: `posix_part_file`
**Issue**: The class has multiple responsibilities: file management, offset calculation, and data writing.
**Severity**: High
**Impact**: This violates the Single Responsibility Principle, making the class harder to test and maintain.
**Fix**: Consider splitting the functionality into separate classes:
```cpp
// Separate file management from offset calculation
class PartFile {
public:
    PartFile(std::string_view path, std::string_view name, int num_pieces, int piece_size);
    ~PartFile();
    // File management methods
};

class SlotOffsetCalculator {
public:
    SlotOffsetCalculator(int piece_size, int header_size);
    std::int64_t calculate(slot_index_t const slot) const;
private:
    int m_piece_size;
    int m_header_size;
};
```

### Performance Optimizations

**Function**: `posix_part_file`
**Issue**: The constructor creates a file without pre-allocating space, which can lead to fragmentation.
**Severity**: Low
**Impact**: Potential performance degradation for large files due to file fragmentation.
**Fix**: Pre-allocate file space to improve performance:
```cpp
posix_part_file(std::string_view path, std::string_view name, int num_pieces, int piece_size) {
    // Create the file
    std::ofstream file(path + "/" + name, std::ios::binary | std::ios::out);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to create file");
    }
    
    // Pre-allocate space for all pieces
    file.seekp((num_pieces * piece_size + header_size) - 1);
    file.put(0);
    file.close();
}
```

**Function**: `slot_offset`
**Issue**: The calculation is done at runtime, which could be optimized for repeated calls.
**Severity**: Low
**Impact**: Minor performance impact for applications that call this function frequently.
**Fix**: Consider caching results if the same slot indices are queried repeatedly:
```cpp
class SlotOffsetCalculator {
public:
    // ... existing constructor
    std::int64_t calculate(slot_index_t const slot) const {
        // Check cache first
        auto it = m_cache.find(slot);
        if (it != m_cache.end()) {
            return it->second;
        }
        
        // Calculate and cache the result
        std::int64_t result = static_cast<int>(slot) * static_cast<std::int64_t>(m_piece_size) + m_header_size;
        m_cache[slot] = result;
        return result;
    }
private:
    std::unordered_map<slot_index_t, std::int64_t> m_cache;
};
```

### Modernization Opportunities (Enhanced)

```markdown
**Function**: `posix_part_file`
**Issue**: The function signature doesn't use modern C++ features like `std::string_view` or `std::span`.
**Severity**: Medium
**Impact**: Reduced performance and increased memory usage due to unnecessary string copies.
**Fix**: Modernize the interface:
```cpp
class posix_part_file {
public:
    posix_part_file(std::string_view path, std::string_view name, int num_pieces, int piece_size);
    // ... rest of the interface
};

**Function**: `slot_offset`
**Issue**: The function doesn't use `std::span` for array parameters, though it doesn't have any array parameters.
**Severity**: Low
**Impact**: No direct impact, but keeping the interface modern is beneficial.
**Fix**: Ensure the interface is consistent with modern C++ practices:
```cpp
std::int64_t slot_offset(slot_index_t const slot) const noexcept;
```