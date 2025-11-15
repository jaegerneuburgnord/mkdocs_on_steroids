# C++ API Documentation: IP Filter Binding Functions

## add_rule

- **Signature**: `void add_rule(ip_filter& filter, std::string start, std::string end, int flags)`
- **Description**: Adds a new IP address rule to the IP filter. The rule specifies a range of IP addresses (from `start` to `end`) with associated flags that determine how the rule should be applied. This function is typically used to define which IP addresses are allowed or blocked by the filter.
- **Parameters**:
  - `filter` (ip_filter&): Reference to the IP filter object where the rule will be added. The filter must be valid and initialized.
  - `start` (std::string): String representation of the starting IP address of the range. Must be a valid IPv4 or IPv6 address in standard format (e.g., "192.168.1.1" or "2001:db8::1"). The address must be valid and convertible to an IP address.
  - `end` (std::string): String representation of the ending IP address of the range. Must be a valid IPv4 or IPv6 address in standard format. The address must be valid and convertible to an IP address.
  - `flags` (int): Flags that determine the behavior of the rule. Valid values depend on the implementation but typically include combinations of access control flags (e.g., allow, deny, etc.).
- **Return Value**:
  - This function returns `void`. It does not return a value, but modifies the filter object in place.
- **Exceptions/Errors**:
  - Could throw an exception if the IP addresses are invalid (e.g., malformed strings).
  - Could throw an exception if the conversion from string to IP address fails.
  - Could throw an exception if the `flags` parameter is invalid.
  - In some implementations, could throw a `std::runtime_error` or `std::invalid_argument` exception.
- **Example**:
```cpp
// Add a rule to allow traffic from 192.168.1.0 to 192.168.1.255
ip_filter filter;
add_rule(filter, "192.168.1.0", "192.168.1.255", 0); // 0 typically means allow
```
- **Preconditions**:
  - The `filter` object must be valid and initialized.
  - The `start` and `end` strings must be valid IP address strings.
  - The `flags` parameter must be a valid value for the IP filter implementation.
- **Postconditions**:
  - The filter will contain the new rule.
  - The filter's internal state will be updated to reflect the new rule.
- **Thread Safety**:
  - This function is not thread-safe. Concurrent access to the same `ip_filter` object from multiple threads may lead to undefined behavior.
- **Complexity**:
  - Time: O(1) - assuming the underlying data structure is efficient.
  - Space: O(1) - constant additional space for storing the rule.
- **See Also**: `access0`, `export_filter`

## access0

- **Signature**: `int access0(ip_filter& filter, std::string addr)`
- **Description**: Checks the access level for a given IP address according to the filter rules. Returns a value indicating whether the IP address is allowed, denied, or has some other access level. This function is typically used to determine if an incoming connection should be accepted or rejected based on the filter rules.
- **Parameters**:
  - `filter` (ip_filter&): Reference to the IP filter object to check against. The filter must be valid and initialized.
  - `addr` (std::string): String representation of the IP address to check. Must be a valid IPv4 or IPv6 address in standard format (e.g., "192.168.1.1" or "2001:db8::1").
- **Return Value**:
  - Returns an integer value indicating the access level:
    - 0: Access is allowed (or the address matches an allow rule).
    - 1: Access is denied (or the address matches a deny rule).
    - Other values: May represent different access levels or error conditions (implementation-specific).
  - The exact meaning of return values depends on the specific IP filter implementation.
- **Exceptions/Errors**:
  - Could throw an exception if the `addr` string is invalid (e.g., malformed IP address).
  - Could throw an exception if the IP address cannot be converted to a valid address.
  - In some implementations, could throw a `std::invalid_argument` exception.
- **Example**:
```cpp
ip_filter filter;
// Configure the filter with rules...
int result = access0(filter, "192.168.1.10");
if (result == 0) {
    std::cout << "Access granted" << std::endl;
} else {
    std::cout << "Access denied" << std::endl;
}
```
- **Preconditions**:
  - The `filter` object must be valid and initialized.
  - The `addr` string must be a valid IP address string.
- **Postconditions**:
  - The filter's state is unchanged.
  - The function returns the access level for the specified IP address.
- **Thread Safety**:
  - This function is thread-safe if the `ip_filter` object is not modified by other threads during the call. It only reads the filter's state.
- **Complexity**:
  - Time: O(log n) - where n is the number of rules, assuming the filter uses a binary search or similar efficient lookup.
  - Space: O(1) - constant additional space.
- **See Also**: `add_rule`, `export_filter`

## convert_range_list

- **Signature**: `list convert_range_list(std::vector<ip_range<T>> const& l)`
- **Description**: Converts a vector of IP range objects into a Python list of tuples. Each tuple contains the string representations of the start and end IP addresses of the range. This function is used as a helper for converting C++ IP range data to Python format during binding.
- **Parameters**:
  - `l` (std::vector<ip_range<T>> const&): Reference to the vector of IP range objects to convert. The vector must be valid and contain valid IP range objects.
- **Return Value**:
  - Returns a Python `list` object containing tuples. Each tuple has two elements:
    - First element: String representation of the start IP address.
    - Second element: String representation of the end IP address.
  - The list contains one tuple for each IP range in the input vector.
- **Exceptions/Errors**:
  - Could throw an exception if the conversion of IP addresses to strings fails (unlikely, as it uses `to_string()`).
  - In some implementations, could throw a `std::bad_alloc` exception if memory allocation fails.
- **Example**:
```cpp
std::vector<ip_range<ip_address>> ranges = {{ip_address("192.168.1.0"), ip_address("192.168.1.255")}};
list result = convert_range_list(ranges);
// result is now a list with one tuple: [("192.168.1.0", "192.168.1.255")]
```
- **Preconditions**:
  - The input vector must be valid and contain valid IP range objects.
  - The IP addresses in the ranges must be convertible to strings.
- **Postconditions**:
  - A new Python list is created with the converted data.
  - The input vector is unchanged.
- **Thread Safety**:
  - This function is thread-safe as it only reads the input data.
- **Complexity**:
  - Time: O(n) - where n is the number of ranges.
  - Space: O(n) - for the output list.
- **See Also**: `export_filter`

## export_filter

- **Signature**: `tuple export_filter(ip_filter const& f)`
- **Description**: Exports the current IP filter configuration as a tuple containing separate lists of IPv4 and IPv6 ranges. This function is typically used to save or serialize the filter configuration. It calls the filter's internal `export_filter` method and converts the result to Python format.
- **Parameters**:
  - `f` (ip_filter const&): Reference to the IP filter object to export. The filter must be valid and initialized.
- **Return Value**:
  - Returns a Python `tuple` with two elements:
    - First element: A Python `list` of IPv4 range tuples (each tuple contains start and end IP addresses as strings).
    - Second element: A Python `list` of IPv6 range tuples (each tuple contains start and end IP addresses as strings).
  - The returned tuple represents the complete filter configuration.
- **Exceptions/Errors**:
  - Could throw an exception if the filter's internal `export_filter` method fails.
  - Could throw an exception if the conversion of IP addresses to strings fails.
  - In some implementations, could throw a `std::bad_alloc` exception if memory allocation fails.
- **Example**:
```cpp
ip_filter filter;
// Configure the filter...
tuple result = export_filter(filter);
list ipv4_ranges = boost::python::extract<list>(result[0]);
list ipv6_ranges = boost::python::extract<list>(result[1]);
// Process the exported ranges...
```
- **Preconditions**:
  - The `f` object must be valid and initialized.
- **Postconditions**:
  - The returned tuple contains the exported filter configuration.
  - The input filter object is unchanged.
- **Thread Safety**:
  - This function is thread-safe if the `ip_filter` object is not modified by other threads during the call. It only reads the filter's state.
- **Complexity**:
  - Time: O(n) - where n is the total number of ranges in the filter.
  - Space: O(n) - for the output tuple and lists.
- **See Also**: `add_rule`, `access0`

## bind_ip_filter

- **Signature**: `void bind_ip_filter()`
- **Description**: Binds the `ip_filter` class to the Python binding system (likely using Boost.Python). This function creates a Python interface for the `ip_filter` class, exposing its methods (`add_rule`, `access`, `export_filter`) to Python code. This is a binding function that is typically called once during program initialization.
- **Parameters**:
  - None
- **Return Value**:
  - This function returns `void`. It does not return a value.
- **Exceptions/Errors**:
  - Could throw an exception if the binding process fails (e.g., memory allocation failure, type system errors).
  - In some implementations, could throw a `boost::python::error_already_set` exception if there are binding errors.
- **Example**:
```cpp
// Called during program initialization to expose ip_filter to Python
bind_ip_filter();
```
- **Preconditions**:
  - The Boost.Python library must be properly initialized.
  - The `ip_filter` class and its methods must be defined and accessible.
  - The binding function must be called before any Python code tries to use the `ip_filter` class.
- **Postconditions**:
  - The `ip_filter` class is exposed to Python with the specified methods.
  - Python code can create `ip_filter` instances and call the bound methods.
- **Thread Safety**:
  - This function is not thread-safe. It should be called only once, typically during program initialization, and not concurrently.
- **Complexity**:
  - Time: O(1) - assuming the binding system is efficient.
  - Space: O(1) - constant additional space for the binding metadata.
- **See Also**: `ip_filter`, `add_rule`, `access0`, `export_filter`

# Usage Examples

## Basic Usage

```cpp
#include "ip_filter.hpp"
#include <boost/python.hpp>
#include <iostream>

// Initialize the binding
bind_ip_filter();

// Create a new IP filter
ip_filter filter;

// Add rules to allow traffic from a specific range
add_rule(filter, "192.168.1.0", "192.168.1.255", 0); // 0 means allow

// Check access for an IP address
int result = access0(filter, "192.168.1.10");
if (result == 0) {
    std::cout << "Access granted to 192.168.1.10" << std::endl;
} else {
    std::cout << "Access denied to 192.168.1.10" << std::endl;
}

// Export the filter configuration
tuple exported = export_filter(filter);
// The exported data can now be used in Python code
```

## Error Handling

```cpp
#include <iostream>
#include <stdexcept>

try {
    ip_filter filter;
    add_rule(filter, "192.168.1.0", "192.168.1.255", 0);
    int result = access0(filter, "192.168.1.10");
    if (result != 0) {
        std::cout << "Access denied" << std::endl;
    }
} catch (const std::invalid_argument& e) {
    std::cerr << "Invalid IP address: " << e.what() << std::endl;
} catch (const std::exception& e) {
    std::cerr << "Other error: " << e.what() << std::endl;
}
```

## Edge Cases

```cpp
#include <iostream>

// Test with invalid IP addresses
try {
    ip_filter filter;
    add_rule(filter, "invalid", "192.168.1.255", 0); // Should throw
} catch (const std::invalid_argument& e) {
    std::cout << "Caught expected exception: " << e.what() << std::endl;
}

// Test with overlapping ranges
ip_filter filter;
add_rule(filter, "192.168.1.0", "192.168.1.255", 0);
add_rule(filter, "192.168.1.100", "192.168.1.200", 1); // 1 might mean deny
// The behavior depends on the filter implementation (priority rules, etc.)

// Test with IPv6 addresses
ip_filter ipv6_filter;
add_rule(ipv6_filter, "2001:db8::1", "2001:db8::ff", 0);
```

# Best Practices

1. **Use appropriate flags**: Always ensure that the flags parameter in `add_rule` is set correctly for the intended access control behavior.

2. **Validate IP addresses**: Always validate IP addresses before passing them to functions, or handle exceptions appropriately.

3. **Initialize properly**: Ensure the `ip_filter` object is properly initialized before using any of its methods.

4. **Thread safety**: Be aware that the `ip_filter` object is not thread-safe. Use proper synchronization if multiple threads need to access it.

5. **Error handling**: Always handle exceptions when working with IP address strings, as invalid IP addresses can cause runtime errors.

6. **Performance**: For high-frequency access checks, consider caching or optimizing the filter structure to reduce lookup times.

7. **Keep filters simple**: Avoid creating too many rules that overlap, as this can impact performance and make the filter logic harder to understand.

8. **Use const references**: When possible, use `const&` parameters to avoid unnecessary copying of objects.

# Code Review & Improvement Suggestions

## Potential Issues

### Function: `add_rule`
**Issue**: No input validation for IP address strings
**Severity**: Medium
**Impact**: Invalid IP addresses could lead to runtime exceptions or undefined behavior
**Fix**: Add validation for IP address strings before conversion:
```cpp
void add_rule(ip_filter& filter, std::string start, std::string end, int flags) {
    if (start.empty() || end.empty()) {
        throw std::invalid_argument("IP addresses cannot be empty");
    }
    // Validate IP format if possible
    try {
        filter.add_rule(make_address(start), make_address(end), flags);
    } catch (const std::exception& e) {
        throw std::invalid_argument("Invalid IP address format");
    }
}
```

### Function: `access0`
**Issue**: No input validation for IP address string
**Severity**: Medium
**Impact**: Invalid IP addresses could lead to runtime exceptions or undefined behavior
**Fix**: Add validation for IP address string:
```cpp
int access0(ip_filter& filter, std::string addr) {
    if (addr.empty()) {
        throw std::invalid_argument("IP address cannot be empty");
    }
    try {
        return filter.access(make_address(addr));
    } catch (const std::exception& e) {
        throw std::invalid_argument("Invalid IP address format");
    }
}
```

### Function: `convert_range_list`
**Issue**: No bounds checking on the vector
**Severity**: Low
**Impact**: Could cause undefined behavior if the vector is invalid
**Fix**: The function already takes a const reference, so it's relatively safe. Consider adding a check for valid vector:
```cpp
list convert_range_list(std::vector<ip_range<T>> const& l) {
    if (l.empty()) {
        return list();
    }
    list ret;
    for (auto const& r : l)
        ret.append(boost::python::make_tuple(r.first.to_string(), r.last.to_string()));
    return ret;
}
```

### Function: `export_filter`
**Issue**: No error handling if `export_filter` fails
**Severity**: Medium
**Impact**: Could cause program crash or undefined behavior
**Fix**: Add try-catch block:
```cpp
tuple export_filter(ip_filter const& f) {
    try {
        auto ret = f.export_filter();
        list ipv4 = convert_range_list(std::get<0>(ret));
        list ipv6 = convert_range_list(std::get<1>(ret));
        return boost::python::make_tuple(ipv4, ipv6);
    } catch (const std::exception& e) {
        throw std::runtime_error("Failed to export filter: " + std::string(e.what()));
    }
}
```

### Function: `bind_ip_filter`
**Issue**: No error handling for binding