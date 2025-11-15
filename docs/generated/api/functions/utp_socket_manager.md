# API Documentation for `utp_socket_manager.hpp`

## `get_local_endpoint`

- **Signature**: `virtual udp::endpoint get_local_endpoint() = 0;`
- **Description**: Pure virtual function that returns the local endpoint (IP address and port) associated with the UTP socket. This function must be implemented by any concrete class inheriting from `utp_socket_interface`. It's used to determine the local address and port that the socket is bound to.
- **Parameters**: None
- **Return Value**: Returns the local endpoint as an `udp::endpoint` object. This contains both the IP address and port number of the local socket.
- **Exceptions/Errors**: None. This is a pure virtual function that must be implemented.
- **Example**:
```cpp
class MyUtpSocket : public utp_socket_interface {
public:
    udp::endpoint get_local_endpoint() override {
        return udp::endpoint(udp::v4(), 6881);
    }
};
```
- **Preconditions**: The socket must be bound to a local address.
- **Postconditions**: The function returns a valid `udp::endpoint` object representing the local socket address.
- **Thread Safety**: Thread-safe if the underlying socket implementation is thread-safe.
- **Complexity**: O(1)
- **See Also**: `udp::endpoint`, `utp_socket_interface`

## `gain_factor`

- **Signature**: `int gain_factor() const`
- **Description**: Retrieves the gain factor setting for UTP (User Datagram Protocol) sockets. The gain factor influences the rate at which the congestion window grows during the congestion avoidance phase of the UTP protocol.
- **Parameters**: None
- **Return Value**: Returns the gain factor as an integer value, which is retrieved from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int factor = socket_manager.gain_factor();
if (factor > 0) {
    // Use the gain factor value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current gain factor setting.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `target_delay`, `syn_resends`

## `target_delay`

- **Signature**: `int target_delay() const`
- **Description**: Retrieves the target delay setting for UTP sockets. This value represents the desired round-trip time (in milliseconds) that the UTP protocol aims to maintain for optimal performance.
- **Parameters**: None
- **Return Value**: Returns the target delay in milliseconds as an integer. The value is obtained from the settings pack and multiplied by 1000.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int delay = socket_manager.target_delay();
if (delay >= 0) {
    // Use the target delay value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the target delay in milliseconds.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `gain_factor`, `loss_multiplier`

## `syn_resends`

- **Signature**: `int syn_resends() const`
- **Description**: Retrieves the number of times a SYN packet will be resent during the UTP connection establishment phase. This helps ensure reliable connection setup over unreliable networks.
- **Parameters**: None
- **Return Value**: Returns the number of SYN resends as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int resends = socket_manager.syn_resends();
if (resends >= 0) {
    // Use the SYN resend count
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current SYN resend count.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `fin_resends`, `num_resends`

## `fin_resends`

- **Signature**: `int fin_resends() const`
- **Description**: Retrieves the number of times a FIN packet will be resent during the UTP connection termination phase. This ensures reliable connection shutdown.
- **Parameters**: None
- **Return Value**: Returns the number of FIN resends as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int resends = socket_manager.fin_resends();
if (resends >= 0) {
    // Use the FIN resend count
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current FIN resend count.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `syn_resends`, `num_resends`

## `num_resends`

- **Signature**: `int num_resends() const`
- **Description**: Retrieves the total number of times a packet will be resent during the UTP connection lifetime. This is a general setting for the maximum number of retransmissions for any packet.
- **Parameters**: None
- **Return Value**: Returns the number of retransmissions as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int resends = socket_manager.num_resends();
if (resends >= 0) {
    // Use the retransmission count
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current retransmission count.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `syn_resends`, `fin_resends`

## `connect_timeout`

- **Signature**: `int connect_timeout() const`
- **Description**: Retrieves the connection timeout setting for UTP sockets. This specifies the maximum time (in seconds) to wait for a connection to be established before giving up.
- **Parameters**: None
- **Return Value**: Returns the connect timeout in seconds as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int timeout = socket_manager.connect_timeout();
if (timeout > 0) {
    // Use the connect timeout value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current connection timeout.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `min_timeout`, `cwnd_reduce_timer`

## `min_timeout`

- **Signature**: `int min_timeout() const`
- **Description**: Retrieves the minimum timeout setting for UTP sockets. This represents the minimum time (in seconds) that the UTP protocol will wait for a response before taking action.
- **Parameters**: None
- **Return Value**: Returns the minimum timeout in seconds as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int timeout = socket_manager.min_timeout();
if (timeout > 0) {
    // Use the minimum timeout value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current minimum timeout.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `connect_timeout`, `cwnd_reduce_timer`

## `loss_multiplier`

- **Signature**: `int loss_multiplier() const`
- **Description**: Retrieves the loss multiplier setting for UTP sockets. This value influences how aggressively the congestion window is reduced when packet loss is detected.
- **Parameters**: None
- **Return Value**: Returns the loss multiplier as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int multiplier = socket_manager.loss_multiplier();
if (multiplier >= 0) {
    // Use the loss multiplier value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current loss multiplier.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `gain_factor`, `target_delay`

## `cwnd_reduce_timer`

- **Signature**: `int cwnd_reduce_timer() const`
- **Description**: Retrieves the congestion window reduction timer setting for UTP sockets. This specifies the time (in seconds) after which the congestion window is reduced when packet loss is detected.
- **Parameters**: None
- **Return Value**: Returns the congestion window reduction timer in seconds as an integer, obtained from the settings pack.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int timer = socket_manager.cwnd_reduce_timer();
if (timer > 0) {
    // Use the congestion window reduction timer value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current congestion window reduction timer.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1)
- **See Also**: `connect_timeout`, `min_timeout`

## `num_sockets`

- **Signature**: `int num_sockets() const`
- **Description**: Returns the number of UTP sockets currently managed by the socket manager.
- **Parameters**: None
- **Return Value**: Returns the number of UTP sockets as an integer, which is the size of the `m_utp_sockets` container.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int count = socket_manager.num_sockets();
if (count > 0) {
    // There are active UTP sockets
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the current count of UTP sockets.
- **Thread Safety**: Thread-safe if access to `m_utp_sockets` is synchronized.
- **Complexity**: O(1)
- **See Also**: `restrict_mtu`, `acquire_packet`

## `restrict_mtu` (Overload 1)

- **Signature**: `void restrict_mtu(int const mtu)`
- **Description**: Sets the Maximum Transmission Unit (MTU) limit for a specific socket. This function updates the `m_restrict_mtu` array with the given MTU value, cycling through the array using `m_mtu_idx`. This is used to limit the size of packets that can be sent.
- **Parameters**:
  - `mtu` (int): The Maximum Transmission Unit value in bytes. This should be a positive integer representing the maximum packet size.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
socket_manager.restrict_mtu(1400); // Set MTU to 1400 bytes
```
- **Preconditions**: The `socket_manager` must be properly initialized. The `mtu` parameter must be a positive integer.
- **Postconditions**: The `m_restrict_mtu` array is updated with the new MTU value at the current index, and `m_mtu_idx` is incremented.
- **Thread Safety**: Not thread-safe; concurrent access may cause race conditions.
- **Complexity**: O(1)
- **See Also**: `restrict_mtu` (Overload 2), `acquire_packet`

## `restrict_mtu` (Overload 2)

- **Signature**: `int restrict_mtu() const`
- **Description**: Returns the maximum MTU value currently set in the `m_restrict_mtu` array. This is the highest value among all the MTU settings that have been applied.
- **Parameters**: None
- **Return Value**: Returns the maximum MTU value as an integer, obtained by calling `std::max_element` on the `m_restrict_mtu` array.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int max_mtu = socket_manager.restrict_mtu();
if (max_mtu > 0) {
    // Use the maximum MTU value
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns the maximum MTU value from the `m_restrict_mtu` array.
- **Thread Safety**: Thread-safe if the `m_restrict_mtu` array is not being modified concurrently.
- **Complexity**: O(n) where n is the size of `m_restrict_mtu`
- **See Also**: `restrict_mtu` (Overload 1), `acquire_packet`

## `acquire_packet`

- **Signature**: `aux::packet_ptr acquire_packet(int const allocate)`
- **Description**: Acquires a packet from the packet pool with the specified allocation size. This function is used to obtain a packet for sending data over the network.
- **Parameters**:
  - `allocate` (int): The number of bytes to allocate for the packet. This should be a positive integer representing the size of the packet.
- **Return Value**: Returns a `aux::packet_ptr` object that contains the allocated packet. This pointer can be used to send data over the network.
- **Exceptions/Errors**: None
- **Example**:
```cpp
aux::packet_ptr packet = socket_manager.acquire_packet(1024);
if (packet) {
    // Use the packet for sending data
    packet->data = "Hello World";
    // ... send the packet
}
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Returns a valid packet pointer with the requested allocation size.
- **Thread Safety**: Thread-safe if the packet pool is thread-safe.
- **Complexity**: O(1)
- **See Also**: `release_packet`, `decay`

## `release_packet`

- **Signature**: `void release_packet(aux::packet_ptr p)`
- **Description**: Releases a packet back to the packet pool. This function is used to return a packet that was previously acquired using `acquire_packet`, allowing it to be reused for future operations.
- **Parameters**:
  - `p` (aux::packet_ptr): The packet pointer to release. This should be a valid packet pointer that was acquired from the packet pool.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
aux::packet_ptr packet = socket_manager.acquire_packet(1024);
if (packet) {
    // Use the packet for sending data
    socket_manager.release_packet(std::move(packet));
}
```
- **Preconditions**: The `socket_manager` must be properly initialized. The `p` parameter must be a valid packet pointer that was acquired from the packet pool.
- **Postconditions**: The packet is returned to the pool and can be reused.
- **Thread Safety**: Thread-safe if the packet pool is thread-safe.
- **Complexity**: O(1)
- **See Also**: `acquire_packet`, `decay`

## `decay`

- **Signature**: `void decay()`
- **Description**: Decays the packet pool by removing packets that have been in the pool for too long. This function is used to clean up stale packets and free up memory.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
socket_manager.decay(); // Clean up stale packets
```
- **Preconditions**: The `socket_manager` must be properly initialized.
- **Postconditions**: Stale packets are removed from the packet pool.
- **Thread Safety**: Thread-safe if the packet pool is thread-safe.
- **Complexity**: O(n) where n is the number of packets in the pool
- **See Also**: `acquire_packet`, `release_packet`

## Usage Examples

### Basic Usage

```cpp
#include "utp_socket_manager.hpp"

// Create a socket manager instance
utp_socket_manager socket_manager;

// Get the number of sockets
int num_sockets = socket_manager.num_sockets();
std::cout << "Number of UTP sockets: " << num_sockets << std::endl;

// Acquire a packet
aux::packet_ptr packet = socket_manager.acquire_packet(1024);
if (packet) {
    // Use the packet for sending data
    packet->data = "Hello World";
    // ... send the packet
}

// Release the packet
socket_manager.release_packet(std::move(packet));

// Decay the packet pool
socket_manager.decay();
```

### Error Handling

```cpp
#include "utp_socket_manager.hpp"

// Create a socket manager instance
utp_socket_manager socket_manager;

// Check for valid settings
int connect_timeout = socket_manager.connect_timeout();
if (connect_timeout <= 0) {
    std::cerr << "Invalid connect timeout setting" << std::endl;
    return;
}

// Acquire a packet
aux::packet_ptr packet = socket_manager.acquire_packet(1024);
if (!packet) {
    std::cerr << "Failed to acquire packet" << std::endl;
    return;
}

// Use the packet for sending data
packet->data = "Hello World";

// Release the packet
socket_manager.release_packet(std::move(packet));
```

### Edge Cases

```cpp
#include "utp_socket_manager.hpp"

// Create a socket manager instance
utp_socket_manager socket_manager;

// Test with zero or negative values
int zero_mtu = socket_manager.restrict_mtu();
if (zero_mtu == 0) {
    std::cout << "No MTU restrictions set" << std::endl;
}

// Test with large packet sizes
int large_packet_size = 8192;
aux::packet_ptr large_packet = socket_manager.acquire_packet(large_packet_size);
if (large_packet) {
    // Use the large packet
    std::cout << "Successfully acquired large packet" << std::endl;
    socket_manager.release_packet(std::move(large_packet));
} else {
    std::cerr << "Failed to acquire large packet" << std::endl;
}
```

## Best Practices

1. **Use `restrict_mtu`**: Always set appropriate MTU values to avoid fragmentation and improve performance.
2. **Manage packet lifecycle**: Properly acquire and release packets to prevent memory leaks.
3. **Monitor packet pool**: Regularly call `decay()` to clean up stale packets and free up memory.
4. **Check return values**: Always check the return values of functions like `acquire_packet` to ensure they succeed.
5. **Thread safety**: Be aware of thread safety issues, especially with concurrent access to the packet pool and MTU settings.

## Code Review & Improvement Suggestions

### `get_local_endpoint`

**Function**: `get_local_endpoint`
**Issue**: No validation of the socket binding
**Severity**: Low
**Impact**: Could return an invalid endpoint if the socket is not bound
**Fix**: Ensure the socket is bound before calling the function:
