# libtorrent Bencode API Documentation

## write_integer

- **Signature**: `int write_integer(OutIt& out, In data)`
- **Description**: Writes a bencoded integer to the output iterator. The function converts the input data to a bencoded integer format (e.g., "i123e"). It validates that the conversion is lossless and uses a stack-allocated buffer for decimal representation.
- **Parameters**:
  - `out` (OutIt&): Output iterator that will receive the bencoded data. This must support increment operations and dereferencing to write values.
  - `data` (In): The integer value to be bencoded. This must be convertible to `entry::integer_type`.
- **Return Value**:
  - Returns the number of bytes written to the output.
  - Returns 0 if the write operation fails.
- **Exceptions/Errors**:
  - If the input data cannot be converted to the expected integer type, the function asserts (in debug builds).
  - No exceptions are thrown, but the function may fail silently.
- **Example**:
```cpp
std::vector<char> buffer;
auto it = buffer.begin();
int result = write_integer(it, 123);
// buffer now contains "i123e"
```
- **Preconditions**:
  - `out` must be a valid output iterator.
  - `data` must be convertible to `entry::integer_type`.
- **Postconditions**:
  - The output iterator will be advanced by the number of bytes written.
  - The buffer will contain the bencoded integer.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(log n) where n is the value of the integer.
- **See Also**: `write_char`, `bencode_recursive`

## write_char

- **Signature**: `void write_char(OutIt& out, char c)`
- **Description**: Writes a single character to the output iterator. This function is a simple wrapper for writing individual characters.
- **Parameters**:
  - `out` (OutIt&): Output iterator that will receive the character. Must support increment and dereferencing.
  - `c` (char): The character to write.
- **Return Value**: None.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
std::vector<char> buffer;
auto it = buffer.begin();
write_char(it, 'a');
// buffer now contains "a"
```
- **Preconditions**:
  - `out` must be a valid output iterator.
- **Postconditions**:
  - The output iterator will be advanced by 1.
  - The character will be written to the buffer.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(1).
- **See Also**: `write_integer`, `read_until`

## read_until

- **Signature**: `std::string read_until(InIt& in, InIt end, char end_token, bool& err)`
- **Description**: Reads characters from the input iterator until the specified end token is found or the end of the input is reached. Returns the collected string.
- **Parameters**:
  - `in` (InIt&): Input iterator that will be advanced as characters are read.
  - `end` (InIt): The end of the input range.
  - `end_token` (char): The character that signals the end of the string.
  - `err` (bool&): Reference to a boolean that will be set to true if an error occurs (e.g., end of input reached before end_token).
- **Return Value**:
  - Returns the string of characters read.
  - Returns an empty string if an error occurs.
- **Exceptions/Errors**:
  - If the input iterator reaches the end before finding the end_token, `err` is set to true.
- **Example**:
```cpp
std::string data = "hello world!";
auto it = data.begin();
bool error = false;
std::string result = read_until(it, data.end(), '!', error);
// result = "hello world", it points to '!'
```
- **Preconditions**:
  - `in` must be a valid input iterator.
  - `end` must be a valid end iterator.
- **Postconditions**:
  - `in` will be advanced to the position after the end_token or to the end of the input.
  - `err` will be set to true if the end_token was not found.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the number of characters read.
- **See Also**: `read_string`, `bdecode_recursive`

## read_string

- **Signature**: `void read_string(InIt& in, InIt end, int len, std::string& str, bool& err)`
- **Description**: Reads a specified number of characters from the input iterator into a string. This function is used to read bencoded strings.
- **Parameters**:
  - `in` (InIt&): Input iterator that will be advanced as characters are read.
  - `end` (InIt): The end of the input range.
  - `len` (int): The number of characters to read. Must be non-negative.
  - `str` (std::string&): Reference to the string that will store the read characters.
  - `err` (bool&): Reference to a boolean that will be set to true if an error occurs (e.g., end of input reached).
- **Return Value**: None.
- **Exceptions/Errors**:
  - If the input iterator reaches the end before reading the specified number of characters, `err` is set to true.
- **Example**:
```cpp
std::string data = "hello world!";
auto it = data.begin();
bool error = false;
std::string result;
read_string(it, data.end(), 5, result, error);
// result = "hello", it points to ' '
```
- **Preconditions**:
  - `in` must be a valid input iterator.
  - `end` must be a valid end iterator.
  - `len` must be non-negative.
- **Postconditions**:
  - `in` will be advanced by `len` characters or to the end of the input.
  - `str` will contain the read characters.
  - `err` will be set to true if the end was reached before reading all characters.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the number of characters read.
- **See Also**: `read_until`, `bencode_recursive`

## bencode_recursive

- **Signature**: `int bencode_recursive(OutIt& out, const entry& e)`
- **Description**: Recursively bencodes a bencoded entry to the output iterator. This function handles integers, strings, and other bencoded types.
- **Parameters**:
  - `out` (OutIt&): Output iterator that will receive the bencoded data.
  - `e` (const entry&): The bencoded entry to encode.
- **Return Value**:
  - Returns the number of bytes written to the output.
  - Returns -1 if an error occurs.
- **Exceptions/Errors**:
  - If the entry type is not supported, the function may fail.
- **Example**:
```cpp
std::vector<char> buffer;
auto it = buffer.begin();
entry e;
e.set_integer(123);
int result = bencode_recursive(it, e);
// buffer now contains "i123e"
```
- **Preconditions**:
  - `out` must be a valid output iterator.
  - `e` must be a valid bencoded entry.
- **Postconditions**:
  - The output iterator will be advanced by the number of bytes written.
  - The buffer will contain the bencoded entry.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the size of the bencoded data.
- **See Also**: `write_integer`, `write_char`

## bdecode_recursive

- **Signature**: `void bdecode_recursive(InIt& in, InIt end, entry& ret, bool& err, int depth)`
- **Description**: Recursively decodes bencoded data from the input iterator into a bencoded entry. This function handles nested bencoded structures.
- **Parameters**:
  - `in` (InIt&): Input iterator that will be advanced as data is read.
  - `end` (InIt): The end of the input range.
  - `ret` (entry&): Reference to the entry that will store the decoded data.
  - `err` (bool&): Reference to a boolean that will be set to true if an error occurs.
  - `depth` (int): Current recursion depth to prevent infinite recursion.
- **Return Value**: None.
- **Exceptions/Errors**:
  - If the recursion depth exceeds 100, `err` is set to true.
  - If the input iterator reaches the end before decoding is complete, `err` is set to true.
- **Example**:
```cpp
std::string data = "i123e";
auto it = data.begin();
bool error = false;
entry e;
bdecode_recursive(it, data.end(), e, error, 0);
// e now contains the integer 123
```
- **Preconditions**:
  - `in` must be a valid input iterator.
  - `end` must be a valid end iterator.
- **Postconditions**:
  - `in` will be advanced to the position after the decoded data.
  - `ret` will contain the decoded entry.
  - `err` will be set to true if an error occurs.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the size of the bencoded data.
- **See Also**: `read_string`, `read_until`

## bencode

- **Signature**: `int bencode(OutIt out, const entry& e)`
- **Description**: Bencodes a bencoded entry to the output iterator. This function is a wrapper around `bencode_recursive`.
- **Parameters**:
  - `out` (OutIt): Output iterator that will receive the bencoded data.
  - `e` (const entry&): The bencoded entry to encode.
- **Return Value**:
  - Returns the number of bytes written to the output.
  - Returns -1 if an error occurs.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::vector<char> buffer;
auto it = buffer.begin();
entry e;
e.set_integer(123);
int result = bencode(it, e);
// buffer now contains "i123e"
```
- **Preconditions**:
  - `out` must be a valid output iterator.
  - `e` must be a valid bencoded entry.
- **Postconditions**:
  - The output iterator will be advanced by the number of bytes written.
  - The buffer will contain the bencoded entry.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the size of the bencoded data.
- **See Also**: `bencode_recursive`, `write_integer`

## bdecode

- **Signature**: `TORRENT_DEPRECATED entry bdecode(InIt start, InIt end)`
- **Description**: Decodes bencoded data from the input range into a bencoded entry. This function is deprecated and should be replaced with the modern version that returns an expected type.
- **Parameters**:
  - `start` (InIt): Input iterator that points to the beginning of the bencoded data.
  - `end` (InIt): Input iterator that points to the end of the bencoded data.
- **Return Value**:
  - Returns the decoded bencoded entry.
  - Returns an empty entry if an error occurs.
- **Exceptions/Errors**:
  - If the input data is malformed, the function may return an invalid entry.
- **Example**:
```cpp
std::string data = "i123e";
auto it = data.begin();
entry e = bdecode(it, data.end());
// e now contains the integer 123
```
- **Preconditions**:
  - `start` must be a valid input iterator.
  - `end` must be a valid end iterator.
- **Postconditions**:
  - The entry `e` will contain the decoded data.
  - If the input is invalid, `e` will be an empty entry.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the size of the bencoded data.
- **See Also**: `bdecode_recursive`, `read_string`

## bdecode

- **Signature**: `TORRENT_DEPRECATED entry bdecode(InIt start, InIt end, typename std::iterator_traits<InIt>::difference_type& len)`
- **Description**: Decodes bencoded data from the input range into a bencoded entry and returns the length of the decoded data. This function is deprecated and should be replaced with the modern version that returns an expected type.
- **Parameters**:
  - `start` (InIt): Input iterator that points to the beginning of the bencoded data.
  - `end` (InIt): Input iterator that points to the end of the bencoded data.
  - `len` (typename std::iterator_traits<InIt>::difference_type&): Reference to a variable that will store the length of the decoded data.
- **Return Value**:
  - Returns the decoded bencoded entry.
  - Returns an empty entry if an error occurs.
- **Exceptions/Errors**:
  - If the input data is malformed, the function may return an invalid entry.
- **Example**:
```cpp
std::string data = "i123e";
auto it = data.begin();
typename std::iterator_traits<decltype(it)>::difference_type len;
entry e = bdecode(it, data.end(), len);
// e now contains the integer 123, len = 5
```
- **Preconditions**:
  - `start` must be a valid input iterator.
  - `end` must be a valid end iterator.
- **Postconditions**:
  - The entry `e` will contain the decoded data.
  - `len` will store the length of the decoded data.
  - If the input is invalid, `e` will be an empty entry.
- **Thread Safety**: Yes, this function is thread-safe.
- **Complexity**: O(n) where n is the size of the bencoded data.
- **See Also**: `bdecode_recursive`, `read_until`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/bencode.hpp>
#include <vector>
#include <string>

// Encoding a simple integer
std::vector<char> buffer;
auto it = buffer.begin();
entry e;
e.set_integer(123);
int result = bencode(it, e);
// buffer now contains "i123e"

// Decoding the encoded data
std::string data(buffer.begin(), buffer.end());
auto it2 = data.begin();
entry decoded;
bool error = false;
bdecode_recursive(it2, data.end(), decoded, error, 0);
// decoded now contains the integer 123
```

## Error Handling

```cpp
#include <libtorrent/bencode.hpp>
#include <iostream>
#include <vector>

void handle_bencode_error(const std::string& data) {
    auto it = data.begin();
    bool error = false;
    entry e;
    bdecode_recursive(it, data.end(), e, error, 0);
    if (error) {
        std::cerr << "Error decoding bencoded data" << std::endl;
        return;
    }
    // Use the decoded entry
    std::cout << "Decoded value: " << e.integer() << std::endl;
}

// Example usage
std::string valid_data = "i123e";
std::string invalid_data = "i123"; // Missing 'e'
handle_bencode_error(valid_data);   // Successfully decodes
handle_bencode_error(invalid_data); // Reports error
```

## Edge Cases

```cpp
#include <libtorrent/bencode.hpp>
#include <vector>
#include <string>

void test_edge_cases() {
    // Test with empty data
    std::string empty_data = "";
    bool error = false;
    entry e;
    bdecode_recursive(empty_data.begin(), empty_data.end(), e, error, 0);
    if (error) {
        std::cout << "Empty data correctly handled" << std::endl;
    }

    // Test with very large integers
    std::string large_data = "i9223372036854775807e"; // Maximum 64-bit integer
    error = false;
    e = entry();
    bdecode_recursive(large_data.begin(), large_data.end(), e, error, 0);
    if (!error) {
        std::cout << "Large integer decoded successfully" << std::endl;
    }

    // Test with nested structures
    std::string nested_data = "d3:fooi123e4:barl3:baz4:qux4:quxe";
    error = false;
    e = entry();
    bdecode_recursive(nested_data.begin(), nested_data.end(), e, error, 0);
    if (!error) {
        std::cout << "Nested structure decoded successfully" << std::endl;
    }
}
```

# Best Practices

## Usage Examples

```cpp
#include <libtorrent/bencode.hpp>
#include <vector>
#include <string>

// Best practice: Use bencode_recursive directly for more control
void encode_with_control() {
    std::vector<char> buffer;
    auto it = buffer.begin();
    entry e;
    e.set_integer(123);
    int result = bencode_recursive(it, e);
    if (result != -1) {
        // Successfully encoded
        std::cout << "Encoded successfully, bytes written: " << result << std::endl;
    } else {
        // Handle encoding error
        std::cerr << "Encoding failed" << std::endl;
    }
}

// Best practice: Use proper error handling
void decode_with_error_handling() {
    std::string data = "i123e";
    auto it = data.begin();
    bool error = false;
    entry e;
    bdecode_recursive(it, data.end(), e, error, 0);
    if (!error) {
        // Successfully decoded
        std::cout << "