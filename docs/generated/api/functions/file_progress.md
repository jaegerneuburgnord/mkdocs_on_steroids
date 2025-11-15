# libtorrent file_progress API Documentation

## file_progress

- **Signature**: `file_progress()`
- **Description**: Default constructor for the file_progress structure. Initializes an empty file_progress object with no file progress data.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_progress progress;
// progress is now initialized and ready for use
```
- **Preconditions**: None
- **Postconditions**: The file_progress object is in a valid initialized state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space
- **See Also**: `init()`, `export_progress()`

## file_progress

- **Signature**: `void init(piece_picker const& picker, file_storage const& fs)`
- **Description**: Initializes the file_progress object with data from a piece_picker and file_storage objects. This function sets up the internal state to track file progress based on the torrent's piece distribution and file layout.
- **Parameters**:
  - `picker` (piece_picker const&): The piece_picker object that contains information about which pieces are available and which are needed. This object must remain valid for the duration of the file_progress object's use.
  - `fs` (file_storage const&): The file_storage object that describes the layout of files in the torrent. This object must remain valid for the duration of the file_progress object's use.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_progress progress;
progress.init(picker, fs);
// Now progress contains the initialized file progress data
```
- **Preconditions**: 
  - The file_progress object must be constructed before calling this function
  - The `picker` and `fs` objects must be valid and remain valid
  - The `picker` must be associated with the same torrent as the `fs`
- **Postconditions**: 
  - The file_progress object is properly initialized
  - The internal state contains file progress information based on the provided picker and file storage
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time where n is the number of files, O(1) space
- **See Also**: `export_progress()`, `total_on_disk()`, `empty()`

## total_on_disk

- **Signature**: `std::int64_t total_on_disk() const`
- **Description**: Returns the total amount of data that has been written to disk for all files in the torrent. This value represents the sum of all bytes that have been successfully saved to disk for each file.
- **Parameters**: None
- **Return Value**: 
  - `std::int64_t`: The total number of bytes on disk across all files
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_progress progress;
// ... assume progress has been initialized
std::int64_t bytes_on_disk = progress.total_on_disk();
std::cout << "Total bytes on disk: " << bytes_on_disk << std::endl;
```
- **Preconditions**: 
  - The file_progress object must have been initialized with `init()`
  - The object must be in a valid state
- **Postconditions**: The function returns the current total bytes on disk
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `export_progress()`, `empty()`

## empty

- **Signature**: `bool empty() const`
- **Description**: Checks if there is any file progress data available. Returns true if no files have been written to disk or if the file_progress object has not been initialized.
- **Parameters**: None
- **Return Value**: 
  - `bool`: Returns `true` if no data has been written to disk, `false` otherwise
- **Exceptions/Errors**: None
- **Example**:
```cpp
file_progress progress;
if (progress.empty()) {
    std::cout << "No data has been written to disk yet" << std::endl;
}
```
- **Preconditions**: 
  - The file_progress object must have been initialized with `init()`
  - The object must be in a valid state
- **Postconditions**: Returns the current emptiness status of the file_progress object
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `init()`, `total_on_disk()`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/aux_/file_progress.hpp"
#include "libtorrent/piece_picker.hpp"
#include "libtorrent/file_storage.hpp"

void demonstrate_file_progress() {
    // Create necessary objects
    piece_picker picker;
    file_storage fs;
    
    // Initialize file_progress
    file_progress progress;
    progress.init(picker, fs);
    
    // Check progress
    if (!progress.empty()) {
        std::cout << "Total bytes on disk: " << progress.total_on_disk() << std::endl;
    } else {
        std::cout << "No data on disk yet" << std::endl;
    }
}
```

## Error Handling

```cpp
#include "libtorrent/aux_/file_progress.hpp"
#include "libtorrent/piece_picker.hpp"
#include "libtorrent/file_storage.hpp"

bool process_file_progress() {
    try {
        file_progress progress;
        piece_picker picker;
        file_storage fs;
        
        // Initialize with error checking
        if (!picker.is_valid() || !fs.is_valid()) {
            std::cerr << "Invalid picker or file storage" << std::endl;
            return false;
        }
        
        progress.init(picker, fs);
        
        // Check if progress is empty
        if (progress.empty()) {
            std::cout << "No files have been written to disk" << std::endl;
        } else {
            std::cout << "Files on disk: " << progress.total_on_disk() << " bytes" << std::endl;
        }
        
        return true;
    } catch (const std::exception& e) {
        std::cerr << "Error processing file progress: " << e.what() << std::endl;
        return false;
    }
}
```

## Edge Cases

```cpp
#include "libtorrent/aux_/file_progress.hpp"
#include "libtorrent/piece_picker.hpp"
#include "libtorrent/file_storage.hpp"

void demonstrate_edge_cases() {
    file_progress progress;
    
    // Case 1: Empty file storage
    file_storage empty_fs;
    piece_picker empty_picker;
    progress.init(empty_picker, empty_fs);
    std::cout << "Empty file storage result: " << progress.empty() << ", bytes on disk: " << progress.total_on_disk() << std::endl;
    
    // Case 2: Single file with no data
    file_storage single_file;
    single_file.add_file("test.txt", 1024);
    piece_picker single_picker;
    progress.init(single_picker, single_file);
    std::cout << "Single file with no data: " << progress.empty() << ", bytes on disk: " << progress.total_on_disk() << std::endl;
    
    // Case 3: Multiple files with some data
    file_storage multi_fs;
    multi_fs.add_file("file1.txt", 1024);
    multi_fs.add_file("file2.txt", 2048);
    piece_picker multi_picker;
    // Assume some pieces are downloaded
    progress.init(multi_picker, multi_fs);
    std::cout << "Multiple files with data: " << !progress.empty() << ", bytes on disk: " << progress.total_on_disk() << std::endl;
}
```

# Best Practices

## How to Use These Functions Effectively

1. **Initialize properly**: Always call `init()` with valid `piece_picker` and `file_storage` objects before using other functions.

2. **Check state**: Use `empty()` to determine if any data has been written to disk before performing operations.

3. **Use const-correctness**: Use `const` references where appropriate to avoid unnecessary copies.

4. **Error handling**: Check for invalid states in your picker and file storage objects before initialization.

5. **Memory management**: Ensure that the picker and file storage objects remain valid for the lifetime of the file_progress object.

## Common Mistakes to Avoid

1. **Using uninitialized objects**: Never call `total_on_disk()` or `empty()` before calling `init()`.

2. **Using expired objects**: Ensure that the `piece_picker` and `file_storage` objects remain valid.

3. **Ignoring return values**: While `total_on_disk()` and `empty()` don't return error codes, always check the state of your objects.

4. **Assuming order**: Don't assume that files are processed in a specific order unless you've verified it.

5. **Memory leaks**: Ensure that the file_progress object is destroyed when no longer needed.

## Performance Tips

1. **Avoid unnecessary initialization**: Only call `init()` when needed, not every time you need to check progress.

2. **Cache results**: If you need to check progress multiple times, store the result in a variable rather than calling the function repeatedly.

3. **Use const methods**: Use `total_on_disk()` and `empty()` as they are const and won't modify the object.

4. **Minimize function calls**: Consider storing the total on disk value if you need to access it frequently.

# Code Review & Improvement Suggestions

## Function: `file_progress()`

### Potential Issues

**Security:**
- None - constructor doesn't have security implications

**Performance:**
- None - constructor is simple and efficient

**Correctness:**
- None - constructor is straightforward

**Code Quality:**
- None - constructor is properly implemented

### Modernization Opportunities

- Add `[[nodiscard]]` attribute if the return value is important
- Add documentation for the default constructor

### Refactoring Suggestions

- No refactoring needed - constructor is properly designed

### Performance Optimizations

- No optimization needed - constructor is already optimal

## Function: `init()`

### Potential Issues

**Security:**
- None - function doesn't access external resources

**Performance:**
- None - function is efficient

**Correctness:**
- None - function properly initializes the object

**Code Quality:**
- None - function is well-implemented

### Modernization Opportunities

- Consider using `std::span` for the file_storage parameter if it's large
- Add `[[nodiscard]]` attribute to indicate the function's importance

### Refactoring Suggestions

- No refactoring needed - function is properly designed

### Performance Optimizations

- No optimization needed - function is already optimal

## Function: `total_on_disk()`

### Potential Issues

**Security:**
- None - function doesn't have security implications

**Performance:**
- None - function is efficient

**Correctness:**
- None - function properly returns the total on disk

**Code Quality:**
- None - function is well-implemented

### Modernization Opportunities

- Add `[[nodiscard]]` attribute to indicate the return value is important
- Consider adding a const reference parameter if the function could be optimized

### Refactoring Suggestions

- No refactoring needed - function is properly designed

### Performance Optimizations

- No optimization needed - function is already optimal

## Function: `empty()`

### Potential Issues

**Security:**
- None - function doesn't have security implications

**Performance:**
- None - function is efficient

**Correctness:**
- None - function properly checks emptiness

**Code Quality:**
- None - function is well-implemented

### Modernization Opportunities

- Add `[[nodiscard]]` attribute to indicate the return value is important
- Consider adding documentation for the function

### Refactoring Suggestions

- No refactoring needed - function is properly designed

### Performance Optimizations

- No optimization needed - function is already optimal