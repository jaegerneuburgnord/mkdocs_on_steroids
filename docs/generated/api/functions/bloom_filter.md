# libtorrent Bloom Filter API Documentation

## Function Reference

### find

- **Signature**: `bool find(sha1_hash const& k) const`
- **Description**: Checks if a given SHA-1 hash exists in the bloom filter. This function determines whether the hash is likely to be in the filter based on the hash's bits. Returns true if the hash is likely to be present (note that false positives are possible, but false negatives are not).
- **Parameters**:
  - `k` (sha1_hash const&): The SHA-1 hash to check for presence in the bloom filter. Must be a valid SHA-1 hash (20 bytes). The function uses the hash's bit representation to query the filter.
- **Return Value**:
  - `true`: The hash is likely to be in the filter (possible false positive)
  - `false`: The hash is definitely not in the filter (no false negatives)
- **Exceptions/Errors**:
  - No exceptions are thrown. The function is designed to be robust and handle all inputs.
- **Example**:
```cpp
sha1_hash hash = generate_random_sha1(); // Assume this function exists
bool result = filter.find(hash);
if (result) {
    std::cout << "Hash might be in the filter\n";
} else {
    std::cout << "Hash is definitely not in the filter\n";
}
```
- **Preconditions**: The bloom filter must be properly initialized (typically through default construction or from_string).
- **Postconditions**: The bloom filter state remains unchanged.
- **Thread Safety**: Thread-safe for concurrent read operations.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `set()`, `to_string()`, `from_string()`

### set

- **Signature**: `void set(sha1_hash const& k)`
- **Description**: Adds a given SHA-1 hash to the bloom filter by setting the appropriate bits. This operation is non-deterministic regarding which bits get set, but the function uses a consistent hash function to map the hash to filter bits.
- **Parameters**:
  - `k` (sha1_hash const&): The SHA-1 hash to add to the bloom filter. Must be a valid SHA-1 hash (20 bytes). The function will use the hash's bit representation to set multiple bits in the filter.
- **Return Value**:
  - `void`: No return value.
- **Exceptions/Errors**:
  - No exceptions are thrown. The function is designed to be robust and handle all inputs.
- **Example**:
```cpp
sha1_hash hash = generate_random_sha1();
filter.set(hash);
std::cout << "Hash added to bloom filter\n";
```
- **Preconditions**: The bloom filter must be properly initialized.
- **Postconditions**: The bloom filter is updated to include the hash (some bits are set).
- **Thread Safety**: Not thread-safe for concurrent modifications. Multiple threads should synchronize access to the bloom filter.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `find()`, `clear()`, `to_string()`

### to_string

- **Signature**: `std::string to_string() const`
- **Description**: Converts the bloom filter's internal bit representation to a string. This is useful for serialization, storage, or transmission of the bloom filter's state.
- **Parameters**: None.
- **Return Value**:
  - `std::string`: A string containing the raw bit data of the bloom filter. The string length will be exactly N bytes, where N is the filter size.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Add some hashes to the filter
filter.set(generate_random_sha1());
filter.set(generate_random_sha1());

std::string serialized = filter.to_string();
std::cout << "Serialized bloom filter size: " << serialized.size() << " bytes\n";
```
- **Preconditions**: The bloom filter must be properly initialized.
- **Postconditions**: The bloom filter state remains unchanged.
- **Thread Safety**: Thread-safe for concurrent read operations.
- **Complexity**: O(N) time complexity, O(N) space complexity (for the returned string).
- **See Also**: `from_string()`, `clear()`, `size()`

### from_string

- **Signature**: `void from_string(char const* str)`
- **Description**: Loads the bloom filter's state from a string representation. This function is used to restore a bloom filter that was previously serialized with `to_string()`. The string must contain exactly N bytes of data.
- **Parameters**:
  - `str` (char const*): A pointer to a character string containing the serialized bloom filter data. Must point to a valid memory location containing exactly N bytes of data.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - No exceptions are thrown. The function assumes the input string is valid and properly formatted.
- **Example**:
```cpp
// Assume we have serialized data from a previous session
std::string serialized_data = load_from_file("bloom_filter.bin"); // Assume this function exists
filter.from_string(serialized_data.c_str());
std::cout << "Bloom filter restored from string\n";
```
- **Preconditions**: The string must contain exactly N bytes of data, and `str` must not be null.
- **Postconditions**: The bloom filter is populated with the data from the string.
- **Thread Safety**: Not thread-safe for concurrent modifications. Multiple threads should synchronize access to the bloom filter.
- **Complexity**: O(N) time complexity, O(1) space complexity.
- **See Also**: `to_string()`, `clear()`, `size()`

### clear

- **Signature**: `void clear()`
- **Description**: Resets the bloom filter to its initial state by clearing all bits. This function is useful when reusing a bloom filter for a new set of data or when resetting the filter's state.
- **Parameters**: None.
- **Return Value**:
  - `void`: No return value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Add some hashes
filter.set(generate_random_sha1());
filter.set(generate_random_sha1());

// Clear the filter
filter.clear();
std::cout << "Bloom filter cleared\n";
```
- **Preconditions**: The bloom filter must be properly initialized.
- **Postconditions**: All bits in the bloom filter are set to zero.
- **Thread Safety**: Not thread-safe for concurrent modifications.
- **Complexity**: O(N) time complexity, O(1) space complexity.
- **See Also**: `set()`, `find()`, `to_string()`

### size

- **Signature**: `float size() const`
- **Description**: Calculates and returns the estimated size of the bloom filter in bits. This function computes the size based on the current number of unset bits and the total number of bits in the filter. The calculation is based on the formula for optimal bloom filter size.
- **Parameters**: None.
- **Return Value**:
  - `float`: The estimated size of the bloom filter in bits. The return value is calculated using the formula: `log(c / m) / (2 * log(1 - 1/m))`, where c is the number of unset bits and m is the total number of bits.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Add some hashes
filter.set(generate_random_sha1());
filter.set(generate_random_sha1());

float estimated_size = filter.size();
std::cout << "Estimated bloom filter size: " << estimated_size << " bits\n";
```
- **Preconditions**: The bloom filter must be properly initialized.
- **Postconditions**: The bloom filter state remains unchanged.
- **Thread Safety**: Thread-safe for concurrent read operations.
- **Complexity**: O(N) time complexity, O(1) space complexity.
- **See Also**: `find()`, `set()`, `clear()`

### bloom_filter

- **Signature**: `bloom_filter()`
- **Description**: Default constructor for the bloom_filter class. Initializes the bloom filter by calling the `clear()` function to set all bits to zero. This constructor is used to create a new, empty bloom filter.
- **Parameters**: None.
- **Return Value**: 
  - Creates a new bloom_filter object.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Create a new bloom filter
bloom_filter filter;
std::cout << "New bloom filter created\n";
```
- **Preconditions**: None.
- **Postconditions**: The bloom filter is initialized with all bits set to zero.
- **Thread Safety**: Not thread-safe for concurrent modifications.
- **Complexity**: O(N) time complexity, O(1) space complexity.
- **See Also**: `clear()`, `set()`, `find()`

## Usage Examples

### Basic Usage

```cpp
#include "bloom_filter.hpp"
#include <iostream>
#include <string>

int main() {
    // Create a new bloom filter
    bloom_filter filter;
    
    // Add some hashes to the filter
    sha1_hash hash1 = generate_random_sha1();
    sha1_hash hash2 = generate_random_sha1();
    
    filter.set(hash1);
    filter.set(hash2);
    
    // Check if hashes are in the filter
    bool found1 = filter.find(hash1);
    bool found2 = filter.find(hash2);
    bool found3 = filter.find(sha1_hash{}); // A different hash
    
    std::cout << "Hash 1 found: " << (found1 ? "true" : "false") << "\n";
    std::cout << "Hash 2 found: " << (found2 ? "true" : "false") << "\n";
    std::cout << "Hash 3 found: " << (found3 ? "true" : "false") << "\n";
    
    // Serialize the filter
    std::string serialized = filter.to_string();
    std::cout << "Serialized size: " << serialized.size() << " bytes\n";
    
    // Create a new filter and load the serialized data
    bloom_filter new_filter;
    new_filter.from_string(serialized.c_str());
    
    // Verify the loaded filter works
    bool loaded_found1 = new_filter.find(hash1);
    std::cout << "Loaded filter found hash 1: " << (loaded_found1 ? "true" : "false") << "\n";
    
    return 0;
}
```

### Error Handling

```cpp
#include "bloom_filter.hpp"
#include <iostream>
#include <string>
#include <stdexcept>

int main() {
    bloom_filter filter;
    
    try {
        // Attempt to load invalid data
        std::string invalid_data = "short data"; // Only 10 bytes, but we need N bytes
        filter.from_string(invalid_data.c_str());
        
        // The function doesn't throw exceptions, so we need to check the result
        // This is a limitation of the current design
        
        // In a real application, we might want to validate the length first
        if (invalid_data.size() != N) {
            std::cerr << "Invalid data length: expected " << N << ", got " << invalid_data.size() << "\n";
            return 1;
        }
        
        std::cout << "Data loaded successfully\n";
    } catch (const std::exception& e) {
        std::cerr << "Exception occurred: " << e.what() << "\n";
        return 1;
    }
    
    return 0;
}
```

### Edge Cases

```cpp
#include "bloom_filter.hpp"
#include <iostream>
#include <string>

int main() {
    bloom_filter filter;
    
    // Test with empty filter
    sha1_hash empty_hash;
    bool found = filter.find(empty_hash);
    std::cout << "Find empty hash: " << (found ? "true" : "false") << "\n";
    // Expected: false (not in filter)
    
    // Test with all-zero hash
    sha1_hash zero_hash;
    std::fill_n(zero_hash.begin(), 20, 0);
    filter.set(zero_hash);
    bool found_zero = filter.find(zero_hash);
    std::cout << "Find all-zero hash: " << (found_zero ? "true" : "false") << "\n";
    // Expected: true (in filter)
    
    // Test with maximum value hash
    sha1_hash max_hash;
    std::fill_n(max_hash.begin(), 20, 255);
    filter.set(max_hash);
    bool found_max = filter.find(max_hash);
    std::cout << "Find maximum hash: " << (found_max ? "true" : "false") << "\n";
    // Expected: true (in filter)
    
    // Test with minimal hash
    sha1_hash min_hash;
    std::fill_n(min_hash.begin(), 20, 1);
    filter.set(min_hash);
    bool found_min = filter.find(min_hash);
    std::cout << "Find minimal hash: " << (found_min ? "true" : "false") << "\n";
    // Expected: true (in filter)
    
    return 0;
}
```

## Best Practices

### Effective Usage

1. **Initialization**: Always initialize the bloom filter using the default constructor or `from_string()` before use.
2. **Serialization**: Use `to_string()` and `from_string()` for persistent storage, ensuring the data is saved and loaded in the same format.
3. **Memory Management**: Be aware of the N-byte requirement for the bloom filter, as this affects memory usage.
4. **Concurrent Access**: Use proper synchronization mechanisms when multiple threads access the same bloom filter.

### Common Mistakes to Avoid

1. **Using Invalid Data**: Ensure that the string passed to `from_string()` contains exactly N bytes of data.
2. **Ignoring Return Values**: While `find()` returns a meaningful result, don't ignore the return value of `set()` or `clear()` as they don't return values.
3. **Overlooking Thread Safety**: The `set()` and `from_string()` methods are not thread-safe, so synchronize access when using them in multithreaded applications.

### Performance Tips

1. **Batch Operations**: When adding many hashes, consider the cost of multiple `set()` calls and look for opportunities to batch operations.
2. **Memory Layout**: Be aware of the N-byte memory requirement and plan your memory allocation accordingly.
3. **Avoid Unnecessary Copies**: Use references where possible to avoid copying large data structures.

## Code Review & Improvement Suggestions

### find

- **Function**: `find`
- **Issue**: No input validation for the sha1_hash parameter
- **Severity**: Low
- **Impact**: The function assumes the input is valid, but in a production environment, input validation could prevent potential issues
- **Fix**: Add a validation check for the hash parameter:
```cpp
bool find(sha1_hash const& k) const
{
    if (k.size() != 20) {
        throw std::invalid_argument("SHA-1 hash must be 20 bytes");
    }
    return has_bits(&k[0], bits, N);
}
```

### set

- **Function**: `set`
- **Issue**: No input validation for the sha1_hash parameter
- **Severity**: Low
- **Impact**: The function assumes the input is valid, but in a production environment, input validation could prevent potential issues
- **Fix**: Add a validation check for the hash parameter:
```cpp
void set(sha1_hash const& k)
{
    if (k.size() != 20) {
        throw std::invalid_argument("SHA-1 hash must be 20 bytes");
    }
    set_bits(&k[0], bits, N);
}
```

### to_string

- **Function**: `to_string`
- **Issue**: No bounds checking for the N parameter
- **Severity**: Low
- **Impact**: The function assumes N is valid, but in a production environment, bounds checking could prevent potential issues
- **Fix**: Add bounds checking:
```cpp
std::string to_string() const
{
    if (N > std::numeric_limits<size_t>::max()) {
        throw std::overflow_error("N is too large");
    }
    return std::string(reinterpret_cast<char const*>(&bits[0]), N);
}
```

### from_string

- **Function**: `from_string`
- **Issue**: No bounds checking for the string length
- **Severity**: Medium
- **Impact**: The function could read past the end of the string if it's too short, leading to undefined behavior
- **Fix**: Add bounds checking:
```cpp
void from_string(char const* str)
{
    if (str == nullptr) {
        throw std::invalid_argument("String cannot be null");
    }
    if (std::strlen(str) < N) {
        throw std::invalid_argument("String is too short");
    }
    std::memcpy(bits, str, N);
}
```

### clear

- **Function**: `clear`
- **Issue**: No bounds checking for the N parameter
- **Severity**: Low
- **Impact**: The function assumes N is valid, but in a production environment, bounds checking could prevent potential issues
- **Fix**: Add bounds checking:
```cpp
void clear()
{
    if (N > std::numeric_limits<size_t>::max()) {
        throw std::overflow_error("N is too large");
    }
    std::memset(bits, 0, N);
}
```

### size

- **Function**: `size`
- **Issue**: Potential for floating-point precision issues
- **Severity**: Medium
- **Impact**: The calculation could lose precision with very large values of N
- **Fix**: Use a more numerically stable approach:
```cpp
float size() const
{
    int const c = (std::min)(count_zero_bits(bits, N), (N * 8) - 1);
    int const m = N * 8;
    
    // Use more precise floating-point calculation
    if (m == 0) {
        return 0.0f;
    }
    
    float log_m = std::log(float(m));
    float log_c_m = std::log(float(c) / float(m));
    
    return log_c_m / (2.0f * log_m);
}
```

### bloom_filter

- **Function**: `bloom_filter`
- **Issue**: No bounds checking for the N parameter
- **Severity**: Low
- **Impact**: The function assumes N is valid, but in a production environment, bounds checking could