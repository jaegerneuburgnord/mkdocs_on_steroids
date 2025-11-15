# libtorrent Network Link Utilities API Documentation

This document provides comprehensive API documentation for the network link utility functions in the libtorrent library. These functions provide convenient wrappers around the Netlink API macros, making it easier to work with network link messages and attributes in a C++ context.

## Function Reference

### nlmsg_ok

- **Signature**: `bool nlmsg_ok(nlmsghdr const* hdr, int const len)`
- **Description**: Checks if a Netlink message header is valid and properly aligned within the given buffer length. This function validates that the message header is within the bounds of the provided buffer and that it has sufficient data for the message type.
- **Parameters**:
  - `hdr` (nlmsghdr const*): Pointer to the Netlink message header to validate. This must be a valid pointer to a `nlmsghdr` structure.
  - `len` (int const): The total length of the buffer containing the Netlink message in bytes. This must be a non-negative value.
- **Return Value**:
  - `true`: The Netlink message header is valid and within the buffer bounds.
  - `false`: The message header is invalid or extends beyond the buffer bounds.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Check if a Netlink message header is valid
if (nlmsg_ok(message_hdr, message_len)) {
    // Process the valid message
    // ...
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to a `nlmsghdr` structure.
  - `len` must be greater than or equal to the size of `nlmsghdr`.
- **Postconditions**: Returns true if the header is valid and within bounds, false otherwise.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `nlmsg_next()`, `nlmsg_data()`

### nlmsg_next

- **Signature**: `nlmsghdr const* nlmsg_next(nlmsghdr const* hdr, int& len)`
- **Description**: Advances to the next Netlink message in a sequence of messages. This function updates the length parameter to reflect the remaining data after the current message, allowing iteration through multiple Netlink messages in a single buffer.
- **Parameters**:
  - `hdr` (nlmsghdr const*): Pointer to the current Netlink message header. This must be a valid pointer to a `nlmsghdr` structure.
  - `len` (int&): Reference to the length of the remaining data. This parameter is updated to the length of the remaining data after the current message.
- **Return Value**:
  - Pointer to the next Netlink message header, or `nullptr` if there are no more messages.
  - Returns `nullptr` when the end of the buffer is reached or if the next message would extend beyond the buffer.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Iterate through all Netlink messages in a buffer
nlmsghdr const* current_hdr = first_message;
int remaining_len = buffer_size;

while (current_hdr != nullptr) {
    // Process current message
    // ...
    
    // Move to next message
    current_hdr = nlmsg_next(current_hdr, remaining_len);
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to a `nlmsghdr` structure.
  - `len` must be a non-negative value representing the current buffer length.
- **Postconditions**: Returns a pointer to the next message header or `nullptr` if no more messages exist. The `len` parameter is updated to reflect the remaining data.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `nlmsg_ok()`, `nlmsg_data()`

### nlmsg_data

- **Signature**: `void const* nlmsg_data(nlmsghdr const* hdr)`
- **Description**: Returns a pointer to the data portion of a Netlink message. This function extracts the data payload from the Netlink message header, which is the portion of the message that contains the actual information.
- **Parameters**:
  - `hdr` (nlmsghdr const*): Pointer to the Netlink message header. This must be a valid pointer to a `nlmsghdr` structure.
- **Return Value**:
  - Pointer to the data portion of the Netlink message.
  - The returned pointer is valid only as long as the original buffer remains valid.
  - Returns `nullptr` if the message header is invalid or has no data.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Extract data from a Netlink message
void const* data = nlmsg_data(message_hdr);
if (data != nullptr) {
    // Process the message data
    // ...
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to a `nlmsghdr` structure.
  - The message header must be valid (can be checked with `nlmsg_ok()`).
- **Postconditions**: Returns a pointer to the data portion of the message, or `nullptr` if the message has no data or is invalid.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `nlmsg_ok()`, `nlmsg_next()`

### rtm_rta

- **Signature**: `rtattr const* rtm_rta(rtmsg const* hdr)`
- **Description**: Returns a pointer to the route attributes in a routing message. This function extracts the route attributes from a routing message header, which contain additional information about the routing information.
- **Parameters**:
  - `hdr` (rtmsg const*): Pointer to the routing message header. This must be a valid pointer to an `rtmsg` structure.
- **Return Value**:
  - Pointer to the route attributes, or `nullptr` if there are no route attributes.
  - The returned pointer is valid only as long as the original buffer remains valid.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Extract route attributes from a routing message
rtattr const* rta = rtm_rta(routing_hdr);
if (rta != nullptr) {
    // Process route attributes
    // ...
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to an `rtmsg` structure.
- **Postconditions**: Returns a pointer to the route attributes, or `nullptr` if there are no route attributes.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `rtm_payload()`, `rta_ok()`

### rtm_payload

- **Signature**: `std::size_t rtm_payload(nlmsghdr const* hdr)`
- **Description**: Returns the length of the payload in a routing message. This function calculates the size of the routing message data portion, which excludes the routing message header but includes the route attributes.
- **Parameters**:
  - `hdr` (nlmsghdr const*): Pointer to the Netlink message header. This must be a valid pointer to a `nlmsghdr` structure.
- **Return Value**:
  - The size of the payload in bytes.
  - Returns 0 if the message is invalid or has no payload.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Get the payload size of a routing message
std::size_t payload_size = rtm_payload(message_hdr);
if (payload_size > 0) {
    // Process the payload data
    // ...
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to a `nlmsghdr` structure.
- **Postconditions**: Returns the size of the payload in bytes.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `nlmsg_data()`, `rtm_rta()`

### rta_ok

- **Signature**: `bool rta_ok(rtattr const* rt, std::size_t const len)`
- **Description**: Checks if a route attribute is valid and properly aligned within the given buffer length. This function validates that the route attribute is within the bounds of the provided buffer and that it has sufficient data for the attribute type.
- **Parameters**:
  - `rt` (rtattr const*): Pointer to the route attribute to validate. This must be a valid pointer to an `rtattr` structure.
  - `len` (std::size_t const): The total length of the buffer containing the route attribute in bytes. This must be a non-negative value.
- **Return Value**:
  - `true`: The route attribute is valid and within the buffer bounds.
  - `false`: The route attribute is invalid or extends beyond the buffer bounds.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Check if a route attribute is valid
if (rta_ok(attribute, attribute_len)) {
    // Process the valid attribute
    // ...
}
```
- **Preconditions**: 
  - `rt` must be a valid pointer to an `rtattr` structure.
  - `len` must be greater than or equal to the size of `rtattr`.
- **Postconditions**: Returns true if the route attribute is valid and within bounds, false otherwise.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `rta_next()`, `rta_data()`

### rta_data

- **Signature**: `void const* rta_data(rtattr const* rt)`
- **Description**: Returns a pointer to the data portion of a route attribute. This function extracts the data payload from a route attribute, which is the portion of the attribute that contains the actual information.
- **Parameters**:
  - `rt` (rtattr const*): Pointer to the route attribute. This must be a valid pointer to an `rtattr` structure.
- **Return Value**:
  - Pointer to the data portion of the route attribute.
  - The returned pointer is valid only as long as the original buffer remains valid.
  - Returns `nullptr` if the route attribute is invalid or has no data.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Extract data from a route attribute
void const* attribute_data = rta_data(attribute);
if (attribute_data != nullptr) {
    // Process the attribute data
    // ...
}
```
- **Preconditions**: 
  - `rt` must be a valid pointer to an `rtattr` structure.
  - The route attribute must be valid (can be checked with `rta_ok()`).
- **Postconditions**: Returns a pointer to the data portion of the attribute, or `nullptr` if the attribute has no data or is invalid.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `rta_ok()`, `rta_next()`

### rta_next

- **Signature**: `rtattr const* rta_next(rtattr const* rt, std::size_t& len)`
- **Description**: Advances to the next route attribute in a sequence of attributes. This function updates the length parameter to reflect the remaining data after the current attribute, allowing iteration through multiple route attributes in a single buffer.
- **Parameters**:
  - `rt` (rtattr const*): Pointer to the current route attribute. This must be a valid pointer to an `rtattr` structure.
  - `len` (std::size_t&): Reference to the length of the remaining data. This parameter is updated to the length of the remaining data after the current attribute.
- **Return Value**:
  - Pointer to the next route attribute, or `nullptr` if there are no more attributes.
  - Returns `nullptr` when the end of the buffer is reached or if the next attribute would extend beyond the buffer.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Iterate through all route attributes in a buffer
rtattr const* current_rt = first_attribute;
std::size_t remaining_len = buffer_size;

while (current_rt != nullptr) {
    // Process current attribute
    // ...
    
    // Move to next attribute
    current_rt = rta_next(current_rt, remaining_len);
}
```
- **Preconditions**: 
  - `rt` must be a valid pointer to an `rtattr` structure.
  - `len` must be a non-negative value representing the current buffer length.
- **Postconditions**: Returns a pointer to the next route attribute or `nullptr` if no more attributes exist. The `len` parameter is updated to reflect the remaining data.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `rta_ok()`, `rta_data()`

### ifa_rta

- **Signature**: `rtattr const* ifa_rta(ifaddrmsg const* ifa)`
- **Description**: Returns a pointer to the interface address attributes in an interface address message. This function extracts the interface address attributes from an interface address message header, which contain additional information about the network interface address.
- **Parameters**:
  - `ifa` (ifaddrmsg const*): Pointer to the interface address message header. This must be a valid pointer to an `ifaddrmsg` structure.
- **Return Value**:
  - Pointer to the interface address attributes, or `nullptr` if there are no interface address attributes.
  - The returned pointer is valid only as long as the original buffer remains valid.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Extract interface address attributes from an interface address message
rtattr const* rta = ifa_rta(interface_msg);
if (rta != nullptr) {
    // Process interface address attributes
    // ...
}
```
- **Preconditions**: 
  - `ifa` must be a valid pointer to an `ifaddrmsg` structure.
- **Postconditions**: Returns a pointer to the interface address attributes, or `nullptr` if there are no interface address attributes.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `ifa_payload()`, `ifla_rta()`

### ifa_payload

- **Signature**: `std::size_t ifa_payload(nlmsghdr const* hdr)`
- **Description**: Returns the length of the payload in an interface address message. This function calculates the size of the interface address message data portion, which excludes the interface address message header but includes the interface address attributes.
- **Parameters**:
  - `hdr` (nlmsghdr const*): Pointer to the Netlink message header. This must be a valid pointer to a `nlmsghdr` structure.
- **Return Value**:
  - The size of the payload in bytes.
  - Returns 0 if the message is invalid or has no payload.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Get the payload size of an interface address message
std::size_t payload_size = ifa_payload(message_hdr);
if (payload_size > 0) {
    // Process the payload data
    // ...
}
```
- **Preconditions**: 
  - `hdr` must be a valid pointer to a `nlmsghdr` structure.
- **Postconditions**: Returns the size of the payload in bytes.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: O(1) - constant time operation.
- **See Also**: `nlmsg_data()`, `ifa_rta()`

### ifla_rta

- **Signature**: `rtattr const* ifla_rta(ifinfomsg const* ifinfo)`
- **Description**: Returns a pointer to the interface attributes in an interface information message. This function extracts the interface attributes from an interface information message header, which contain additional information about the network interface.
- **Parameters**:
  - `ifinfo` (ifinfomsg const*): Pointer to the interface information message header. This must be a valid pointer to an `ifinfomsg` structure.
- **Return Value**:
  - Pointer to the interface attributes, or `nullptr` if there are no interface attributes.
  - The returned pointer is valid only as long as the original buffer remains valid.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - This function does not check for memory access violations; invalid pointers can lead to undefined behavior.
- **Example**:
```cpp
// Extract interface attributes from an interface information message
rtattr const* rta = ifla_rta(interface_info);
if (rta != nullptr) {
    // Process interface attributes
    // ...
}
```
- **Preconditions**: 
  - `ifinfo` must be a valid pointer to an `ifinfomsg` structure.
- **Postconditions**: Returns a pointer to the interface attributes, or `nullptr` if there are no interface attributes.
- **Thread Safety**: Thread-safe (read-only access to const data).
- **Complexity**: