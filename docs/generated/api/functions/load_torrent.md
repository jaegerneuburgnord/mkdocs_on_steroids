# C++ API Documentation: Torrent Loading Functions

## Function: load_torrent_file1

- **Signature**: `lt::add_torrent_params load_torrent_file1(std::string filename, dict cfg)`
- **Description**: Loads a torrent file from the specified filename and returns an `add_torrent_params` object configured with the file's content and optional configuration settings. This function serves as a wrapper around the core `lt::load_torrent_file` function, allowing Python-style dictionary configuration.
- **Parameters**:
  - `filename` (std::string): The path to the torrent file to load. Must be a valid file path accessible by the application. The file must be a properly formatted .torrent file. The function will throw an exception if the file cannot be opened or is invalid.
  - `cfg` (dict): A dictionary containing configuration options for the torrent. This dictionary is converted to `lt::torrent_limits` using `dict_to_limits()` function. Valid keys and values depend on the specific `lt::torrent_limits` configuration options.
- **Return Value**:
  - Returns an `lt::add_torrent_params` object containing the parsed torrent data and configuration settings.
  - The returned object can be used directly with libtorrent functions to add the torrent to a session.
- **Exceptions/Errors**:
  - Throws `std::runtime_error` if the torrent file cannot be opened or is malformed.
  - Throws `std::invalid_argument` if the configuration dictionary contains invalid keys or values.
  - Throws `std::bad_alloc` if memory allocation fails.
- **Example**:
```cpp
try {
    auto params = load_torrent_file1("example.torrent", {"max_connections": 100, "max_upload_rate": 1000});
    // Use params to add torrent to session
} catch (const std::exception& e) {
    std::cerr << "Error loading torrent: " << e.what() << std::endl;
}
```
- **Preconditions**:
  - The `filename` must be a valid file path.
  - The file at the specified path must be a valid .torrent file.
  - The `cfg` dictionary must contain valid configuration keys.
- **Postconditions**:
  - Returns a valid `lt::add_torrent_params` object if the file was successfully loaded.
  - The function does not modify the input parameters.
- **Thread Safety**: The function is thread-safe as long as the underlying libtorrent library is thread-safe.
- **Complexity**: O(n) where n is the size of the torrent file, due to file reading and parsing operations.
- **See Also**: `lt::load_torrent_file`, `dict_to_limits`

## Function: load_torrent_buffer0

- **Signature**: `lt::add_torrent_params load_torrent_buffer0(bytes b)`
- **Description**: Loads a torrent from a byte buffer containing the torrent data. This function is designed for scenarios where the torrent data is already in memory (e.g., downloaded from a network source) and doesn't need to be read from a file.
- **Parameters**:
  - `b` (bytes): A bytes object containing the raw torrent data. This must be a valid .torrent file format, typically a bencoded dictionary. The bytes object must be valid and non-null.
- **Return Value**:
  - Returns an `lt::add_torrent_params` object containing the parsed torrent data.
  - The returned object can be used directly with libtorrent functions to add the torrent to a session.
- **Exceptions/Errors**:
  - Throws `std::runtime_error` if the buffer contains invalid torrent data.
  - Throws `std::bad_alloc` if memory allocation fails.
- **Example**:
```cpp
// Assuming bytes is a valid bytes object containing torrent data
auto params = load_torrent_buffer0(bytes);
if (params.ti) {
    // Successfully loaded torrent
}
```
- **Preconditions**:
  - The `bytes` object must contain valid torrent data in bencoded format.
  - The bytes object must be valid and non-null.
- **Postconditions**:
  - Returns a valid `lt::add_torrent_params` object if the buffer was successfully parsed.
  - The function does not modify the input buffer.
- **Thread Safety**: The function is thread-safe as long as the underlying libtorrent library is thread-safe.
- **Complexity**: O(n) where n is the size of the torrent data, due to parsing operations.
- **See Also**: `lt::load_torrent_buffer`, `bytes`

## Function: load_torrent_buffer1

- **Signature**: `lt::add_torrent_params load_torrent_buffer1(bytes b, dict cfg)`
- **Description**: Loads a torrent from a byte buffer with additional configuration options. This function extends the basic buffer loading capability by allowing configuration of the torrent's limits and behavior through a dictionary.
- **Parameters**:
  - `b` (bytes): A bytes object containing the raw torrent data. Must be a valid .torrent file in bencoded format.
  - `cfg` (dict): A dictionary containing configuration options for the torrent. This dictionary is converted to `lt::torrent_limits` using `dict_to_limits()` function.
- **Return Value**:
  - Returns an `lt::add_torrent_params` object containing the parsed torrent data and configuration settings.
  - The returned object can be used directly with libtorrent functions to add the torrent to a session.
- **Exceptions/Errors**:
  - Throws `std::runtime_error` if the buffer contains invalid torrent data.
  - Throws `std::invalid_argument` if the configuration dictionary contains invalid keys or values.
  - Throws `std::bad_alloc` if memory allocation fails.
- **Example**:
```cpp
auto params = load_torrent_buffer1(bytes, {"max_connections": 150, "max_download_rate": 5000});
// Use params to add torrent to session
```
- **Preconditions**:
  - The `bytes` object must contain valid torrent data in bencoded format.
  - The `cfg` dictionary must contain valid configuration keys.
- **Postconditions**:
  - Returns a valid `lt::add_torrent_params` object if the buffer was successfully parsed and configuration applied.
  - The function does not modify the input parameters.
- **Thread Safety**: The function is thread-safe as long as the underlying libtorrent library is thread-safe.
- **Complexity**: O(n) where n is the size of the torrent data, due to parsing and configuration processing.
- **See Also**: `lt::load_torrent_buffer`, `dict_to_limits`, `bytes`

## Function: load_torrent_parsed1

- **Signature**: `lt::add_torrent_params load_torrent_parsed1(lt::bdecode_node const& n, dict cfg)`
- **Description**: Loads a torrent from a pre-parsed bdecode_node object with additional configuration options. This function is useful when the torrent data has already been decoded and needs to be converted into an `add_torrent_params` object.
- **Parameters**:
  - `n` (lt::bdecode_node const&): A reference to a bdecode_node object containing the parsed torrent data. This must be a valid bencoded dictionary representing a torrent file.
  - `cfg` (dict): A dictionary containing configuration options for the torrent. This dictionary is converted to `lt::torrent_limits` using `dict_to_limits()` function.
- **Return Value**:
  - Returns an `lt::add_torrent_params` object containing the parsed torrent data and configuration settings.
  - The returned object can be used directly with libtorrent functions to add the torrent to a session.
- **Exceptions/Errors**:
  - Throws `std::runtime_error` if the bdecode_node is invalid or does not represent a valid torrent.
  - Throws `std::invalid_argument` if the configuration dictionary contains invalid keys or values.
  - Throws `std::bad_alloc` if memory allocation fails.
- **Example**:
```cpp
lt::bdecode_node torrent_node;
// Assume torrent_node is populated with valid torrent data
auto params = load_torrent_parsed1(torrent_node, {"max_upload_rate": 2000});
// Use params to add torrent to session
```
- **Preconditions**:
  - The `n` parameter must be a valid bdecode_node object representing a torrent file.
  - The `cfg` dictionary must contain valid configuration keys.
- **Postconditions**:
  - Returns a valid `lt::add_torrent_params` object if the bdecode_node was successfully processed and configuration applied.
  - The function does not modify the input bdecode_node.
- **Thread Safety**: The function is thread-safe as long as the underlying libtorrent library is thread-safe.
- **Complexity**: O(n) where n is the size of the torrent data, due to parsing operations.
- **See Also**: `lt::load_torrent_parsed`, `lt::bdecode_node`, `dict_to_limits`

## Function: bind_load_torrent

- **Signature**: `void bind_load_torrent()`
- **Description**: Binds the torrent loading functions to the Python interface. This function creates the necessary bindings between the C++ torrent loading functions and the Python API, allowing Python code to call these functions.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
// This function is typically called during initialization
bind_load_torrent();
// Now Python code can call load_torrent_file, load_torrent_buffer, etc.
```
- **Preconditions**: None
- **Postconditions**: The specified C++ functions are registered in the Python interface and can be called from Python code.
- **Thread Safety**: The function is typically called during initialization and should not be called concurrently with other binding operations.
- **Complexity**: O(1) - constant time operation for binding functions.
- **See Also**: `def`, `lt::load_torrent_file`, `lt::load_torrent_parsed`

# Usage Examples

## 1. Basic Usage

```cpp
#include "load_torrent.h"

// Load a torrent from a file with default configuration
auto params = load_torrent_file1("example.torrent", {});

// Load a torrent from a buffer with custom configuration
std::vector<uint8_t> torrent_data = /* ... */;
bytes b(torrent_data.data(), torrent_data.size());
auto params = load_torrent_buffer1(b, {"max_connections": 100, "max_download_rate": 5000});

// Load a torrent from a pre-parsed bdecode_node
lt::bdecode_node torrent_node; // Assume this is populated
auto params = load_torrent_parsed1(torrent_node, {});
```

## 2. Error Handling

```cpp
#include <iostream>
#include <stdexcept>

try {
    auto params = load_torrent_file1("nonexistent.torrent", {});
    std::cout << "Torrent loaded successfully" << std::endl;
} catch (const std::runtime_error& e) {
    std::cerr << "Failed to load torrent: " << e.what() << std::endl;
} catch (const std::invalid_argument& e) {
    std::cerr << "Invalid configuration: " << e.what() << std::endl;
} catch (const std::bad_alloc& e) {
    std::cerr << "Memory allocation failed: " << e.what() << std::endl;
}
```

## 3. Edge Cases

```cpp
// Empty torrent file
auto params = load_torrent_file1("", {});

// Invalid torrent file
auto params = load_torrent_file1("invalid.torrent", {});

// Large torrent file (handle memory allocation)
auto params = load_torrent_file1("large_torrent.torrent", {"max_connections": 500});
```

# Best Practices

## Effective Usage

1. Always validate the input torrent data before loading.
2. Use appropriate configuration settings for your use case.
3. Handle errors gracefully with try-catch blocks.
4. Consider using the buffer version for performance-critical applications.

## Common Mistakes to Avoid

1. **Not handling errors**: Always wrap torrent loading operations in try-catch blocks.
2. **Using invalid configuration**: Ensure configuration dictionaries contain valid keys and values.
3. **Memory leaks**: Ensure that all resources are properly cleaned up.
4. **Thread safety issues**: Be aware of the thread safety properties of the functions.

## Performance Tips

1. Use `load_torrent_buffer` when the torrent data is already in memory.
2. Pre-parse bencoded data when possible to avoid repeated parsing.
3. Use appropriate configuration settings to optimize performance.
4. Consider caching parsed torrent data for frequently used torrents.

# Code Review & Improvement Suggestions

## Potential Issues

### Function: load_torrent_file1
**Issue**: The function converts a Python dictionary to limits but doesn't validate the dictionary keys before passing to `dict_to_limits`.
**Severity**: Medium
**Impact**: Could lead to runtime errors if invalid dictionary keys are passed.
**Fix**: Add validation of dictionary keys before calling `dict_to_limits`:
```cpp
lt::add_torrent_params load_torrent_file1(std::string filename, dict cfg)
{
    // Validate dictionary keys here
    // Convert dictionary to limits
    return lt::load_torrent_file(filename, dict_to_limits(cfg));
}
```

### Function: load_torrent_buffer0
**Issue**: No validation of the bytes object content before passing to `lt::load_torrent_buffer`.
**Severity**: Medium
**Impact**: Could lead to runtime errors if the bytes object contains invalid data.
**Fix**: Add validation of the bytes object:
```cpp
lt::add_torrent_params load_torrent_buffer0(bytes b)
{
    // Validate bytes object content
    return lt::load_torrent_buffer(b.arr);
}
```

### Function: load_torrent_buffer1
**Issue**: The function converts a Python dictionary to limits but doesn't validate the dictionary keys.
**Severity**: Medium
**Impact**: Could lead to runtime errors if invalid dictionary keys are passed.
**Fix**: Add validation of dictionary keys:
```cpp
lt::add_torrent_params load_torrent_buffer1(bytes b, dict cfg)
{
    // Validate dictionary keys
    return lt::load_torrent_buffer(b.arr, dict_to_limits(cfg));
}
```

### Function: load_torrent_parsed1
**Issue**: No validation of the bdecode_node object before passing to `lt::load_torrent_parsed`.
**Severity**: Medium
**Impact**: Could lead to runtime errors if the bdecode_node is invalid.
**Fix**: Add validation of the bdecode_node:
```cpp
lt::add_torrent_params load_torrent_parsed1(lt::bdecode_node const& n, dict cfg)
{
    // Validate bdecode_node
    return lt::load_torrent_parsed(n, dict_to_limits(cfg));
}
```

### Function: bind_load_torrent
**Issue**: The function binds functions but doesn't handle potential binding errors.
**Severity**: Medium
**Impact**: Binding failures could go unnoticed, leading to runtime issues.
**Fix**: Add error handling for binding operations:
```cpp
void bind_load_torrent()
{
    try {
        lt::add_torrent_params (*load_torrent_file0)(std::string const&) = &lt::load_torrent_file;
        lt::add_torrent_params (*load_torrent_parsed0)(lt::bdecode_node const&) = &lt::load_torrent_parsed;
        
        def("load_torrent_file", load_torrent_file0);
        def("load_torrent_parsed", load_torrent_parsed0);
    } catch (const std::exception& e) {
        std::cerr << "Failed to bind torrent loading functions: " << e.what() << std::endl;
    }
}
```

## Modernization Opportunities

### Function: load_torrent_file1
**Opportunity**: Use `std::string_view` for the filename parameter to improve performance and flexibility.
**Suggestion**:
```cpp
[[nodiscard]] lt::add_torrent_params load_torrent_file1(std::string_view filename, dict cfg)
{
    return lt::load_torrent_file(std::string(filename), dict_to_limits(cfg));
}
```

### Function: load_torrent_buffer0
**Opportunity**: Use `std::span` for the bytes parameter to improve safety and expressiveness.
**Suggestion**:
```cpp
[[nodiscard]] lt::add_torrent_params load_torrent_buffer0(std::span<const uint8_t> buffer)
{
    return lt::load_torrent_buffer(buffer.data());
}
```

### Function: load_torrent_buffer1
**Opportunity**: Use `std::span` for the bytes parameter and add `[[nodiscard]]` attribute.
**Suggestion**:
```cpp
[[nodiscard]] lt::add_torrent_params load_torrent_buffer1(std::span<const uint8_t> buffer, dict cfg)
{
    return lt::load_torrent_buffer(buffer.data(), dict_to_limits(cfg));
}
```

### Function: load_torrent_parsed1
**Opportunity**: Use `std::span` for the bdecode_node parameter and add `[[nodiscard]]` attribute.
**Suggestion**:
```cpp
[[nodiscard]] lt::add_torrent_params load_torrent_parsed1(lt::bdecode_node const& n, dict cfg)
{
    return lt::load_torrent_parsed(n, dict_to_limits(cfg));
}
```

## Refactoring Suggestions

1. **Extract common logic**: The common pattern of converting dictionaries to limits and loading torrents could be extracted into a utility function.
2. **Create a class**: Consider creating a `TorrentLoader` class to encapsulate the loading functionality and configuration.
3. **Combine similar functions**: The three loading functions could be consolidated into a single function with multiple overloads.

## Performance Optimizations

1. **Use move semantics**: Where possible, use move semantics for large objects.
2. **Return by value**: The functions already return by value, which is optimal for RVO (Return Value Optimization).
3. **Use string_view**: For string parameters, use `std::string_view` to avoid unnecessary string copying.
4. **Add noexcept**: Add `noexcept` where appropriate to improve performance and safety.