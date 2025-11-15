# API Documentation for receive_buffer.hpp

## Function Reference

### packet_size

- **Signature**: `int packet_size() const`
- **Description**: Returns the total size of the current packet being received, as determined during the initial packet handshake.
- **Parameters**: None
- **Return Value**: 
  - Returns the packet size in bytes
  - Always non-negative when the buffer is in a valid state
  - Returns 0 if the buffer is not currently receiving a packet
- **Exceptions/Errors**: 
  - None
  - Uses assertions to validate internal state
- **Example**:
```cpp
auto packet_size = buffer.packet_size();
if (packet_size > 0) {
    // Process packet of known size
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
  - The packet size must have been previously set
- **Postconditions**: 
  - Returns the current packet size
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `packet_bytes_remaining()`, `packet_finished()`

### packet_bytes_remaining

- **Signature**: `int packet_bytes_remaining() const`
- **Description**: Calculates how many bytes remain to be received for the current packet.
- **Parameters**: None
- **Return Value**: 
  - Returns the number of bytes remaining in the current packet
  - Returns 0 when the packet is fully received
  - Returns a positive value when more data is needed
- **Exceptions/Errors**: 
  - Asserts if the internal state is invalid (m_recv_start != 0, m_packet_size <= 0)
- **Example**:
```cpp
int bytes_remaining = buffer.packet_bytes_remaining();
if (bytes_remaining > 0) {
    // Need to receive more data
    auto data = socket.receive(bytes_remaining);
    buffer.received(data.size());
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
  - The packet size must be greater than 0
- **Postconditions**: 
  - Returns the number of bytes remaining
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `packet_size()`, `packet_finished()`

### packet_finished

- **Signature**: `bool packet_finished() const`
- **Description**: Determines whether the current packet has been fully received.
- **Parameters**: None
- **Return Value**: 
  - Returns `true` if the packet is complete (m_packet_size <= m_recv_pos)
  - Returns `false` if more data is needed
- **Exceptions/Errors**: 
  - Asserts if the packet size is invalid
- **Example**:
```cpp
if (buffer.packet_finished()) {
    // Process completed packet
    process_packet(buffer);
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
  - The packet size must be greater than 0
- **Postconditions**: 
  - Returns the packet completion status
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `packet_bytes_remaining()`, `packet_size()`

### pos

- **Signature**: `int pos() const`
- **Description**: Returns the current position within the receive buffer, indicating how many bytes have been received so far.
- **Parameters**: None
- **Return Value**: 
  - Returns the number of bytes received for the current packet
  - Returns 0 when no data has been received
  - Returns the packet size when the packet is complete
- **Exceptions/Errors**: 
  - Asserts if the buffer state is invalid
- **Example**:
```cpp
int current_pos = buffer.pos();
if (current_pos < buffer.packet_size()) {
    // Continue receiving data
    auto bytes_needed = buffer.packet_size() - current_pos;
    // ...
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the current receive position
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `packet_bytes_remaining()`, `capacity()`

### capacity

- **Signature**: `int capacity() const`
- **Description**: Returns the total capacity of the receive buffer in bytes.
- **Parameters**: None
- **Return Value**: 
  - Returns the maximum number of bytes the buffer can hold
  - Returns 0 if the buffer is empty or invalid
- **Exceptions/Errors**: 
  - None
  - Uses `aux::numeric_cast<int>` to safely convert size_t to int
- **Example**:
```cpp
int buffer_capacity = buffer.capacity();
if (buffer_capacity > 0) {
    // Buffer has usable capacity
    // ...
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the buffer capacity
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `pos()`, `watermark()`

### watermark

- **Signature**: `int watermark() const`
- **Description**: Returns the current watermark value for the receive buffer, representing the average or expected size of packets.
- **Parameters**: None
- **Return Value**: 
  - Returns the current watermark value
  - This is an average value used for optimization purposes
  - Returns 0 if no watermark has been set
- **Exceptions/Errors**: 
  - None
  - Uses `aux::numeric_cast<int>` to safely convert size_t to int
- **Example**:
```cpp
int current_watermark = buffer.watermark();
if (current_watermark > 0) {
    // Use watermark for optimization
    // ...
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the current watermark value
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `capacity()`, `pos()`

### received

- **Signature**: `void received(int bytes_transferred)`
- **Description**: Updates the receive buffer to account for the number of bytes that have been successfully transferred.
- **Parameters**: 
  - `bytes_transferred` (int): The number of bytes that were received
  - Must be non-negative
  - Should not exceed the remaining space in the buffer
- **Return Value**: None
- **Exceptions/Errors**: 
  - Asserts if the packet size is invalid (m_packet_size <= 0)
  - Asserts if the received position exceeds the buffer capacity
- **Example**:
```cpp
// After receiving data from a socket
int bytes_received = socket.receive(buffer.mutable_buffer());
buffer.received(bytes_received);
```
- **Preconditions**: 
  - The buffer must be in a valid state
  - The packet size must be greater than 0
  - The number of bytes transferred must be non-negative
- **Postconditions**: 
  - Updates the receive position and end position
  - Ensures the receive buffer is in a consistent state
- **Thread Safety**: 
  - Not thread-safe (modifies state)
- **Complexity**: O(1)
- **See Also**: `pos()`, `pos_at_end()`, `check_invariant()`

### pos_at_end

- **Signature**: `bool pos_at_end()`
- **Description**: Determines whether the receive position has reached the end of the current packet.
- **Parameters**: None
- **Return Value**: 
  - Returns `true` if the receive position equals the end position
  - Returns `false` if more data needs to be received
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
if (buffer.pos_at_end()) {
    // Process the current packet
    process_packet(buffer);
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the position comparison result
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `pos()`, `packet_finished()`

### normalized

- **Signature**: `bool normalized() const`
- **Description**: Checks whether the receive buffer is in a normalized state, where the receive start position is 0.
- **Parameters**: None
- **Return Value**: 
  - Returns `true` if the receive buffer is normalized (m_recv_start == 0)
  - Returns `false` if the buffer is in a shifted or offset state
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
if (buffer.normalized()) {
    // Buffer is in normal state, ready for processing
    // ...
} else {
    // Buffer is in a shifted state, may need normalization
    // ...
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the normalization status
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `check_invariant()`, `crypto_receive_buffer()`

### check_invariant

- **Signature**: `void check_invariant() const`
- **Description**: Verifies the internal consistency of the receive buffer by checking all invariants.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: 
  - Asserts if any invariant is violated
  - The assertions will trigger in debug builds if the buffer is in an invalid state
- **Example**:
```cpp
// Call this function to verify buffer consistency
buffer.check_invariant();
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - If no assertions fail, the buffer is in a consistent state
  - If assertions fail, the program will terminate (in debug mode)
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `normalized()`, `pos_at_end()`

### crypto_receive_buffer

- **Signature**: `explicit crypto_receive_buffer(receive_buffer& next)`
- **Description**: Constructs a crypto receive buffer that wraps another receive buffer for encrypted data processing.
- **Parameters**: 
  - `next` (receive_buffer&): The underlying receive buffer to wrap
  - Must be a valid reference to a receive buffer
- **Return Value**: None
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
receive_buffer base_buffer;
crypto_receive_buffer crypto_buffer(base_buffer);
```
- **Preconditions**: 
  - The passed receive buffer must be valid
- **Postconditions**: 
  - The crypto receive buffer is initialized and ready to use
  - The underlying buffer is wrapped and accessible
- **Thread Safety**: 
  - Not thread-safe (modifies state during construction)
- **Complexity**: O(1)
- **See Also**: `mutable_buffer()`, `crypto_packet_finished()`

### mutable_buffer

- **Signature**: `span<char> mutable_buffer()`
- **Description**: Returns a mutable span of the underlying receive buffer, allowing direct access to the data.
- **Parameters**: None
- **Return Value**: 
  - Returns a span of char representing the mutable buffer
  - The span covers the entire buffer or a portion of it
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
auto buffer_span = crypto_buffer.mutable_buffer();
// Directly access and modify the buffer data
for (auto& byte : buffer_span) {
    // Process or modify each byte
}
```
- **Preconditions**: 
  - The receive buffer must be in a valid state
- **Postconditions**: 
  - Returns a mutable span of the buffer
  - Does not modify the buffer state itself
- **Thread Safety**: 
  - Not thread-safe (returns mutable reference)
- **Complexity**: O(1)
- **See Also**: `crypto_packet_finished()`, `crypto_packet_size()`

### crypto_packet_finished

- **Signature**: `bool crypto_packet_finished() const`
- **Description**: Determines whether the current encrypted packet has been fully received.
- **Parameters**: None
- **Return Value**: 
  - Returns `true` if the crypto packet is finished
  - Returns `false` if more data is needed
- **Exceptions/Errors**: 
  - Asserts if the receive position is invalid (m_recv_pos == std::numeric_limits<int>::max())
- **Example**:
```cpp
if (crypto_buffer.crypto_packet_finished()) {
    // Process the completed encrypted packet
    process_encrypted_packet(crypto_buffer);
}
```
- **Preconditions**: 
  - The crypto receive buffer must be in a valid state
- **Postconditions**: 
  - Returns the crypto packet completion status
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `crypto_packet_size()`, `crypto_cut()`

### crypto_packet_size

- **Signature**: `int crypto_packet_size() const`
- **Description**: Returns the size of the remaining encrypted packet data.
- **Parameters**: None
- **Return Value**: 
  - Returns the number of bytes remaining in the encrypted packet
  - Returns 0 if the packet is finished
- **Exceptions/Errors**: 
  - Asserts if the receive position is invalid (m_recv_pos == std::numeric_limits<int>::max())
- **Example**:
```cpp
int remaining_size = crypto_buffer.crypto_packet_size();
if (remaining_size > 0) {
    // Need to receive more encrypted data
    // ...
}
```
- **Preconditions**: 
  - The crypto receive buffer must be in a valid state
  - The receive position must not be at the maximum value
- **Postconditions**: 
  - Returns the remaining packet size
  - Does not modify the buffer state
- **Thread Safety**: 
  - Thread-safe (const method)
- **Complexity**: O(1)
- **See Also**: `crypto_packet_finished()`, `crypto_cut()`

### crypto_cut

- **Signature**: `void crypto_cut(int size, int packet_size)`
- **Description**: Cuts the specified number of bytes from the crypto receive buffer, adjusting the receive position and end position accordingly.
- **Parameters**: 
  - `size` (int): The number of bytes to cut from the buffer
  - Must be non-negative
  - Should not exceed the buffer capacity
  - `packet_size` (int): The size of the packet being processed
  - Must be positive
- **Return Value**: None
- **Exceptions/Errors**: 
  - Asserts if the receive position is invalid (m_recv_pos == std::numeric_limits<int>::max())
  - Asserts if the packet size is invalid
- **Example**:
```cpp
// After processing a portion of the encrypted packet
crypto_buffer.crypto_cut(1024, 4096);
```
- **Preconditions**: 
  - The crypto receive buffer must be in a valid state
  - The receive position must not be at the maximum value
  - The packet size must be positive
- **Postconditions**: 
  - Updates the receive position and end position
  - The buffer state remains consistent
- **Thread Safety**: 
  - Not thread-safe (modifies state)
- **Complexity**: O(1)
- **See Also**: `crypto_packet_size()`, `crypto_packet_finished()`

## Usage Examples

### Basic Usage

```cpp
#include "libtorrent/aux_/receive_buffer.hpp"

// Create a receive buffer
libtorrent::aux::receive_buffer buffer;

// Set up the buffer for a new packet
int packet_size = 1024;
buffer.received(0); // Initialize for new packet

// Receive data
std::vector<char> data(1024);
// ... receive data into buffer
buffer.received(data.size());

// Check if packet is complete
if (buffer.packet_finished()) {
    // Process the complete packet
    // ...
}
```

### Error Handling

```cpp
#include "libtorrent/aux_/receive_buffer.hpp"
#include <cassert>

void process_packet_data(libtorrent::aux::receive_buffer& buffer) {
    try {
        // Check if packet is complete
        if (buffer.packet_finished()) {
            // Process the packet
            auto packet_data = buffer.mutable_buffer().subspan(0, buffer.pos());
            // Process packet_data...
        } else {
            // Packet is not complete, need more data
            int bytes_needed = buffer.packet_bytes_remaining();
            std::vector<char> buffer(bytes_needed);
            
            // Receive more data
            int bytes_received = socket.receive(buffer.data(), bytes_needed);
            buffer.received(bytes_received);
            
            // Check invariant to ensure buffer consistency
            buffer.check_invariant();
        }
    } catch (const std::exception& e) {
        // Handle exceptions
        std::cerr << "Error processing packet: " << e.what() << std::endl;
        // Reset buffer or take other recovery actions
    }
}
```

### Edge Cases

```cpp
#include "libtorrent/aux_/receive_buffer.hpp"

void handle_edge_cases(libtorrent::aux::receive_buffer& buffer) {
    // Edge case: empty packet
    if (buffer.packet_size() == 0) {
        // Handle empty packet case
        buffer.received(0); // Update position
        return;
    }
    
    // Edge case: partial packet
    if (buffer.packet_bytes_remaining() > 0) {
        // Handle partial packet
        int bytes_remaining = buffer.packet_bytes_remaining();
        if (bytes_remaining > buffer.capacity()) {
            // Handle case where packet size exceeds buffer capacity
            // This should be prevented at the protocol level
            return;
        }
        
        // Receive remaining data
        int bytes_received = socket.receive(buffer.mutable_buffer(), bytes_remaining);
        buffer.received(bytes_received);
    }
    
    // Edge case: packet size exceeds buffer capacity
    if (buffer.packet_size() > buffer.capacity()) {
