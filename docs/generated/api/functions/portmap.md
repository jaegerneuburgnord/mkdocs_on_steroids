# API Documentation

## portmap_callback

- **Signature**: `virtual ~portmap_callback()`
- **Description**: This is a pure virtual base class for port mapping callbacks in libtorrent. It defines the interface for receiving notifications about port mapping operations, such as when a port is successfully mapped or when an error occurs. This class is intended to be derived from by user code to handle port mapping events.
- **Parameters**: 
  - This is a base class and has no parameters in its destructor.
- **Return Value**: 
  - The destructor returns nothing.
- **Exceptions/Errors**: 
  - This is a virtual destructor and does not throw exceptions.
- **Example**:
```cpp
class MyPortmapCallback : public portmap_callback
{
public:
    void on_portmap(int mapping_index, address const& ext_addr, int ext_port, int protocol, error_code const& ec, int transport) override
    {
        // Handle port mapping event
        std::cout << "Port mapped: " << ext_port << std::endl;
    }
};
```
- **Preconditions**: The derived class must implement all pure virtual functions from this base class.
- **Postconditions**: The object is properly destroyed and any cleanup is performed.
- **Thread Safety**: This function is thread-safe when properly implemented in the derived class.
- **Complexity**: O(1) - Constant time complexity.
- **See Also**: `portmap_protocol`, `portmap_action`, `portmap_callback::on_portmap`

## to_string (portmap_protocol)

- **Signature**: `inline char const* to_string(portmap_protocol const p)`
- **Description**: Converts a `portmap_protocol` enum value to its corresponding string representation. This function is useful for debugging or logging purposes, allowing developers to display human-readable protocol names (UDP or TCP).
- **Parameters**: 
  - `p` (portmap_protocol): The protocol to convert to string. Valid values are `portmap_protocol::udp` and `portmap_protocol::tcp`.
- **Return Value**: 
  - Returns a pointer to a null-terminated C-style string.
  - Returns "UDP" for `portmap_protocol::udp`.
  - Returns "TCP" for `portmap_protocol::tcp`.
- **Exceptions/Errors**: 
  - No exceptions are thrown.
- **Example**:
```cpp
auto protocol = portmap_protocol::udp;
auto protocol_str = to_string(protocol);
std::cout << "Protocol: " << protocol_str << std::endl; // Output: Protocol: UDP
```
- **Preconditions**: The input parameter `p` must be a valid `portmap_protocol` enum value.
- **Postconditions**: The returned string is valid and remains valid for the duration of the program.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1) - Constant time complexity.
- **See Also**: `to_string(portmap_action)`, `portmap_protocol`

## to_string (portmap_action)

- **Signature**: `inline char const* to_string(portmap_action const act)`
- **Description**: Converts a `portmap_action` enum value to its corresponding string representation. This function is useful for debugging or logging purposes, allowing developers to display human-readable action names (none, add, delete).
- **Parameters**: 
  - `act` (portmap_action): The action to convert to string. Valid values are `portmap_action::none`, `portmap_action::add`, and `portmap_action::del`.
- **Return Value**: 
  - Returns a pointer to a null-terminated C-style string.
  - Returns "none" for `portmap_action::none`.
  - Returns "add" for `portmap_action::add`.
  - Returns "delete" for `portmap_action::del`.
- **Exceptions/Errors**: 
  - No exceptions are thrown.
- **Example**:
```cpp
auto action = portmap_action::add;
auto action_str = to_string(action);
std::cout << "Action: " << action_str << std::endl; // Output: Action: add
```
- **Preconditions**: The input parameter `act` must be a valid `portmap_action` enum value.
- **Postconditions**: The returned string is valid and remains valid for the duration of the program.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1) - Constant time complexity.
- **See Also**: `to_string(portmap_protocol)`, `portmap_action`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/portmap.hpp>
#include <iostream>

int main() {
    // Convert protocol enum to string
    auto protocol_str = to_string(portmap_protocol::udp);
    std::cout << "Protocol: " << protocol_str << std::endl; // Output: Protocol: UDP
    
    // Convert action enum to string
    auto action_str = to_string(portmap_action::add);
    std::cout << "Action: " << action_str << std::endl; // Output: Action: add
    
    return 0;
}
```

## Error Handling

```cpp
#include <libtorrent/aux_/portmap.hpp>
#include <iostream>

int main() {
    // Use the functions in a safe manner
    try {
        // The functions are safe and don't throw exceptions
        auto protocol_str = to_string(portmap_protocol::udp);
        auto action_str = to_string(portmap_action::add);
        
        std::cout << "Protocol: " << protocol_str << std::endl;
        std::cout << "Action: " << action_str << std::endl;
        
        // Verify the strings are valid
        if (protocol_str && action_str) {
            std::cout << "Success: Strings are valid" << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/portmap.hpp>
#include <iostream>

int main() {
    // Test with all possible enum values
    std::cout << "Testing all protocol values:" << std::endl;
    for (int i = 0; i <= 1; ++i) {
        auto p = static_cast<portmap_protocol>(i);
        auto str = to_string(p);
        std::cout << "portmap_protocol::" << (i == 0 ? "udp" : "tcp") << " -> " << str << std::endl;
    }
    
    std::cout << "\nTesting all action values:" << std::endl;
    for (int i = 0; i <= 2; ++i) {
        auto act = static_cast<portmap_action>(i);
        auto str = to_string(act);
        std::cout << "portmap_action::" << (i == 0 ? "none" : i == 1 ? "add" : "del") << " -> " << str << std::endl;
    }
    
    return 0;
}
```

# Best Practices

## How to Use These Functions Effectively

1. **Use for Debugging and Logging**: These functions are particularly useful for debugging and logging port mapping operations, providing clear human-readable output.
2. **Combine with Other Functions**: Use these functions in conjunction with `portmap_callback` to provide detailed information about port mapping events.
3. **Use in Error Messages**: Incorporate these functions in error messages to provide context about what protocol or action caused an issue.

## Common Mistakes to Avoid

1. **Assuming String Validity**: Don't assume the returned string is valid without checking. While these functions are safe, always validate the output in production code.
2. **Ignoring Return Values**: Always check the return values of these functions, especially in error handling scenarios.
3. **Using in Performance-Critical Code**: These functions involve string lookups and should be used sparingly in performance-critical sections of code.

## Performance Tips

1. **Cache Results**: If you need to convert the same enum value multiple times, cache the result rather than calling the function repeatedly.
2. **Avoid in Tight Loops**: Don't call these functions in tight loops where performance is critical, as they involve string lookups.
3. **Use for Debugging Only**: These functions are best suited for debugging and logging, not for core functionality.

# Code Review & Improvement Suggestions

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `to_string(portmap_protocol)`
**Issue**: The function uses a simple conditional to return strings, but doesn't validate the input parameter.
**Severity**: Low
**Impact**: Could potentially return unexpected results if the input is invalid.
**Fix**: Add input validation to ensure the parameter is a valid enum value:

```cpp
inline char const* to_string(portmap_protocol const p)
{
    if (p == portmap_protocol::udp) return "UDP";
    if (p == portmap_protocol::tcp) return "TCP";
    return "unknown";
}
```

**Function**: `to_string(portmap_action)`
**Issue**: The function doesn't handle the default case explicitly, which could lead to undefined behavior if the input is invalid.
**Severity**: Low
**Impact**: Could return an empty string or undefined behavior if the input is invalid.
**Fix**: Add a default case to handle invalid values:

```cpp
inline char const* to_string(portmap_action const act)
{
    switch (act)
    {
        case portmap_action::none: return "none";
        case portmap_action::add: return "add";
        case portmap_action::del: return "delete";
        default: return "unknown";
    }
}
```

### Modernization Opportunities

**Function**: `to_string(portmap_protocol)`
**Opportunity**: Use `std::string_view` for better string handling.
**Suggestion**: 
```cpp
#include <string_view>

inline std::string_view to_string(portmap_protocol const p)
{
    return p == portmap_protocol::udp ? "UDP"sv : "TCP"sv;
}
```

**Function**: `to_string(portmap_action)`
**Opportunity**: Use `std::string_view` for better string handling.
**Suggestion**: 
```cpp
#include <string_view>

inline std::string_view to_string(portmap_action const act)
{
    switch (act)
    {
        case portmap_action::none: return "none"sv;
        case portmap_action::add: return "add"sv;
        case portmap_action::del: return "delete"sv;
        default: return "unknown"sv;
    }
}
```

### Refactoring Suggestions

**Function**: `to_string(portmap_protocol)`
**Suggestion**: Consider creating a template function or using a map to handle both protocol and action conversions in a more generic way.

**Function**: `to_string(portmap_action)`
**Suggestion**: Consider combining both string conversion functions into a single utility function with an enum class parameter.

### Performance Optimizations

**Function**: `to_string(portmap_protocol)`
**Opportunity**: Use compile-time string literals to avoid runtime string creation.
**Suggestion**: 
```cpp
inline consteval char const* to_string(portmap_protocol const p)
{
    return p == portmap_protocol::udp ? "UDP" : "TCP";
}
```

**Function**: `to_string(portmap_action)`
**Opportunity**: Use `constexpr` for compile-time evaluation.
**Suggestion**: 
```cpp
inline constexpr char const* to_string(portmap_action const act)
{
    switch (act)
    {
        case portmap_action::none: return "none";
        case portmap_action::add: return "add";
        case portmap_action::del: return "delete";
        default: return "unknown";
    }
}
```