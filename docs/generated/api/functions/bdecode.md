# libtorrent bdecode API Documentation

## get_bdecode_category

- **Signature**: `auto get_bdecode_category()`
- **Description**: Returns a reference to the bdecode error category, which is used for error handling in bdecode operations. This function is deprecated and should not be used in new code.
- **Parameters**: None
- **Return Value**: Returns a reference to `boost::system::error_category` representing the bdecode error category. This error category can be used to determine the type of error that occurred during bdecode operations.
- **Exceptions/Errors**: None thrown directly, but the returned error category may be used with other error handling mechanisms.
- **Example**:
```cpp
auto& category = get_bdecode_category();
// Use the category for error handling
```
- **Preconditions**: None
- **Postconditions**: Returns a valid reference to the bdecode error category
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bdecode_category()`

## bdecode_token (Constructor 1)

- **Signature**: `auto bdecode_token(std::ptrdiff_t off, bdecode_token::type_t t)`
- **Description**: Constructs a bdecode_token object with the specified offset and type. This constructor is used internally to create bdecode tokens during the decoding process.
- **Parameters**:
  - `off` (std::ptrdiff_t): The offset in the input data where this token begins. Must be non-negative and within the valid range.
  - `t` (bdecode_token::type_t): The type of the token (e.g., string, dictionary, list, etc.). Must be a valid token type.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None thrown directly, but assertions will trigger if invalid parameters are provided.
- **Example**:
```cpp
bdecode_token token(42, bdecode_token::string);
```
- **Preconditions**: `off >= 0` and `off <= max_offset`, and `t <= end`
- **Postconditions**: The bdecode_token object is properly initialized with the specified values
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bdecode_token::type_t`, `bdecode_token::long_string`

## bdecode_token (Constructor 2)

- **Signature**: `auto bdecode_token(std::ptrdiff_t const off, std::uint32_t const next, bdecode_token::type_t const t, std::uint32_t const header_size = 0)`
- **Description**: Constructs a bdecode_token object with the specified offset, next item position, type, and header size. This constructor is used internally to create bdecode tokens during the decoding process.
- **Parameters**:
  - `off` (std::ptrdiff_t): The offset in the input data where this token begins. Must be non-negative.
  - `next` (std::uint32_t): The offset of the next item in the bdecode stream.
  - `t` (bdecode_token::type_t): The type of the token (e.g., string, dictionary, list, etc.).
  - `header_size` (std::uint32_t): The size of the header for this token. Defaults to 0.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None thrown directly, but assertions will trigger if invalid parameters are provided.
- **Example**:
```cpp
bdecode_token token(42, 84, bdecode_token::string, 10);
```
- **Preconditions**: `off >= 0`, `t <= end`, and `header_size` must be valid
- **Postconditions**: The bdecode_token object is properly initialized with the specified values
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bdecode_token::type_t`, `bdecode_token::long_string`

## start_offset

- **Signature**: `auto start_offset() const`
- **Description**: Calculates the starting offset of the data within a bdecode token. This function is used to determine where the actual data begins after the header for string tokens.
- **Parameters**: None
- **Return Value**: Returns an integer representing the starting offset of the data. For short strings, this is `header + 2`. For long strings, this is `header + 8 + 2`.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bdecode_token token(42, 84, bdecode_token::string, 10);
int offset = token.start_offset();
```
- **Preconditions**: The token type must be string or long_string
- **Postconditions**: Returns the correct starting offset for the data
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bdecode_token::string`, `bdecode_token::long_string`

## bdecode

- **Signature**: `auto bdecode(char const* start, char const* end, bdecode_node& ret, error_code& ec, int* error_pos, int depth_limit, int token_limit)`
- **Description**: Parses a bencoded string and populates a bdecode_node object with the decoded data. This function is the main entry point for bdecode operations.
- **Parameters**:
  - `start` (char const*): Pointer to the beginning of the bencoded data.
  - `end` (char const*): Pointer to the end of the bencoded data.
  - `ret` (bdecode_node&): Reference to the bdecode_node object that will store the decoded data.
  - `ec` (error_code&): Reference to an error_code object that will store any error that occurs.
  - `error_pos` (int*): Pointer to an integer that will store the position of any error.
  - `depth_limit` (int): Maximum recursion depth allowed during parsing.
  - `token_limit` (int): Maximum number of tokens allowed during parsing.
- **Return Value**: Returns an integer representing the number of bytes parsed successfully. Returns 0 if an error occurs.
- **Exceptions/Errors**: The function may throw exceptions if there are parsing errors. The error_code parameter will contain the specific error if one occurs.
- **Example**:
```cpp
char data[] = "d3:cow3:moo4:spam4:spami4e";
bdecode_node result;
error_code ec;
int error_pos = 0;
int bytes_parsed = bdecode(data, data + sizeof(data) - 1, result, ec, &error_pos, 100, 1000);
if (bytes_parsed == 0) {
    // Handle error
}
```
- **Preconditions**: `start` must point to valid memory, `end` must be after `start`, `depth_limit` and `token_limit` must be positive
- **Postconditions**: The `ret` parameter contains the decoded data, `ec` contains the error status
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) where n is the length of the input data
- **See Also**: `bdecode_node`, `error_code`

## bdecode_node

- **Signature**: `auto bdecode_node() = default;`
- **Description**: Default constructor for the bdecode_node class. Creates an empty bdecode_node object that can be populated with decoded data.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
bdecode_node node;
// The node is now ready to be populated with decoded data
```
- **Preconditions**: None
- **Postconditions**: The bdecode_node object is in a valid, default-constructed state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bdecode`, `bdecode_token`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/bdecode.hpp"
#include <iostream>

int main() {
    // Sample bencoded data
    char data[] = "d3:cow3:moo4:spam4:spami4e";
    
    // Create a bdecode_node to store the result
    bdecode_node result;
    
    // Create error code for error reporting
    error_code ec;
    
    // Create error position for error reporting
    int error_pos = 0;
    
    // Parse the bencoded data
    int bytes_parsed = bdecode(data, data + sizeof(data) - 1, result, ec, &error_pos, 100, 1000);
    
    // Check for errors
    if (bytes_parsed == 0) {
        std::cerr << "Error parsing bencoded data at position " << error_pos << ": " << ec.message() << std::endl;
        return 1;
    }
    
    // Successfully parsed, now process the data
    if (result.is_dict()) {
        bdecode_node::dict_type const& dict = result.dict();
        for (auto const& pair : dict) {
            std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
        }
    }
    
    return 0;
}
```

## Error Handling

```cpp
#include "libtorrent/bdecode.hpp"
#include <iostream>

void process_bencoded_data(const char* data, size_t length) {
    bdecode_node result;
    error_code ec;
    int error_pos = 0;
    
    int bytes_parsed = bdecode(data, data + length, result, ec, &error_pos, 100, 1000);
    
    if (bytes_parsed == 0) {
        // Handle different types of errors
        if (ec == bdecode_error::too_deep) {
            std::cerr << "Bencoded data is too deeply nested at position " << error_pos << std::endl;
        } else if (ec == bdecode_error::too_many_tokens) {
            std::cerr << "Bencoded data contains too many tokens at position " << error_pos << std::endl;
        } else if (ec == bdecode_error::invalid_string_size) {
            std::cerr << "Invalid string size in bencoded data at position " << error_pos << std::endl;
        } else {
            std::cerr << "Unknown error parsing bencoded data at position " << error_pos << ": " << ec.message() << std::endl;
        }
        return;
    }
    
    // Process successfully decoded data
    if (result.is_dict()) {
        // Process dictionary data
        // ...
    }
}
```

## Edge Cases

```cpp
#include "libtorrent/bdecode.hpp"
#include <iostream>

void test_edge_cases() {
    // Empty input
    char empty_data[] = "";
    bdecode_node result;
    error_code ec;
    int error_pos = 0;
    int bytes_parsed = bdecode(empty_data, empty_data, result, ec, &error_pos, 100, 1000);
    std::cout << "Empty input parsed: " << bytes_parsed << std::endl;
    
    // Invalid bencoded data
    char invalid_data[] = "d3:cow3:moo4:spam4:spami4e"; // Missing closing 'e'
    result = bdecode_node();
    ec = error_code();
    error_pos = 0;
    bytes_parsed = bdecode(invalid_data, invalid_data + sizeof(invalid_data) - 1, result, ec, &error_pos, 100, 1000);
    std::cout << "Invalid data parsed: " << bytes_parsed << ", error: " << ec.message() << std::endl;
    
    // Deep nesting
    char deep_data[] = "d5:rootd5:keyi0ee"; // Very deep nesting
    result = bdecode_node();
    ec = error_code();
    error_pos = 0;
    bytes_parsed = bdecode(deep_data, deep_data + sizeof(deep_data) - 1, result, ec, &error_pos, 1, 1000);
    std::cout << "Deep nesting parsed: " << bytes_parsed << ", error: " << ec.message() << std::endl;
}

int main() {
    test_edge_cases();
    return 0;
}
```

# Best Practices

## Usage Recommendations

1. Always check the return value of `bdecode()` to ensure successful parsing
2. Use proper error handling with `error_code` and `error_pos` to debug issues
3. Set appropriate `depth_limit` and `token_limit` values based on your use case
4. Use the `bdecode_node` class methods to access decoded data safely
5. Handle the `bdecode_error` category appropriately in your error handling code

## Common Mistakes to Avoid

1. **Not checking return values**: Always check the return value of `bdecode()` to detect parsing errors
2. **Invalid memory access**: Ensure that `start` and `end` pointers are valid and that `end` is after `start`
3. **Excessive depth limits**: Set `depth_limit` to prevent stack overflow in deeply nested data
4. **Ignoring error positions**: Use the `error_pos` parameter to pinpoint error locations
5. **Unnecessary allocations**: Use the existing `bdecode_node` object instead of creating new ones for each parse

## Performance Tips

1. **Reuse bdecode_node objects**: Create a bdecode_node object once and reuse it for multiple parse operations
2. **Set appropriate limits**: Tune `depth_limit` and `token_limit` to balance safety and performance
3. **Use const pointers**: Use `char const*` for input data to ensure you don't modify it
4. **Avoid unnecessary copies**: Pass data by pointer rather than copying large strings
5. **Batch processing**: Parse multiple bencoded strings in a single batch when possible

# Code Review & Improvement Suggestions

## Potential Issues

**Function**: `get_bdecode_category`
**Issue**: Function is deprecated but still accessible
**Severity**: Low
**Impact**: Could lead to confusion in codebase
**Fix**: Document as deprecated and recommend using `bdecode_category()` instead:
```cpp
// Deprecated: use bdecode_category() instead
TORRENT_DEPRECATED
inline boost::system::error_category& get_bdecode_category()
{ return bdecode_category(); }
```

**Function**: `bdecode_token` (Constructor 1)
**Issue**: No validation for `t` parameter beyond assertions
**Severity**: Medium
**Impact**: Could lead to undefined behavior if invalid type is passed
**Fix**: Add validation and use a default constructor for invalid types:
```cpp
bdecode_token(std::ptrdiff_t off, bdecode_token::type_t t)
    : offset(std::uint32_t(off))
    , type(t <= end ? t : invalid)
    , next_item(0)
    , header(0)
{
    TORRENT_ASSERT(off >= 0);
    TORRENT_ASSERT(off <= max_offset);
    TORRENT_ASSERT(type <= end);
}
```

**Function**: `bdecode_token` (Constructor 2)
**Issue**: No validation for `header_size` parameter
**Severity**: Medium
**Impact**: Could lead to incorrect parsing if header_size is invalid
**Fix**: Add validation for header_size:
```cpp
bdecode_token(std::ptrdiff_t const off, std::uint32_t const next, bdecode_token::type_t const t, std::uint32_t const header_size = 0)
    : offset(std::uint32_t(off))
    , type(t == string && header_size > aux::bdecode_token::short_string_max_header ? long_string : t)
    , next_item(next)
    , header(header_size)
{
    TORRENT_ASSERT(off >= 0);
    TORRENT_ASSERT(off <= max_offset);
    TORRENT_ASSERT(t <= end);
    TORRENT_ASSERT(header_size <= max_header_size);
}
```

**Function**: `start_offset`
**Issue**: No validation that the token type is actually a string
**Severity**: High
**Impact**: Could lead to incorrect offset calculation
**Fix**: Add validation and handle cases where type is not string:
```cpp
int start_offset() const
{
    TORRENT_ASSERT(type == string || type == long_string);
    if (type == string)
        return int(header) + 2;
    else if (type == long_string)
        return int(header) + 8 + 2;
    else
        return 0; // Or throw an exception
}
```

## Modernization Opportunities

**Function**: `bdecode`
**Opportunity**: Use std::span for safer memory handling
**Suggestion**: Modernize the function signature:
```cpp
[[nodiscard]] bool bdecode(std::span<const char> data, bdecode_node& ret, 
    error_code& ec, int* error_pos, int depth_limit, int token_limit);
```

**Function**: `bdecode_node`
**Opportunity**: Add move semantics
**Suggestion**: Add move constructor and move assignment operator:
```cpp
bdecode_node(bdecode_node&& other) noexcept;
bdecode_node& operator=(bdecode_node&& other) noexcept;
```

**Function**: `bdecode_token`
**Opportunity**: Use std::uint32_t consistently
**Suggestion**: Replace `std::ptrdiff_t` with `std::uint32_t` for offset parameters:
```cpp
bdecode_token(std::uint32_t off, bdecode_token::type_t t)
```

## Refactoring Suggestions

**Function**: `bdecode`
**Suggestion**: Split into separate functions for better maintainability:
- `bdecode_impl` for the core parsing logic
- `bdecode_validate` for input validation
- `bdecode_process` for processing the parsed data

**Function**: `bdecode_token`
**Suggestion**: Consider moving to a separate utility class or namespace for better organization

**Function**: `start_offset`
**Suggestion**: Move to a utility function in a namespace rather than a class method

## Performance Optimizations

**Function**: `bdecode`
**Opportunity**: Use move semantics for the bdecode_node parameter:
```cpp
[[nodiscard]] bool bdecode(std::span<const char> data, bdecode_node&& ret, 
    error_code& ec, int* error_pos, int depth_limit, int token_limit);
```

**Function**: `bdecode_token`
**Opportunity**: Consider using a pool allocator for token objects to reduce allocations

**Function**: `bdecode_node`
**Opportunity**: Add a move constructor and move assignment operator to improve performance when moving objects