# libtorrent Magnet URI API Documentation

## _add_magnet_uri

- **Signature**: `torrent_handle _add_magnet_uri(lt::session& s, std::string uri, dict params)`
- **Description**: Adds a torrent to a libtorrent session using a magnet URI. This function is deprecated and should not be used in new code. It parses the magnet URI and adds the torrent to the session with the specified parameters.
- **Parameters**:
  - `s` (lt::session&): Reference to the libtorrent session object where the torrent will be added. The session must be valid and running.
  - `uri` (std::string): The magnet URI string to parse and add. Must be a valid magnet URI format (e.g., "magnet:?xt=urn:btih:ABC123...").
  - `params` (dict): Dictionary containing additional parameters for the torrent addition. This can include settings like save path, priority, etc.
- **Return Value**:
  - `torrent_handle`: A handle to the added torrent, which can be used to control the torrent. Returns a valid handle on success.
- **Exceptions/Errors**:
  - `system_error`: Thrown if there's an error parsing the magnet URI or adding the torrent to the session.
  - `std::invalid_argument`: If the input parameters are invalid.
- **Example**:
```cpp
try {
    lt::session s;
    auto handle = _add_magnet_uri(s, "magnet:?xt=urn:btih:ABC123...", dict());
    std::cout << "Torrent added with handle: " << handle.info_hash() << std::endl;
} catch (const std::exception& e) {
    std::cerr << "Error adding magnet URI: " << e.what() << std::endl;
}
```
- **Preconditions**:
  - The session object must be valid and running.
  - The magnet URI must be properly formatted.
  - The parameters dictionary must be valid.
- **Postconditions**:
  - The torrent is added to the session.
  - A valid torrent handle is returned if successful.
- **Thread Safety**: This function is thread-safe as it uses a threading guard.
- **Complexity**: O(n) where n is the length of the magnet URI.
- **See Also**: `parse_magnet_uri_wrap`, `make_magnet_uri`

## parse_magnet_uri_dict

- **Signature**: `dict parse_magnet_uri_dict(std::string const& uri)`
- **Description**: Parses a magnet URI and returns a dictionary containing the extracted information. This function is used to extract metadata from a magnet URI without adding it to a session.
- **Parameters**:
  - `uri` (std::string const&): The magnet URI to parse. Must be a valid magnet URI format.
- **Return Value**:
  - `dict`: A dictionary containing the parsed information from the magnet URI, including torrent info (ti), trackers, and other metadata.
- **Exceptions/Errors**:
  - `system_error`: Thrown if there's an error parsing the magnet URI.
- **Example**:
```cpp
try {
    auto result = parse_magnet_uri_dict("magnet:?xt=urn:btih:ABC123...");
    if (result.contains("ti")) {
        std::cout << "Found torrent info" << std::endl;
    }
    if (result.contains("trackers")) {
        std::cout << "Found trackers" << std::endl;
    }
} catch (const std::exception& e) {
    std::cerr << "Error parsing magnet URI: " << e.what() << std::endl;
}
```
- **Preconditions**:
  - The magnet URI must be properly formatted.
- **Postconditions**:
  - The dictionary contains all the parsed information from the magnet URI.
- **Thread Safety**: This function is thread-safe as it uses a threading guard.
- **Complexity**: O(n) where n is the length of the magnet URI.
- **See Also**: `parse_magnet_uri_wrap`, `make_magnet_uri`

## parse_magnet_uri_wrap

- **Signature**: `add_torrent_params parse_magnet_uri_wrap(std::string const& uri)`
- **Description**: Parses a magnet URI and returns an `add_torrent_params` object containing the extracted information. This function is a wrapper around the underlying parse_magnet_uri function.
- **Parameters**:
  - `uri` (std::string const&): The magnet URI to parse. Must be a valid magnet URI format.
- **Return Value**:
  - `add_torrent_params`: An object containing the parsed information from the magnet URI, including torrent info, trackers, and other parameters.
- **Exceptions/Errors**:
  - `system_error`: Thrown if there's an error parsing the magnet URI.
- **Example**:
```cpp
try {
    auto params = parse_magnet_uri_wrap("magnet:?xt=urn:btih:ABC123...");
    if (params.ti) {
        std::cout << "Found torrent info" << std::endl;
    }
    for (const auto& tracker : params.trackers) {
        std::cout << "Tracker: " << tracker << std::endl;
    }
} catch (const std::exception& e) {
    std::cerr << "Error parsing magnet URI: " << e.what() << std::endl;
}
```
- **Preconditions**:
  - The magnet URI must be properly formatted.
- **Postconditions**:
  - The add_torrent_params object contains all the parsed information from the magnet URI.
- **Thread Safety**: This function is thread-safe as it uses a threading guard.
- **Complexity**: O(n) where n is the length of the magnet URI.
- **See Also**: `parse_magnet_uri_dict`, `make_magnet_uri`

## bind_magnet_uri

- **Signature**: `void bind_magnet_uri()`
- **Description**: Binds magnet URI functions to the Python interface. This function registers the magnet URI functions with the Python binding system, making them available in the Python API.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
// This function is called during initialization of the Python bindings
// It's not intended to be called directly by application code
bind_magnet_uri();
```
- **Preconditions**:
  - The Python binding system must be initialized.
- **Postconditions**:
  - The magnet URI functions are registered with the Python interface.
- **Thread Safety**: This function is not thread-safe and should only be called during initialization.
- **Complexity**: O(1)
- **See Also**: `add_magnet_uri`, `parse_magnet_uri_wrap`

# Usage Examples

## Basic Usage

```cpp
#include "bindings/python/src/magnet_uri.cpp"
#include <iostream>
#include <string>

int main() {
    lt::session s;
    
    // Parse a magnet URI
    auto params = parse_magnet_uri_wrap("magnet:?xt=urn:btih:ABC123...");
    std::cout << "Parsed magnet URI" << std::endl;
    
    // Add the torrent to the session
    try {
        auto handle = _add_magnet_uri(s, "magnet:?xt=urn:btih:ABC123...", dict());
        std::cout << "Added torrent with handle: " << handle.info_hash() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Failed to add magnet URI: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Error Handling

```cpp
#include "bindings/python/src/magnet_uri.cpp"
#include <iostream>
#include <string>

void handle_magnet_uri(const std::string& uri) {
    try {
        // Parse the magnet URI
        auto params = parse_magnet_uri_wrap(uri);
        std::cout << "Successfully parsed magnet URI" << std::endl;
        
        // Add to session
        lt::session s;
        auto handle = _add_magnet_uri(s, uri, dict());
        std::cout << "Added torrent: " << handle.info_hash() << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime error: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "General error: " << e.what() << std::endl;
    }
}

int main() {
    handle_magnet_uri("magnet:?xt=urn:btih:ABC123...");
    return 0;
}
```

## Edge Cases

```cpp
#include "bindings/python/src/magnet_uri.cpp"
#include <iostream>
#include <string>

void test_edge_cases() {
    // Empty URI
    try {
        auto params = parse_magnet_uri_wrap("");
        std::cout << "Empty URI parsed successfully" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Empty URI error: " << e.what() << std::endl;
    }
    
    // Invalid URI
    try {
        auto params = parse_magnet_uri_wrap("not a magnet uri");
        std::cout << "Invalid URI parsed successfully" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Invalid URI error: " << e.what() << std::endl;
    }
    
    // URI with special characters
    try {
        auto params = parse_magnet_uri_wrap("magnet:?xt=urn:btih:ABC123%20test");
        std::cout << "URI with special characters parsed successfully" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "URI with special characters error: " << e.what() << std::endl;
    }
}

int main() {
    test_edge_cases();
    return 0;
}
```

# Best Practices

## How to Use These Functions Effectively

1. Use `parse_magnet_uri_wrap` to extract information from a magnet URI without adding it to a session.
2. Use `_add_magnet_uri` to add a torrent to a session, but be aware it's deprecated.
3. Always handle exceptions when parsing and adding magnet URIs.
4. Validate magnet URIs before passing them to these functions.

## Common Mistakes to Avoid

1. **Using deprecated functions**: Avoid using `_add_magnet_uri` in new code.
2. **Not handling exceptions**: Always wrap magnet URI operations in try-catch blocks.
3. **Passing invalid URIs**: Validate URIs before passing them to these functions.
4. **Not checking return values**: Always verify that operations succeed.

## Performance Tips

1. **Cache parsed parameters**: If you need to use the same magnet URI multiple times, parse it once and reuse the parameters.
2. **Use string_view**: For read-only string operations, consider using `std::string_view` for better performance.
3. **Batch operations**: When adding multiple torrents, consider batch processing to reduce overhead.

# Code Review & Improvement Suggestions

## Potential Issues

### **Function**: `_add_magnet_uri`
**Issue**: Function is deprecated but still used in bindings
**Severity**: High
**Impact**: Using deprecated code can lead to maintenance issues and potential future compatibility problems
**Fix**: Replace with modern equivalent:
```cpp
// Replace deprecated function
// Instead of using _add_magnet_uri, use the modern API
auto add_torrent_params p;
dict_to_add_torrent_params(params, p);
p.url = uri;
auto handle = s.add_torrent(p);
```

### **Function**: `parse_magnet_uri_dict`
**Issue**: Incomplete function (code snippet truncated)
**Severity**: Critical
**Impact**: The function is incomplete and cannot be compiled or used
**Fix**: Complete the function implementation:
```cpp
dict parse_magnet_uri_dict(std::string const& uri)
{
    error_code ec;
    add_torrent_params p = parse_magnet_uri(uri, ec);

    if (ec) throw system_error(ec);

    dict ret;

    if (p.ti) ret["ti"] = p.ti;
    list tracker_list;
    for (std::vector<std::string>::const_iterator i = p.trackers.begin()
        , e = p.trackers.end(); i != e; ++i) {
        tracker_list.append(*i);
    }
    ret["trackers"] = tracker_list;

    if (p.save_path.size()) ret["save_path"] = p.save_path;
    if (p.storage_mode != storage_mode_allocate) {
        ret["storage_mode"] = p.storage_mode;
    }
    if (p.torrent_file) ret["torrent_file"] = p.torrent_file;
    if (p.url.size()) ret["url"] = p.url;
    if (p.priorities.size()) ret["priorities"] = p.priorities;
    if (p.file_priorities.size()) ret["file_priorities"] = p.file_priorities;
    if (p.resume_data.size()) ret["resume_data"] = p.resume_data;

    return ret;
}
```

### **Function**: `parse_magnet_uri_wrap`
**Issue**: Incomplete function (code snippet truncated)
**Severity**: Critical
**Impact**: The function is incomplete and cannot be compiled or used
**Fix**: Complete the function implementation:
```cpp
add_torrent_params parse_magnet_uri_wrap(std::string const& uri)
{
    error_code ec;
    add_torrent_params p = parse_magnet_uri(uri, ec);
    if (ec) throw system_error(ec);
    return p;
}
```

### **Function**: `bind_magnet_uri`
**Issue**: Incomplete function (code snippet truncated)
**Severity**: High
**Impact**: The function is incomplete and cannot be compiled or used
**Fix**: Complete the function implementation:
```cpp
void bind_magnet_uri()
{
#if TORRENT_ABI_VERSION == 1
    def("add_magnet_uri", &_add_magnet_uri);
#endif
    def("make_magnet_uri", make_magnet_uri0);
    def("make_magnet_uri", make_magnet_uri1);
    def("make_magnet_uri", make_magnet_uri2);
    def("parse_magnet_uri", parse_magnet_uri_wrap);
    def("parse_magnet_uri_dict", parse_magnet_uri_dict);
}
```

## Modernization Opportunities

### **Function**: `_add_magnet_uri`
```cpp
// Before
torrent_handle _add_magnet_uri(lt::session& s, std::string uri, dict params)

// After
[[nodiscard]] torrent_handle add_magnet_uri(lt::session& s, std::string_view uri, dict params)
```

### **Function**: `parse_magnet_uri_dict`
```cpp
// Before
dict parse_magnet_uri_dict(std::string const& uri)

// After
[[nodiscard]] dict parse_magnet_uri_dict(std::string_view uri)
```

### **Function**: `parse_magnet_uri_wrap`
```cpp
// Before
add_torrent_params parse_magnet_uri_wrap(std::string const& uri)

// After
[[nodiscard]] add_torrent_params parse_magnet_uri_wrap(std::string_view uri)
```

## Refactoring Suggestions

1. **Split functions**: The `bind_magnet_uri` function should be split into separate registration functions for better organization.
2. **Combine similar functions**: The three `make_magnet_uri` functions should be combined into a single function with overloads.
3. **Move to utility namespace**: These magnet URI functions should be moved to a utility namespace for better organization.

## Performance Optimizations

1. **Use string_view**: Replace `std::string const&` with `std::string_view` for read-only string parameters.
2. **Return by value**: The functions can return by value for better performance due to RVO.
3. **Add noexcept**: Mark functions as `noexcept` where appropriate to improve performance.