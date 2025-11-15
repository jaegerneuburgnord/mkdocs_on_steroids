# libtorrent Packet Pool API Documentation

## operator

- **Signature**: `void operator()(packet* p) const`
- **Description**: A function object that destroys a packet and frees its memory. This is typically used as a deleter for smart pointers, ensuring proper cleanup of packet objects. The function performs safety checks and memory management operations.
- **Parameters**:
  - `p` (packet*): Pointer to the packet object to be destroyed. Must not be null.
- **Return Value**: None
- **Exceptions/Errors**: Throws `std::bad_alloc` if memory allocation fails during packet creation (though this doesn't happen in this function). The function also uses assertions to validate input.
- **Example**:
```cpp
auto p = create_packet(1024);
// Use packet...
std::unique_ptr<packet, packet_deleter> packet_ptr(p, packet_deleter());
// packet_ptr will automatically call operator() when it goes out of scope
```
- **Preconditions**: `p` must not be null
- **Postconditions**: The packet object is destroyed, its memory is deallocated, and the pointer is no longer valid
- **Thread Safety**: Thread-safe if the packet is not accessed by other threads
- **Complexity**: O(1)
- **See Also**: `create_packet()`, `packet_ptr`

## create_packet

- **Signature**: `inline packet_ptr create_packet(int size)`
- **Description**: Allocates memory for a new packet of the specified size and constructs a packet object. The function creates a packet with the given allocation size and returns it as a unique pointer.
- **Parameters**:
  - `size` (int): The size of the packet to allocate. Must be non-negative and within the range of `std::uint16_t`. Values larger than `std::numeric_limits<std::uint16_t>::max()` will cause undefined behavior.
- **Return Value**: A `packet_ptr` (unique pointer) to the newly created packet. Returns a valid pointer if allocation succeeds.
- **Exceptions/Errors**: Throws `std::bad_alloc` if memory allocation fails.
- **Example**:
```cpp
try {
    auto packet = create_packet(512);
    // Use the packet
    // packet will be automatically freed when it goes out of scope
} catch (const std::bad_alloc& e) {
    // Handle memory allocation failure
}
```
- **Preconditions**: `size` must be ≥ 0 and ≤ `std::numeric_limits<std::uint16_t>::max()`
- **Postconditions**: Returns a valid packet pointer with the specified allocation size
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `packet_ptr`, `operator()`, `packet_slab`

## packet_slab

- **Signature**: `struct TORRENT_EXTRA_EXPORT packet_slab`
- **Description**: A slab allocator for packets of a specific size. This class manages a pool of packets of a fixed size, allowing efficient allocation and deallocation. It's designed to reduce memory fragmentation and improve performance by reusing previously allocated memory.
- **Members**:
  - `allocate_size` (int): The size of packets managed by this slab
  - `m_limit` (std::size_t): The maximum number of packets to keep in the pool
  - `m_storage` (std::vector<packet_ptr>): The storage for packets in the slab
- **Example**:
```cpp
packet_slab slab(1024, 50); // Create a slab for 1024-byte packets with a limit of 50 packets
auto packet = slab.alloc(); // Allocate a packet from the slab
// Use the packet
slab.try_push_back(packet); // Return the packet to the slab
```
- **Preconditions**: The slab should not be accessed concurrently
- **Postconditions**: The slab maintains a pool of packets of the specified size
- **Thread Safety**: Not thread-safe; designed for single-threaded use
- **Complexity**: O(1) for allocation and deallocation
- **See Also**: `alloc()`, `try_push_back()`, `decay()`

## packet_slab (constructor)

- **Signature**: `explicit packet_slab(int const alloc_size, std::size_t const limit = 10)`
- **Description**: Constructs a packet slab with the specified allocation size and limit on the number of packets to keep.
- **Parameters**:
  - `alloc_size` (int): The size of packets to allocate
  - `limit` (std::size_t): Maximum number of packets to keep in the slab. Default is 10.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_slab slab(512, 100); // Create a slab for 512-byte packets with a limit of 100
```
- **Preconditions**: `limit` must be ≥ 0
- **Postconditions**: The slab is initialized with the specified parameters
- **Thread Safety**: Thread-safe for construction
- **Complexity**: O(1)
- **See Also**: `packet_slab`, `alloc()`, `try_push_back()`

## packet_slab (copy constructor)

- **Signature**: `packet_slab(const packet_slab&) = delete;`
- **Description**: Deleted copy constructor to prevent copying of packet slabs. This is to avoid potential issues with shared ownership of the packet storage.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**: This function cannot be called as it's deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Not applicable
- **Complexity**: N/A
- **See Also**: `packet_slab`, `packet_slab(packet_slab&&)`

## packet_slab (move constructor)

- **Signature**: `packet_slab(packet_slab&&) = default;`
- **Description**: Default move constructor for packet slabs. Allows transferring ownership of a packet slab to another object.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_slab slab1(512, 50);
packet_slab slab2 = std::move(slab1); // Transfer ownership
```
- **Preconditions**: None
- **Postconditions**: The source slab is left in a valid but unspecified state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `packet_slab`, `packet_slab(const packet_slab&)`

## try_push_back

- **Signature**: `void try_push_back(packet_ptr &p)`
- **Description**: Attempts to add a packet back to the slab's storage if there's room. This function checks if the slab has capacity before adding the packet.
- **Parameters**:
  - `p` (packet_ptr&): The packet to try to push back. The packet will be moved from this parameter.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_slab slab(512, 50);
auto packet = slab.alloc();
// Use packet...
slab.try_push_back(packet); // Return packet to slab if space available
```
- **Preconditions**: The slab must not be accessed concurrently
- **Postconditions**: If the slab has capacity, the packet is added to storage; otherwise, it's discarded
- **Thread Safety**: Not thread-safe
- **Complexity**: O(1)
- **See Also**: `alloc()`, `decay()`

## alloc

- **Signature**: `packet_ptr alloc()`
- **Description**: Allocates a packet from the slab. If the slab has packets available, it returns one from the pool; otherwise, it creates a new packet.
- **Parameters**: None
- **Return Value**: A `packet_ptr` to the allocated packet
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_slab slab(1024, 20);
auto packet = slab.alloc(); // Get a packet from the slab
// Use packet...
```
- **Preconditions**: The slab must not be accessed concurrently
- **Postconditions**: Returns a packet with the slab's allocation size
- **Thread Safety**: Not thread-safe
- **Complexity**: O(1)
- **See Also**: `try_push_back()`, `create_packet()`

## decay

- **Signature**: `void decay()`
- **Description**: Removes the oldest packet from the slab's storage. This function is used to reduce the size of the slab when it grows too large.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_slab slab(512, 50);
// After some operations...
slab.decay(); // Remove the oldest packet from the slab
```
- **Preconditions**: The slab must not be accessed concurrently
- **Postconditions**: The oldest packet is removed from storage
- **Thread Safety**: Not thread-safe
- **Complexity**: O(1)
- **See Also**: `try_push_back()`, `alloc()`

## packet_pool

- **Signature**: `struct TORRENT_EXTRA_EXPORT packet_pool : private single_threaded`
- **Description**: A packet pool that manages multiple packet slabs for different packet sizes. This class provides a convenient interface for allocating and releasing packets of various sizes.
- **Members**:
  - `m_syn_slab`: Slab for SYN packets
  - `m_mtu_floor_slab`: Slab for MTU floor packets
  - `m_mtu_ceiling_slab`: Slab for MTU ceiling packets
- **Example**:
```cpp
packet_pool pool;
auto packet = pool.acquire(512); // Acquire a packet of size 512
// Use packet...
pool.release(packet); // Return packet to the pool
```
- **Preconditions**: The pool should not be accessed concurrently
- **Postconditions**: The pool is initialized with the specified slabs
- **Thread Safety**: Thread-safe due to `single_threaded` inheritance
- **Complexity**: O(1)
- **See Also**: `acquire()`, `release()`, `single_threaded`

## packet_pool (constructor)

- **Signature**: `packet_pool()`
- **Description**: Default constructor for the packet pool. Initializes the pool with the predefined slab sizes.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_pool pool; // Construct a packet pool
```
- **Preconditions**: None
- **Postconditions**: The pool is initialized with the default slab configuration
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `packet_pool`, `acquire()`, `release()`

## packet_pool (move constructor)

- **Signature**: `packet_pool(packet_pool&&) = default;`
- **Description**: Default move constructor for packet pools. Allows transferring ownership of a packet pool to another object.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_pool pool1;
packet_pool pool2 = std::move(pool1); // Transfer ownership
```
- **Preconditions**: None
- **Postconditions**: The source pool is left in a valid but unspecified state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `packet_pool`, `packet_pool(packet_pool&&)`

## acquire

- **Signature**: `packet_ptr acquire(int const allocate)`
- **Description**: Acquires a packet of the specified size from the pool. The function selects the appropriate slab based on the requested size and allocates a packet from it.
- **Parameters**:
  - `allocate` (int const): The size of the packet to acquire. Must be non-negative and within the range of `std::uint16_t`.
- **Return Value**: A `packet_ptr` to the acquired packet
- **Exceptions/Errors**: None (assertions are checked at runtime)
- **Example**:
```cpp
packet_pool pool;
auto packet = pool.acquire(2048); // Acquire a 2048-byte packet
// Use packet...
```
- **Preconditions**: The function must be called from a single-threaded context, and `allocate` must be ≥ 0 and ≤ `std::numeric_limits<std::uint16_t>::max()`
- **Postconditions**: Returns a packet with the specified allocation size
- **Thread Safety**: Not thread-safe; requires single-threaded access
- **Complexity**: O(1)
- **See Also**: `release()`, `alloc()`

## release

- **Signature**: `void release(packet_ptr p)`
- **Description**: Releases a packet back to the pool. The function determines which slab the packet belongs to based on its allocation size and returns it to the appropriate slab.
- **Parameters**:
  - `p` (packet_ptr): The packet to release. Can be null.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_pool pool;
auto packet = pool.acquire(1024);
// Use packet...
pool.release(packet); // Return packet to the pool
```
- **Preconditions**: The function must be called from a single-threaded context, and the packet must have been acquired from this pool
- **Postconditions**: The packet is returned to the appropriate slab if it's not null and has a valid allocation size
- **Thread Safety**: Not thread-safe; requires single-threaded access
- **Complexity**: O(1)
- **See Also**: `acquire()`, `try_push_back()`

## decay

- **Signature**: `void decay()`
- **Description**: Reduces the size of all slabs in the packet pool by removing the oldest packet from each slab. This function helps maintain the memory footprint of the pool.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
packet_pool pool;
// After some operations...
pool.decay(); // Reduce the size of all slabs
```
- **Preconditions**: The function must be called from a single-threaded context
- **Postconditions**: The oldest packet is removed from each slab
- **Thread Safety**: Not thread-safe; requires single-threaded access
- **Complexity**: O(1)
- **See Also**: `acquire()`, `release()`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/packet_pool.hpp>

int main() {
    // Create a packet pool
    packet_pool pool;
    
    // Acquire a packet of size 512
    auto packet = pool.acquire(512);
    
    // Use the packet
    // ... (packet manipulation code)
    
    // Release the packet back to the pool
    pool.release(packet);
    
    // Decay the pool to reduce memory usage
    pool.decay();
    
    return 0;
}
```

## Error Handling

```cpp
#include <libtorrent/aux_/packet_pool.hpp>
#include <iostream>

int main() {
    packet_pool pool;
    
    try {
        // Attempt to acquire a packet
        auto packet = pool.acquire(1024);
        
        // Check if packet acquisition was successful
        if (!packet) {
            std::cerr << "Failed to acquire packet" << std::endl;
            return 1;
        }
        
        // Use the packet
        // ... (packet manipulation code)
        
        // Release the packet
        pool.release(packet);
    } catch (const std::bad_alloc& e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/packet_pool.hpp>

int main() {
    packet_pool pool;
    
    // Edge case 1: Acquire maximum possible packet size
    try {
        auto packet = pool.acquire(std::numeric_limits<std::uint16_t>::max());
        if (packet) {
            std::cout << "Acquired max-sized packet" << std::endl;
            pool.release(packet);
        }
    } catch (const std::bad_alloc& e) {
        std::cout << "Could not acquire max-sized packet: " << e.what() << std::endl;
    }
    
    // Edge case 2: Acquire zero-sized packet
    try {
        auto packet = pool.acquire(0);
        if (packet) {
            std::cout << "Acquired zero-sized packet" << std::endl;
            pool.release(packet);
        }
    } catch (const std::bad_alloc& e) {
        std::cout << "Could not acquire zero-sized packet: " << e.what() << std::endl;
    }
    
    // Edge case 3: Release null packet
    pool.release(nullptr); // Should be safe
    
    return 0;
}
```

# Best Practices

1. **Use the pool appropriately**: Only use `packet_pool` for packet allocation and deallocation. Don't use it for general memory management.

2. **Ensure thread safety**: The packet pool is designed for single-threaded use. Make sure that all operations on the same pool are performed from the same thread.

3. **Check for null packets**: Always check if `acquire()` returns a valid packet before using it.

4. **Release packets promptly**: Return packets to the pool as soon as they're no longer needed to maintain optimal memory usage.

5. **Use appropriate slab sizes**: Understand the packet sizes you need and use the most appropriate slab to avoid unnecessary allocations.

6. **Monitor memory usage**: Use `decay()` periodically to reduce memory footprint when the pool grows large.

7. **Handle exceptions**: Wrap `acquire()` in try-catch blocks to handle memory allocation failures gracefully.

# Code Review & Improvement Suggestions

## Potential Issues

**Function**: `operator()`
**Issue**: No null pointer check before calling `std::free()` (though there's an assertion)
**Severity**: Medium
**Impact**: Could lead to undefined behavior if null pointer is passed
**Fix**: The assertion already handles this case, but it could be more explicit:
```cpp
void