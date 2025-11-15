```markdown
# libtorrent Byte Order Conversion API

## host_to_network (std::uint32_t)

- **Signature**: `std::uint32_t host_to_network(std::uint32_t x)`
- **Description**: Converts a 32-bit unsigned integer from host byte order to network byte order (big-endian). This function is essential for network communication where data must be transmitted in a standardized byte order regardless of the host architecture.
- **Parameters**:
  - `x` (std::uint32_t): The 32-bit unsigned integer value to convert from host byte order to network byte order. The value can be any valid 32-bit unsigned integer.
- **Return Value**:
  - Returns the input value converted to network byte order (big-endian). The return value is a 32-bit unsigned integer in network byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. This function is a simple wrapper around the standard `htonl` function.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint32_t host_value = 0x12345678;
    std::uint32_t network_value = host_to_network(host_value);
    std::cout << "Host value: " << std::hex << host_value << std::endl;
    std::cout << "Network value: " << std::hex << network_value << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 32-bit unsigned integer.
- **Postconditions**: The returned value is the input value converted to network byte order (big-endian).
- **Thread Safety**: This function is thread-safe as it only performs a simple bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `network_to_host`, `host_to_network` (std::uint16_t), `swap_byteorder`

## network_to_host (std::uint32_t)

- **Signature**: `std::uint32_t network_to_host(std::uint32_t x)`
- **Description**: Converts a 32-bit unsigned integer from network byte order (big-endian) to host byte order. This function is used to interpret network data on the local system's byte order.
- **Parameters**:
  - `x` (std::uint32_t): The 32-bit unsigned integer value in network byte order (big-endian) to convert to host byte order.
- **Return Value**:
  - Returns the input value converted to host byte order. The return value is a 32-bit unsigned integer in host byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. This function is a simple wrapper around the standard `ntohl` function.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint32_t network_value = 0x12345678;
    std::uint32_t host_value = network_to_host(network_value);
    std::cout << "Network value: " << std::hex << network_value << std::endl;
    std::cout << "Host value: " << std::hex << host_value << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 32-bit unsigned integer in network byte order (big-endian).
- **Postconditions**: The returned value is the input value converted to host byte order.
- **Thread Safety**: This function is thread-safe as it only performs a simple bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `host_to_network`, `network_to_host` (std::uint16_t), `little_endian_to_host`

## host_to_network (std::uint16_t)

- **Signature**: `std::uint16_t host_to_network(std::uint16_t x)`
- **Description**: Converts a 16-bit unsigned integer from host byte order to network byte order (big-endian). This function is used for network communication where 16-bit values need to be transmitted in a standardized byte order.
- **Parameters**:
  - `x` (std::uint16_t): The 16-bit unsigned integer value to convert from host byte order to network byte order.
- **Return Value**:
  - Returns the input value converted to network byte order (big-endian). The return value is a 16-bit unsigned integer in network byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. This function is a simple wrapper around the standard `htons` function.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint16_t host_value = 0x1234;
    std::uint16_t network_value = host_to_network(host_value);
    std::cout << "Host value: " << std::hex << host_value << std::endl;
    std::cout << "Network value: " << std::hex << network_value << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 16-bit unsigned integer.
- **Postconditions**: The returned value is the input value converted to network byte order (big-endian).
- **Thread Safety**: This function is thread-safe as it only performs a simple bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `network_to_host`, `host_to_network` (std::uint32_t), `swap_byteorder`

## network_to_host (std::uint16_t)

- **Signature**: `std::uint16_t network_to_host(std::uint16_t x)`
- **Description**: Converts a 16-bit unsigned integer from network byte order (big-endian) to host byte order. This function is used to interpret network data on the local system's byte order.
- **Parameters**:
  - `x` (std::uint16_t): The 16-bit unsigned integer value in network byte order (big-endian) to convert to host byte order.
- **Return Value**:
  - Returns the input value converted to host byte order. The return value is a 16-bit unsigned integer in host byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. This function is a simple wrapper around the standard `ntohs` function.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint16_t network_value = 0x1234;
    std::uint16_t host_value = network_to_host(network_value);
    std::cout << "Network value: " << std::hex << network_value << std::endl;
    std::cout << "Host value: " << std::hex << host_value << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 16-bit unsigned integer in network byte order (big-endian).
- **Postconditions**: The returned value is the input value converted to host byte order.
- **Thread Safety**: This function is thread-safe as it only performs a simple bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `host_to_network`, `network_to_host` (std::uint32_t), `little_endian_to_host`

## swap_byteorder

- **Signature**: `std::uint32_t swap_byteorder(std::uint32_t const x)`
- **Description**: Swaps the byte order of a 32-bit unsigned integer. This function is used to convert between little-endian and big-endian formats, independent of the host's native byte order.
- **Parameters**:
  - `x` (std::uint32_t const): The 32-bit unsigned integer value whose byte order should be swapped.
- **Return Value**:
  - Returns the input value with its bytes swapped. The return value is a 32-bit unsigned integer with reversed byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. This function is a simple bit manipulation operation.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint32_t value = 0x12345678;
    std::uint32_t swapped = swap_byteorder(value);
    std::cout << "Original: " << std::hex << value << std::endl;
    std::cout << "Swapped: " << std::hex << swapped << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 32-bit unsigned integer.
- **Postconditions**: The returned value is the input value with all bytes swapped.
- **Thread Safety**: This function is thread-safe as it only performs a simple bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `little_endian_to_host`, `host_to_network`, `network_to_host`

## little_endian_to_host

- **Signature**: `std::uint32_t little_endian_to_host(std::uint32_t x)`
- **Description**: Converts a 32-bit unsigned integer from little-endian byte order to host byte order. This function is used when the input data is in little-endian format and needs to be converted to the host's native byte order.
- **Parameters**:
  - `x` (std::uint32_t): The 32-bit unsigned integer value in little-endian byte order to convert to host byte order.
- **Return Value**:
  - Returns the input value converted to host byte order. The return value is a 32-bit unsigned integer in host byte order.
- **Exceptions/Errors**:
  - No exceptions are thrown. However, if the system's endianness is neither big nor little, the code will fail to compile due to the `#error` directive.
- **Example**:
```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    std::uint32_t little_endian_value = 0x12345678;
    std::uint32_t host_value = little_endian_to_host(little_endian_value);
    std::cout << "Little-endian value: " << std::hex << little_endian_value << std::endl;
    std::cout << "Host value: " << std::hex << host_value << std::endl;
    return 0;
}
```
- **Preconditions**: The input parameter must be a valid 32-bit unsigned integer in little-endian byte order.
- **Postconditions**: The returned value is the input value converted to host byte order.
- **Thread Safety**: This function is thread-safe as it only performs a conditional bit manipulation.
- **Complexity**: O(1) time and O(1) space complexity.
- **See Also**: `swap_byteorder`, `host_to_network`, `network_to_host`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    // Convert a 32-bit integer from host to network byte order
    std::uint32_t host_value = 0x12345678;
    std::uint32_t network_value = host_to_network(host_value);
    
    // Convert back from network to host byte order
    std::uint32_t restored_value = network_to_host(network_value);
    
    std::cout << "Original: " << std::hex << host_value << std::endl;
    std::cout << "Network: " << std::hex << network_value << std::endl;
    std::cout << "Restored: " << std::hex << restored_value << std::endl;
    
    // For 16-bit values
    std::uint16_t host_value_16 = 0x1234;
    std::uint16_t network_value_16 = host_to_network(host_value_16);
    std::uint16_t restored_value_16 = network_to_host(network_value_16);
    
    std::cout << "16-bit Original: " << std::hex << host_value_16 << std::endl;
    std::cout << "16-bit Network: " << std::hex << network_value_16 << std::endl;
    std::cout << "16-bit Restored: " << std::hex << restored_value_16 << std::endl;
    
    return 0;
}
```

## Error Handling

```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>
#include <stdexcept>

int main() {
    try {
        // In this case, there's no runtime error to catch since these functions
        // don't throw exceptions. However, we can demonstrate proper usage
        // of the functions in a robust application.
        
        std::uint32_t host_value = 0x12345678;
        std::uint32_t network_value = host_to_network(host_value);
        
        // Simulate receiving network data (in network byte order)
        std::uint32_t received_network_value = network_value;
        
        // Convert to host byte order for processing
        std::uint32_t processed_value = network_to_host(received_network_value);
        
        if (processed_value != host_value) {
            std::cerr << "Byte order conversion error: values don't match" << std::endl;
            return 1;
        }
        
        std::cout << "Byte order conversion successful: " << std::hex << processed_value << std::endl;
        
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Exception occurred: " << e.what() << std::endl;
        return 1;
    }
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/byteswap.hpp>
#include <iostream>

int main() {
    // Test with all possible values
    std::cout << "Testing byte order conversion with edge cases:" << std::endl;
    
    // Test with zero
    std::uint32_t zero = 0x00000000;
    std::uint32_t zero_network = host_to_network(zero);
    std::uint32_t zero_host = network_to_host(zero_network);
    std::cout << "Zero: " << std::hex << zero << " -> " << zero_network << " -> " << zero_host << std::endl;
    
    // Test with maximum value
    std::uint32_t max_value = 0xFFFFFFFF;
    std::uint32_t max_network = host_to_network(max_value);
    std::uint32_t max_host = network_to_host(max_network);
    std::cout << "Max value: " << std::hex << max_value << " -> " << max_network << " -> " << max_host << std::endl;
    
    // Test with minimum value
    std::uint32_t min_value = 0x00000001;
    std::uint32_t min_network = host_to_network(min_value);
    std::uint32_t min_host = network_to_host(min_network);
    std::cout << "Min value: " << std::hex << min_value << " -> " << min_network << " -> " << min_host << std::endl;
    
    // Test with mixed endianness
    std::uint32_t mixed = 0x12345678;
    std::uint32_t mixed_swapped = swap_byteorder(mixed);
    std::cout << "Mixed endianness: " << std::hex << mixed << " -> " << mixed_swapped << std::endl;
    
    // Test with little endian to host conversion
    std::uint32_t little_endian = 0x12345678;
    std::uint32_t host_converted = little_endian_to_host(little_endian);
    std::cout << "Little endian to host: " << std::hex << little_endian << " -> " << host_converted << std::endl;
    
    return 0;
}
```

# Best Practices

1. **Use the appropriate function based on the context**:
   - Use `host_to_network` and `network_to_host` for network communication
   - Use `swap_byteorder` when you need to convert between endianness regardless of the network
   - Use `little_endian_to_host` when you specifically need to convert from little-endian to host

2. **Always consider the host architecture**:
   - Be aware of whether your system is little-endian or big-endian
   - Use `BOOST_ENDIAN_BIG_BYTE` and `BOOST_ENDIAN_LITTLE_BYTE` macros to determine endianness

3. **Avoid unnecessary conversions**:
   - Only convert when necessary for network communication or data storage
   - Don't convert back and forth unnecessarily

4. **Handle endianness consistently**:
   - Ensure that all systems in your network communication use the same byte order
   - Use network byte order (big-endian) as the standard for data transmission

5. **Use constexpr where possible**:
   - These functions can be marked as constexpr if they're used at compile time

6. **Avoid magic numbers**:
   - Use hexadecimal notation for byte manipulation to make the code more readable

# Code Review & Improvement Suggestions

## Function: `host_to_network (std::uint32_t)`

**Issue**: No return value checking for overflow or other issues
**Severity**: Low
**Impact**: The function is a simple wrapper around `htonl`, which doesn't return errors. No practical impact.
**Fix**: No fix needed as this is standard behavior.

## Function: `network_to_host (std::uint32_t)`

**Issue**: No return value checking for overflow or other issues
**Severity**: Low
**Impact**: The function is a simple wrapper around `ntohl`, which doesn't return errors. No practical impact.
**Fix**: No fix needed as this is standard behavior.

## Function: `host_to_network (std::uint16_t)`

**Issue**: No return value checking for overflow or