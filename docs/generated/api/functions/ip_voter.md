# libtorrent IP Voter API Documentation

## ip_voter

- **Signature**: `ip_voter()`
- **Description**: Constructs a new ip_voter object. This voter is responsible for tracking and determining the external IP address of the system by aggregating votes from various sources. The voter maintains a voting system where different IP addresses can receive votes based on their source type and reliability.
- **Parameters**: None
- **Return Value**: Returns a new instance of the ip_voter class.
- **Exceptions/Errors**: None
- **Example**:
```cpp
ip_voter voter;
```
- **Preconditions**: None
- **Postconditions**: A new ip_voter object is created and ready to receive votes.
- **Thread Safety**: The constructor is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `cast_vote()`, `external_address()`

## cast_vote

- **Signature**: `bool cast_vote(address const& ip, aux::ip_source_t source_type, address const& source)`
- **Description**: Casts a vote for a given IP address from a specific source. The function evaluates whether the provided IP address should be considered the current external address by comparing it with the current top vote. Returns true if the top vote has changed (i.e., a different IP is now considered the external IP).
- **Parameters**:
  - `ip` (address const&): The IP address being voted for. This should be a valid IP address (IPv4 or IPv6). The function will validate the address and ensure it's not a loopback or private address.
  - `source_type` (aux::ip_source_t): The type of source providing the IP address (e.g., NAT-PMP, UPnP, STUN, etc.). This determines the reliability and weight of the vote.
  - `source` (address const&): The address of the source that provided the IP. This is used for additional validation and to prevent spoofing.
- **Return Value**:
  - `true`: The top vote has changed, indicating that the external IP address has been updated.
  - `false`: The top vote remains unchanged.
- **Exceptions/Errors**: None
- **Example**:
```cpp
ip_voter voter;
address ip("192.168.1.100");
aux::ip_source_t source_type = aux::ip_source_t::upnp;
address source("192.168.1.1");
bool changed = voter.cast_vote(ip, source_type, source);
if (changed) {
    std::cout << "External IP has changed!" << std::endl;
}
```
- **Preconditions**: The `ip` and `source` addresses must be valid and not null.
- **Postconditions**: The vote is recorded, and the top vote may have changed.
- **Thread Safety**: The function is thread-safe and can be called from multiple threads simultaneously.
- **Complexity**: O(log n) time complexity due to the internal sorting and comparison of votes.
- **See Also**: `external_address()`, `external_ip`

## external_address

- **Signature**: `address external_address() const`
- **Description**: Returns the current external IP address as determined by the ip_voter. This is the IP address that is considered the most reliable based on the voting system.
- **Parameters**: None
- **Return Value**: The current external IP address as an `address` object. This can be either an IPv4 or IPv6 address depending on the system configuration.
- **Exceptions/Errors**: None
- **Example**:
```cpp
ip_voter voter;
// ... votes have been cast
address external = voter.external_address();
std::cout << "External IP: " << external.to_string() << std::endl;
```
- **Preconditions**: The ip_voter must have received at least one valid vote.
- **Postconditions**: The returned address is the most reliable external IP address based on the current voting state.
- **Thread Safety**: The function is thread-safe and can be called from multiple threads simultaneously.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `cast_vote()`, `ip_voter`

## operator<

- **Signature**: `bool operator<(external_ip_t const& rhs) const`
- **Description**: Compares the current external IP vote with another external IP vote. The comparison is based on the number of votes first, then on the source type if the vote counts are equal. This operator is used to sort external IP votes in a priority queue or similar data structure.
- **Parameters**:
  - `rhs` (external_ip_t const&): The external IP vote to compare against.
- **Return Value**:
  - `true`: The current vote is considered "less than" the right-hand side vote.
  - `false`: The current vote is not considered "less than" the right-hand side vote.
- **Exceptions/Errors**: None
- **Example**:
```cpp
external_ip_t vote1, vote2;
bool less = vote1 < vote2;
```
- **Preconditions**: None
- **Postconditions**: The comparison result is returned based on the defined ordering rules.
- **Thread Safety**: The function is thread-safe and can be called from multiple threads simultaneously.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `external_ip`, `external_ip_t`

## external_ip (constructor)

- **Signature**: `external_ip()`
- **Description**: Constructs a new external_ip object with default values. This constructor initializes the internal address storage with empty IPv4 and IPv6 addresses for both local and external addresses.
- **Parameters**: None
- **Return Value**: Returns a new instance of the external_ip class with default values.
- **Exceptions/Errors**: None
- **Example**:
```cpp
external_ip ip;
```
- **Preconditions**: None
- **Postconditions**: A new external_ip object is created with all addresses initialized to empty values.
- **Thread Safety**: The constructor is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `external_ip(address const& local4, address const& global4, address const& local6, address const& global6)`

## external_ip (constructor)

- **Signature**: `external_ip(address const& local4, address const& global4, address const& local6, address const& global6)`
- **Description**: Constructs a new external_ip object with the specified local and external addresses for both IPv4 and IPv6. This constructor is used when you have explicit information about the local and external addresses.
- **Parameters**:
  - `local4` (address const&): The local IPv4 address.
  - `global4` (address const&): The external IPv4 address.
  - `local6` (address const&): The local IPv6 address.
  - `global6` (address const&): The external IPv6 address.
- **Return Value**: Returns a new instance of the external_ip class with the specified addresses.
- **Exceptions/Errors**: None
- **Example**:
```cpp
address local4("192.168.1.100");
address global4("1.2.3.4");
address local6("fe80::1");
address global6("2001:db8::1");
external_ip ip(local4, global4, local6, global6);
```
- **Preconditions**: All address parameters must be valid.
- **Postconditions**: A new external_ip object is created with the specified addresses.
- **Thread Safety**: The constructor is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `external_ip()` (default constructor)

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/ip_voter.hpp"
#include "libtorrent/address.hpp"
#include "libtorrent/aux.hpp"

int main() {
    // Create a new ip_voter
    ip_voter voter;
    
    // Cast votes from different sources
    address ip1("192.168.1.100");
    address ip2("1.2.3.4");
    address source("192.168.1.1");
    
    voter.cast_vote(ip1, aux::ip_source_t::upnp, source);
    voter.cast_vote(ip2, aux::ip_source_t::stun, source);
    
    // Get the current external IP
    address external = voter.external_address();
    std::cout << "Current external IP: " << external.to_string() << std::endl;
    
    return 0;
}
```

## Error Handling

```cpp
#include "libtorrent/ip_voter.hpp"
#include "libtorrent/address.hpp"
#include "libtorrent/aux.hpp"
#include <iostream>

int main() {
    try {
        ip_voter voter;
        
        // Cast a vote with invalid IP (this would typically be caught by validation)
        address invalid_ip("invalid");
        if (invalid_ip.is_valid()) {
            voter.cast_vote(invalid_ip, aux::ip_source_t::upnp, address("192.168.1.1"));
        } else {
            std::cerr << "Invalid IP address provided" << std::endl;
        }
        
        // Get the external address
        address external = voter.external_address();
        if (external.is_valid()) {
            std::cout << "External IP: " << external.to_string() << std::endl;
        } else {
            std::cerr << "No valid external IP found" << std::endl;
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Exception occurred: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include "libtorrent/ip_voter.hpp"
#include "libtorrent/address.hpp"
#include "libtorrent/aux.hpp"
#include <iostream>

int main() {
    ip_voter voter;
    
    // Test with loopback addresses
    address loopback_v4("127.0.0.1");
    address loopback_v6("::1");
    
    voter.cast_vote(loopback_v4, aux::ip_source_t::upnp, address("192.168.1.1"));
    voter.cast_vote(loopback_v6, aux::ip_source_t::stun, address("192.168.1.1"));
    
    // Test with private addresses
    address private_v4("192.168.1.100");
    address private_v6("fe80::1");
    
    voter.cast_vote(private_v4, aux::ip_source_t::upnp, address("192.168.1.1"));
    voter.cast_vote(private_v6, aux::ip_source_t::stun, address("192.168.1.1"));
    
    // Test with public addresses
    address public_v4("1.2.3.4");
    address public_v6("2001:db8::1");
    
    voter.cast_vote(public_v4, aux::ip_source_t::upnp, address("192.168.1.1"));
    voter.cast_vote(public_v6, aux::ip_source_t::stun, address("192.168.1.1"));
    
    // The external address should be the most reliable public address
    address external = voter.external_address();
    std::cout << "Final external IP: " << external.to_string() << std::endl;
    
    return 0;
}
```

# Best Practices

## How to Use These Functions Effectively

1. **Initialize the ip_voter**: Always create an ip_voter object before casting any votes.
2. **Use appropriate source types**: Different source types have different reliability. Use the most reliable source available.
3. **Validate IP addresses**: Always validate IP addresses before casting votes to ensure they are valid and not private or loopback addresses.
4. **Handle multiple sources**: Cast votes from multiple sources to increase the reliability of the external IP detection.
5. **Check the return value of cast_vote**: Use the return value to detect when the external IP has changed.
6. **Use external_address() for the final IP**: This function provides the most reliable external IP address based on the voting system.

## Common Mistakes to Avoid

1. **Using invalid IP addresses**: Always validate IP addresses before casting votes.
2. **Not handling the return value of cast_vote**: The return value indicates if the external IP has changed, so it should be checked.
3. **Using the wrong source type**: Use the correct source type to ensure the vote is properly weighted.
4. **Not considering IPv6**: Always consider both IPv4 and IPv6 addresses when determining the external IP.
5. **Not initializing the ip_voter**: Ensure the ip_voter is properly initialized before use.

## Performance Tips

1. **Use const references**: Use const references for parameters to avoid unnecessary copies.
2. **Minimize function calls**: Cache results when possible to avoid redundant function calls.
3. **Use move semantics**: Use move semantics for large objects when appropriate.
4. **Avoid unnecessary allocations**: Reuse objects when possible to reduce memory allocations.
5. **Use appropriate data structures**: Use efficient data structures for storing and sorting IP addresses.

# Code Review & Improvement Suggestions

## Potential Issues

### **Function**: `ip_voter()`
**Issue**: No documentation for the constructor parameters
**Severity**: Low
**Impact**: Could lead to confusion about how to use the constructor
**Fix**: Add documentation for the constructor parameters

### **Function**: `cast_vote`
**Issue**: No input validation for the ip parameter
**Severity**: Medium
**Impact**: Could lead to invalid IP addresses being used, potentially causing issues
**Fix**: Add input validation for the ip parameter:
```cpp
bool cast_vote(address const& ip, aux::ip_source_t source_type, address const& source) {
    if (!ip.is_valid()) {
        return false; // or throw an exception
    }
    // ... rest of the function
}
```

### **Function**: `external_address`
**Issue**: No documentation for the return value
**Severity**: Low
**Impact**: Could lead to confusion about what the function returns
**Fix**: Add documentation for the return value

### **Function**: `operator<`
**Issue**: No documentation for the comparison criteria
**Severity**: Low
**Impact**: Could lead to confusion about how the comparison works
**Fix**: Add documentation for the comparison criteria

### **Function**: `external_ip` (constructor)
**Issue**: No documentation for the constructor parameters
**Severity**: Low
**Impact**: Could lead to confusion about how to use the constructor
**Fix**: Add documentation for the constructor parameters

### **Function**: `external_ip` (constructor)
**Issue**: No documentation for the constructor parameters
**Severity**: Low
**Impact**: Could lead to confusion about how to use the constructor
**Fix**: Add documentation for the constructor parameters

## Modernization Opportunities

### **Function**: `ip_voter()`
**Opportunity**: Use `[[nodiscard]]` for functions that return important values
**Suggestion**: Add `[[nodiscard]]` to the constructor if it's intended to be used for important operations

### **Function**: `cast_vote`
**Opportunity**: Use `std::span` for array parameters
**Suggestion**: Consider using `std::span` if the function were to accept arrays of addresses

### **Function**: `external_address`
**Opportunity**: Use `std::expected` (C++23) for error handling
**Suggestion**: Consider using `std::expected` if the function were to return an error code

### **Function**: `operator<`
**Opportunity**: Use `std::strong_ordering` (C++20) for comparison
**Suggestion**: Consider using `std::strong_ordering` if the function were to return a more detailed comparison result

## Refactoring Suggestions

### **Function**: `ip_voter`
**Suggestion**: Split the ip_voter class into smaller, more focused classes
**Reason**: The ip_voter class might be doing too much. Consider separating the voting logic from the external IP determination.

### **Function**: `cast_vote`
**Suggestion**: Move the voting logic to a separate class
**Reason**: The voting logic might be reused in other contexts and could benefit from being in a separate class.

### **Function**: `external_address`
**Suggestion**: Move the external address determination to a separate class
**Reason**: The external address determination might be reused in other contexts and could benefit from being in a separate class.

## Performance Optimizations

### **Function**: `ip_voter()`
**Optimization**: Use move semantics for initialization
**Suggestion**: Consider using move semantics when initializing the ip_voter object

### **Function**: `cast_vote`
**Optimization**: Use return by value for RVO
**Suggestion**: Consider using return by value for RVO if the function were to return a large object

### **Function**: `external_address`
**Optimization**: Use string_view for read-only strings
**Suggestion**: Consider using `std::string_view` for the return value if it were to return a string

### **Function**: `operator<`
**Optimization**: Add noexcept where applicable
**Suggestion**: Consider adding `noexcept` to the operator if it's guaranteed to not throw exceptions