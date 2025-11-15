# API Documentation for Hex Encoding/Decoding Functions

## Function: `to_hex` (char array version)

- **Signature**: `void to_hex(char const* in, int len, char* out)`
- **Description**: Converts a binary buffer to its hexadecimal string representation. This function takes a binary input of specified length and writes the corresponding hexadecimal characters to the output buffer. The output buffer must be at least twice the length of the input buffer (since each byte becomes two hex characters).
- **Parameters**:
  - `in` (char const*): Pointer to the binary data to convert. This pointer must be valid and point to a memory region of at least `len` bytes.
  - `len` (int): Length of the binary data in bytes. Must be non-negative. The function will process exactly `len` bytes from the input buffer.
  - `out` (char*): Pointer to the output buffer where the hexadecimal string will be written. This buffer must be large enough to hold at least `2 * len` characters (for the hex digits) plus one additional character for the null terminator if needed.
- **Return Value**:
  - This function returns `void`. The conversion result is written directly to the output buffer.
- **Exceptions/Errors**:
  - **Invalid pointers**: If `in` or `out` is a null pointer, the behavior is undefined (likely a crash).
  - **Buffer overflow**: If the `out` buffer is too small (less than `2 * len` characters), the function will write past the buffer boundaries, leading to undefined behavior.
  - **Negative length**: If `len` is negative, the function may behave unpredictably.
- **Example**:
```cpp
#include <libtorrent/hex.hpp>

int main() {
    char input[] = {0x12, 0x34, 0x56, 0x78};
    char output[9]; // 4 bytes * 2 hex chars + null terminator
    
    to_hex(input, 4, output);
    // output now contains "12345678\0"
    return 0;
}
```
- **Preconditions**:
  - `in` must be a valid pointer to a memory region of at least `len` bytes.
  - `len` must be non-negative.
  - `out` must be a valid pointer to a buffer of at least `2 * len` characters.
  - The output buffer must be large enough to hold the hex string (including any null terminator if needed).
- **Postconditions**:
  - The output buffer contains the hexadecimal representation of the input binary data.
  - The output buffer is null-terminated if the function is called with a buffer that can accommodate it.
- **Thread Safety**: This function is thread-safe as it only reads from the input buffer and writes to the output buffer.
- **Complexity**: O(n) time complexity, O(1) space complexity (assuming the output buffer is provided).
- **See Also**: `to_hex(std::string const&)`, `from_hex()`

## Function: `to_hex` (string version)

- **Signature**: `std::string to_hex(std::string const& s)`
- **Description**: Converts a string to its hexadecimal string representation. This function takes a string and returns a new string containing the hexadecimal representation of each character in the original string.
- **Parameters**:
  - `s` (std::string const&): The input string to convert. This parameter is passed by const reference to avoid unnecessary copying.
- **Return Value**:
  - Returns a `std::string` containing the hexadecimal representation of the input string. Each byte in the input string is converted to two hexadecimal characters.
- **Exceptions/Errors**:
  - **No exceptions**: This function does not throw exceptions under normal circumstances. It will not throw if the input string is empty or contains any character values.
- **Example**:
```cpp
#include <libtorrent/hex.hpp>
#include <iostream>

int main() {
    std::string input = "Hello";
    std::string result = to_hex(input);
    std::cout << "Hex representation: " << result << std::endl;
    // Output: Hex representation: 48656c6c6f
    return 0;
}
```
- **Preconditions**:
  - The input string must be valid (not corrupted or otherwise invalid).
- **Postconditions**:
  - The returned string contains the hexadecimal representation of the input string.
  - The returned string is properly formatted with all characters converted to lowercase hex digits.
- **Thread Safety**: This function is thread-safe as it only reads from the input string and creates a new string.
- **Complexity**: O(n) time complexity, O(n) space complexity.
- **See Also**: `to_hex(char const*, int, char*)`, `from_hex()`

## Function: `from_hex`

- **Signature**: `bool from_hex(char const *in, int len, char* out)`
- **Description**: Converts a hexadecimal string to its binary representation. This function takes a hexadecimal string of specified length and writes the corresponding binary data to the output buffer. The function returns `true` if the conversion was successful, `false` otherwise.
- **Parameters**:
  - `in` (char const *): Pointer to the hexadecimal string to convert. This pointer must be valid and point to a memory region of at least `len` bytes.
  - `len` (int): Length of the hexadecimal string in bytes. Must be non-negative and even (since each byte requires two hex digits).
  - `out` (char*): Pointer to the output buffer where the binary data will be written. This buffer must be large enough to hold at least `len / 2` bytes.
- **Return Value**:
  - Returns `true` if the conversion was successful (all characters were valid hex digits and the length was even).
  - Returns `false` if the conversion failed (invalid hex character or odd length).
- **Exceptions/Errors**:
  - **Invalid pointers**: If `in` or `out` is a null pointer, the behavior is undefined (likely a crash).
  - **Buffer overflow**: If the `out` buffer is too small (less than `len / 2` bytes), the function will write past the buffer boundaries, leading to undefined behavior.
  - **Invalid hex input**: If the input contains non-hex characters (not 0-9, a-f, A-F), the function will return `false`.
  - **Odd length**: If `len` is odd, the function will return `false` since a complete byte cannot be formed.
- **Example**:
```cpp
#include <libtorrent/hex.hpp>

int main() {
    char input[] = "48656c6c6f";
    char output[5];
    
    bool success = from_hex(input, 10, output);
    if (success) {
        // output now contains "Hello"
    } else {
        // Handle conversion error
    }
    return 0;
}
```
- **Preconditions**:
  - `in` must be a valid pointer to a memory region of at least `len` bytes.
  - `len` must be non-negative and even.
  - `out` must be a valid pointer to a buffer of at least `len / 2` bytes.
- **Postconditions**:
  - If successful, the output buffer contains the binary representation of the hexadecimal input.
  - If unsuccessful, the output buffer may contain partially modified data, but the function does not guarantee the state of the buffer.
- **Thread Safety**: This function is thread-safe as it only reads from the input buffer and writes to the output buffer.
- **Complexity**: O(n) time complexity, O(1) space complexity.
- **See Also**: `to_hex(char const*, int, char*)`, `to_hex(std::string const&)`

## Usage Examples

### Basic Usage

```cpp
#include <libtorrent/hex.hpp>
#include <iostream>

int main() {
    // Convert binary data to hex
    char binary_data[] = {0x12, 0x34, 0x56, 0x78};
    char hex_output[9];
    
    to_hex(binary_data, 4, hex_output);
    std::cout << "Binary to hex: " << hex_output << std::endl;
    
    // Convert hex back to binary
    char hex_data[] = "12345678";
    char original_output[4];
    
    bool success = from_hex(hex_data, 8, original_output);
    if (success) {
        std::cout << "Hex to binary successful" << std::endl;
    } else {
        std::cout << "Hex to binary failed" << std::endl;
    }
    
    return 0;
}
```

### Error Handling

```cpp
#include <libtorrent/hex.hpp>
#include <iostream>
#include <vector>

int main() {
    // Test with invalid hex data
    char invalid_hex[] = "12345G78"; // 'G' is not a valid hex digit
    char buffer[4];
    
    bool success = from_hex(invalid_hex, 8, buffer);
    if (!success) {
        std::cout << "Conversion failed: invalid hex data" << std::endl;
    }
    
    // Test with odd length
    char odd_hex[] = "12345"; // 5 characters, can't form complete bytes
    success = from_hex(odd_hex, 5, buffer);
    if (!success) {
        std::cout << "Conversion failed: odd length" << std::endl;
    }
    
    // Test with string version
    std::string string_input = "48656c6c6f";
    try {
        std::string result = to_hex(string_input);
        std::cout << "String hex: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}
```

### Edge Cases

```cpp
#include <libtorrent/hex.hpp>
#include <iostream>

int main() {
    // Empty string case
    char empty_input[1];
    to_hex("", 0, empty_input);
    std::cout << "Empty input: " << empty_input << std::endl;
    
    // Empty buffer case
    char empty_buffer[1];
    from_hex("00", 2, empty_buffer);
    std::cout << "Empty buffer: " << empty_buffer[0] << std::endl;
    
    // Large data case
    const int buffer_size = 1024;
    char large_input[buffer_size];
    char large_output[2 * buffer_size];
    
    // Fill with random data
    for (int i = 0; i < buffer_size; ++i) {
        large_input[i] = static_cast<char>(rand() % 256);
    }
    
    to_hex(large_input, buffer_size, large_output);
    std::cout << "Large data conversion successful" << std::endl;
    
    return 0;
}
```

## Best Practices

### How to Use These Functions Effectively

1. **Always check return values**: The `from_hex` function returns a boolean indicating success or failure. Always check this return value to handle errors properly.

2. **Ensure proper buffer sizing**: When calling `to_hex` with a character array, ensure the output buffer is at least twice the size of the input buffer. For `from_hex`, ensure the output buffer is at least half the size of the input buffer.

3. **Use the string version for simple cases**: When working with `std::string`, use the `to_hex(std::string const&)` function as it's more convenient and handles the buffer management automatically.

4. **Consider the deprecated status**: These functions are marked as deprecated. Consider using modern alternatives if available in your codebase.

5. **Use appropriate error handling**: Implement proper error handling for `from_hex` function calls, as it can fail due to invalid input.

### Common Mistakes to Avoid

1. **Buffer overflows**: The most common mistake is not ensuring that the output buffer is large enough. This can lead to memory corruption and undefined behavior.

2. **Ignoring return values**: Forgetting to check the return value of `from_hex` can lead to bugs when the conversion fails.

3. **Using incorrect buffer sizes**: Using a buffer that's too small for the output can cause data loss or crashes.

4. **Not handling null pointers**: Passing null pointers to these functions will result in undefined behavior.

5. **Using deprecated functions**: These functions are deprecated and may be removed in future versions. Consider migrating to modern alternatives.

### Performance Tips

1. **Pre-allocate buffers**: When converting large amounts of data, pre-allocate buffers to avoid repeated allocations.

2. **Use const references**: When passing strings to `to_hex`, use `std::string const&` to avoid unnecessary copies.

3. **Minimize conversions**: If you need to convert multiple times, consider storing the hex representation to avoid repeated conversions.

4. **Consider in-place conversion**: If you're working with large binary data, consider whether the conversion can be done in-place or with a reusable buffer.

5. **Profile your code**: If performance is critical, profile your code to determine if these conversions are a bottleneck.

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `to_hex(char const*, int, char*)`
**Issue**: Buffer overflow risk when converting large data
**Severity**: Medium
**Impact**: Writing past the buffer boundaries can cause memory corruption and undefined behavior
**Fix**: Add buffer size checks and ensure the output buffer is large enough
```cpp
// Before
inline void to_hex(char const* in, int len, char* out)
{ aux::to_hex({in, len}, out); }

// After
inline bool to_hex(char const* in, int len, char* out, int out_capacity)
{
    if (out_capacity < 2 * len) {
        return false; // Buffer too small
    }
    aux::to_hex({in, len}, out);
    return true;
}
```

**Function**: `to_hex(std::string const&)`
**Issue**: No error handling for invalid string input
**Severity**: Low
**Impact**: The function will convert any string, even if it contains non-printable characters, which might not be expected
**Fix**: Consider adding validation if the input should be printable
```cpp
// Before
inline std::string to_hex(std::string const& s)
{ return aux::to_hex(s); }

// After
inline std::string to_hex(std::string const& s)
{
    // Optional: Validate string content
    for (char c : s) {
        if (c < 0 || c > 255) {
            throw std::invalid_argument("String contains invalid characters");
        }
    }
    return aux::to_hex(s);
}
```

**Function**: `from_hex(char const*, int, char*)`
**Issue**: Buffer overflow risk when converting large hex strings
**Severity**: Medium
**Impact**: Writing past the buffer boundaries can cause memory corruption and undefined behavior
**Fix**: Add buffer size checks and ensure the output buffer is large enough
```cpp
// Before
inline bool from_hex(char const *in, int len, char* out)
{ return aux::from_hex({in, len}, out); }

// After
inline bool from_hex(char const *in, int len, char* out, int out_capacity)
{
    if (len % 2 != 0) {
        return false; // Odd length, can't form complete bytes
    }
    if (out_capacity < len / 2) {
        return false; // Output buffer too small
    }
    return aux::from_hex({in, len}, out);
}
```

### Modernization Opportunities

1. **Use std::span**: Replace raw pointers and lengths with `std::span` for safer and more expressive code.

```cpp
// Modern C++ version
#include <span>

[[nodiscard]] bool from_hex(std::span<const char> hex_input, std::span<char> output_buffer)
{
    if (hex_input.size() % 2 != 0) {
        return false;
    }
    if (output_buffer.size() < hex_input.size() / 2) {
        return false;
    }
    // Implementation using spans
    return aux::from_hex(hex_input, output_buffer);
}
```

2. **Use [[nodiscard]]**: Mark functions that return important values as `[[nodiscard]]` to prevent accidental discard of return values.

```cpp
// Modern C++ version
[[nodiscard]] bool from_hex(char const *in, int len, char* out)
{ return aux::from_hex({in, len}, out); }
```

3. **Use std::string_view**: Replace `std::string const&` with `std::string_view` for better performance and flexibility.

```cpp
// Modern C++ version
[[nodiscard]] std::string to_hex(std::string_view s)
{ return aux::to_hex(s); }
```

### Refactoring Suggestions

1. **Consolidate function signatures**: Consider creating a single function that can handle both string and character array inputs to reduce code duplication.

```cpp
// Suggested refactoring
template<typename InputType>
[[nodiscard]] std::string to_hex(InputType const& input)
{
    // Convert input to hex
    return aux::to_hex(input);
}
```

2. **Move to utility namespace**: Consider moving these functions to a dedicated utility namespace to improve organization.

```cpp
namespace libtorrent::util {
    [[nodiscard]] std::string to_hex(std::string_view s);
    [[nodiscard]] bool from_hex(std::string_view hex_input, std::span<char> output_buffer);
}
```

### Performance Optimizations

1. **Use move semantics**: When returning strings, consider returning by value with RVO (Return Value Optimization) instead of copying.

```cpp
// Optimized version
[[nodiscard]] std::string to_hex(std::string_view s)
{
    std::string result;
    // Reserve space to avoid reallocations
    result.reserve(s.size() * 2);
    // Fill result
    return result;
}
```

2. **Add noexcept**: Mark functions as `noexcept` where appropriate to improve performance and allow compiler optimizations.

```cpp
// Optimized version
[[nodiscard]] bool from_hex(char const *in, int len, char* out) noexcept
{
    // Implementation that doesn't throw exceptions
    return aux::from_hex({in, len}, out);
}
```

3. **Use string_view for read