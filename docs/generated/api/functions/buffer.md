# buffer Class API Documentation

## Overview
The `buffer` class is a lightweight, non-owning wrapper around a dynamically allocated character buffer. It provides efficient memory management with move semantics and supports various container-like operations. The class is designed for high-performance networking applications, particularly in the libtorrent library.

## buffer

- **Signature**: `explicit buffer(difference_type size = 0)`
- **Description**: Constructs a buffer of the specified size. The buffer is initialized to contain uninitialized memory. This constructor rounds up the size to be 8 bytes aligned for optimal memory access on most platforms.
- **Parameters**:
  - `size` (difference_type): The requested size of the buffer in bytes. Must be less than `std::numeric_limits<std::int32_t>::max()`.
- **Return Value**:
  - None (constructor)
- **Exceptions/Errors**:
  - Throws `std::bad_alloc` if memory allocation fails
  - Asserts that `size < std::numeric_limits<std::int32_t>::max()` if the condition is violated
- **Example**:
```cpp
buffer my_buffer(1024);
// Buffer is now allocated with 1024 bytes of uninitialized memory
```
- **Preconditions**: `size < std::numeric_limits<std::int32_t>::max()`
- **Postconditions**: A buffer of the specified size is allocated and initialized
- **Thread Safety**: Not thread-safe (constructor creates a new instance)
- **Complexity**: O(1) time and space complexity
- **See Also**: `buffer(difference_type, span<char const>)`, `~buffer()`

## buffer

- **Signature**: `buffer(difference_type const size, span<char const> initialize)`
- **Description**: Constructs a buffer of the specified size and initializes it with the content from the provided span. The size of the initialization span must not exceed the buffer size.
- **Parameters**:
  - `size` (difference_type): The requested size of the buffer in bytes. Must be less than `std::numeric_limits<std::int32_t>::max()`.
  - `initialize` (span<char const>): A span containing the data to initialize the buffer with. The size of this span must be ≤ `size`.
- **Return Value**:
  - None (constructor)
- **Exceptions/Errors**:
  - Throws `std::bad_alloc` if memory allocation fails
  - Asserts that `initialize.size() <= size` if the condition is violated
- **Example**:
```cpp
std::vector<char> data = {'h', 'e', 'l', 'l', 'o'};
buffer my_buffer(10, span<char const>(data.data(), data.size()));
// Buffer is initialized with "hello" followed by zeros
```
- **Preconditions**: `size < std::numeric_limits<std::int32_t>::max()` and `initialize.size() <= size`
- **Postconditions**: Buffer is allocated and initialized with the provided data
- **Thread Safety**: Not thread-safe (constructor creates a new instance)
- **Complexity**: O(n) time complexity where n is the size of the initialization span
- **See Also**: `buffer()`, `operator=()`

## buffer

- **Signature**: `buffer(buffer const& b) = delete;`
- **Description**: Deleted copy constructor prevents copying of buffer objects. This enforces move semantics and prevents unintended memory sharing.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None (function is deleted, not callable)
- **Example**: Not applicable - attempting to copy will result in a compile-time error
```cpp
buffer b1(1024);
buffer b2 = b1; // Compilation error: copy constructor is deleted
```
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: N/A (function is deleted)
- **Complexity**: N/A
- **See Also**: `buffer(buffer&& b)`, `operator=(buffer&& b)`

## buffer

- **Signature**: `buffer(buffer&& b)`
- **Description**: Move constructor transfers ownership of the buffer from the source object to the new object. This is a non-throwing operation that efficiently transfers the internal pointer and size.
- **Parameters**:
  - `b` (buffer&&): The source buffer to move from. After the move, the source buffer is in a valid but unspecified state.
- **Return Value**: None
- **Exceptions/Errors**: None (no-throw guarantee)
- **Example**:
```cpp
buffer b1(1024);
buffer b2 = std::move(b1); // b1 is now in a valid but unspecified state
// b2 now owns the buffer that b1 previously owned
```
- **Preconditions**: The source buffer must be in a valid state
- **Postconditions**: The new buffer owns the resources previously owned by the source buffer, and the source buffer is in a valid but unspecified state
- **Thread Safety**: Not thread-safe (moves memory ownership)
- **Complexity**: O(1) time complexity
- **See Also**: `~buffer()`, `operator=(buffer&& b)`

## operator=

- **Signature**: `buffer& operator=(buffer&& b)`
- **Description**: Move assignment operator transfers ownership of the buffer from the source object to the current object. It handles self-assignment and properly deallocates existing resources before taking ownership of the new resources.
- **Parameters**:
  - `b` (buffer&&): The source buffer to move from. After the move, the source buffer is in a valid but unspecified state.
- **Return Value**:
  - `buffer&`: Reference to the current object (for method chaining)
- **Exceptions/Errors**: None (no-throw guarantee)
- **Example**:
```cpp
buffer b1(1024);
buffer b2;
b2 = std::move(b1); // b1 is now in a valid but unspecified state
// b2 now owns the buffer that b1 previously owned
```
- **Preconditions**: The source buffer must be in a valid state
- **Postconditions**: The current buffer owns the resources previously owned by the source buffer, and the source buffer is in a valid but unspecified state
- **Thread Safety**: Not thread-safe (moves memory ownership)
- **Complexity**: O(1) time complexity
- **See Also**: `buffer(buffer&& b)`, `~buffer()`

## ~buffer

- **Signature**: `~buffer()`
- **Description**: Destructor that frees the allocated memory when the buffer goes out of scope. This ensures proper cleanup of dynamically allocated memory.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None (no-throw guarantee)
- **Example**:
```cpp
{
    buffer b(1024);
    // Use buffer
} // Buffer is automatically cleaned up here
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: The allocated memory is freed and the buffer is destructed
- **Thread Safety**: Not thread-safe (modifies internal state)
- **Complexity**: O(1) time complexity
- **See Also**: `buffer()`, `operator=()`

## data

- **Signature**: `char* data()`
- **Description**: Returns a pointer to the beginning of the buffer. This allows direct access to the raw memory for read/write operations.
- **Parameters**: None
- **Return Value**:
  - `char*`: Pointer to the beginning of the buffer. The pointer is valid until the buffer is destroyed or modified.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(1024);
char* ptr = b.data();
// Use ptr to access or modify the buffer contents
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a valid pointer to the buffer's data
- **Thread Safety**: Not thread-safe (pointer may become invalid if buffer is modified)
- **Complexity**: O(1) time complexity
- **See Also**: `data() const`, `size()`

## data

- **Signature**: `char const* data() const`
- **Description**: Returns a constant pointer to the beginning of the buffer. This allows read-only access to the raw memory.
- **Parameters**: None
- **Return Value**:
  - `char const*`: Constant pointer to the beginning of the buffer. The pointer is valid until the buffer is destroyed or modified.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(1024);
char const* ptr = b.data();
// Use ptr to read the buffer contents (but not modify them)
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a valid constant pointer to the buffer's data
- **Thread Safety**: Not thread-safe (pointer may become invalid if buffer is modified)
- **Complexity**: O(1) time complexity
- **See Also**: `data()`, `size()`

## size

- **Signature**: `difference_type size() const`
- **Description**: Returns the current size of the buffer in bytes.
- **Parameters**: None
- **Return Value**:
  - `difference_type`: The size of the buffer in bytes. This value represents the amount of memory allocated for the buffer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(1024);
std::cout << "Buffer size: " << b.size() << " bytes" << std::endl;
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns the current size of the buffer
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time complexity
- **See Also**: `empty()`, `data()`

## empty

- **Signature**: `bool empty() const`
- **Description**: Checks if the buffer is empty (has zero size).
- **Parameters**: None
- **Return Value**:
  - `bool`: Returns `true` if the buffer has zero size, `false` otherwise.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(0);
if (b.empty()) {
    std::cout << "Buffer is empty" << std::endl;
}
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns `true` if the buffer has zero size
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time complexity
- **See Also**: `size()`, `data()`

## operator[]

- **Signature**: `char& operator[](index_type const i)`
- **Description**: Returns a reference to the character at the specified index with bounds checking. This operator provides safe access to buffer elements and asserts that the index is within bounds.
- **Parameters**:
  - `i` (index_type): The index of the character to access. Must be less than the buffer size.
- **Return Value**:
  - `char&`: Reference to the character at the specified index.
- **Exceptions/Errors**: Throws an assertion failure if `i >= size()` (debug builds only)
- **Example**:
```cpp
buffer b(10);
b[0] = 'a';
char c = b[0]; // c is now 'a'
```
- **Preconditions**: The buffer must be in a valid state and `i < size()`
- **Postconditions**: Returns a reference to the character at the specified index
- **Thread Safety**: Not thread-safe (modifies buffer content)
- **Complexity**: O(1) time complexity
- **See Also**: `operator[] const`, `data()`

## operator[]

- **Signature**: `char const& operator[](difference_type const i) const`
- **Description**: Returns a constant reference to the character at the specified index with bounds checking. This operator provides safe read-only access to buffer elements and asserts that the index is within bounds.
- **Parameters**:
  - `i` (difference_type): The index of the character to access. Must be less than the buffer size.
- **Return Value**:
  - `char const&`: Constant reference to the character at the specified index.
- **Exceptions/Errors**: Throws an assertion failure if `i >= size()` (debug builds only)
- **Example**:
```cpp
buffer b(10);
b[0] = 'a';
char c = b[0]; // c is now 'a'
```
- **Preconditions**: The buffer must be in a valid state and `i < size()`
- **Postconditions**: Returns a constant reference to the character at the specified index
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time complexity
- **See Also**: `operator[]`, `data()`

## begin

- **Signature**: `char* begin()`
- **Description**: Returns a pointer to the beginning of the buffer. This function provides direct access to the buffer's data for iteration purposes.
- **Parameters**: None
- **Return Value**:
  - `char*`: Pointer to the beginning of the buffer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(10);
for (char* p = b.begin(); p != b.end(); ++p) {
    *p = 'x'; // Fill buffer with 'x' characters
}
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a pointer to the beginning of the buffer
- **Thread Safety**: Not thread-safe (pointer may become invalid if buffer is modified)
- **Complexity**: O(1) time complexity
- **See Also**: `end()`, `data()`

## begin

- **Signature**: `char const* begin() const`
- **Description**: Returns a constant pointer to the beginning of the buffer. This function provides read-only access to the buffer's data for iteration purposes.
- **Parameters**: None
- **Return Value**:
  - `char const*`: Constant pointer to the beginning of the buffer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(10);
b[0] = 'a';
b[1] = 'b';
for (char const* p = b.begin(); p != b.end(); ++p) {
    std::cout << *p << std::endl; // Print all characters
}
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a constant pointer to the beginning of the buffer
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time complexity
- **See Also**: `end()`, `data()`

## end

- **Signature**: `char* end()`
- **Description**: Returns a pointer to the position immediately after the last element of the buffer. This function is used for iteration purposes to define the end of the buffer.
- **Parameters**: None
- **Return Value**:
  - `char*`: Pointer to the position immediately after the last element of the buffer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(10);
for (char* p = b.begin(); p != b.end(); ++p) {
    *p = 'x'; // Fill buffer with 'x' characters
}
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a pointer to the position after the last element of the buffer
- **Thread Safety**: Not thread-safe (pointer may become invalid if buffer is modified)
- **Complexity**: O(1) time complexity
- **See Also**: `begin()`, `data()`

## end

- **Signature**: `char const* end() const`
- **Description**: Returns a constant pointer to the position immediately after the last element of the buffer. This function is used for iteration purposes to define the end of the buffer.
- **Parameters**: None
- **Return Value**:
  - `char const*`: Constant pointer to the position after the last element of the buffer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
buffer b(10);
b[0] = 'a';
b[1] = 'b';
for (char const* p = b.begin(); p != b.end(); ++p) {
    std::cout << *p << std::endl; // Print all characters
}
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: Returns a constant pointer to the position after the last element of the buffer
- **Thread Safety**: Thread-safe (const method)
- **Complexity**: O(1) time complexity
- **See Also**: `begin()`, `data()`

## swap

- **Signature**: `void swap(buffer& b)`
- **Description**: Swaps the contents of this buffer with another buffer. This operation is efficient and does not throw exceptions.
- **Parameters**:
  - `b` (buffer&): The buffer to swap with.
- **Return Value**: None
- **Exceptions/Errors**: None (no-throw guarantee)
- **Example**:
```cpp
buffer b1(1024);
buffer b2(512);
b1.swap(b2); // Now b1 has 512 bytes and b2 has 1024 bytes
```
- **Preconditions**: The buffer must be in a valid state
- **Postconditions**: The contents of the two buffers are swapped
- **Thread Safety**: Not thread-safe (modifies internal state)
- **Complexity**: O(1) time complexity
- **See Also**: `buffer(buffer&& b)`, `operator=(buffer&& b)`

# Usage Examples

## Basic Usage

```cpp
#include <iostream>
#include <vector>
#include "libtorrent/aux_/buffer.hpp"

int main() {
    // Create a buffer of 1024 bytes
    buffer b(1024);
    
    // Fill buffer with data
    std::vector<char> data = {'h', 'e', 'l', 'l', 'o'};
    std::copy(data.begin(), data.end(), b.data());
    
    // Access data using the [] operator
    for (int i = 0; i < data.size(); ++i) {
        std::cout << b[i] << " ";
    }
    std::cout << std::endl;
    
    // Iterate over buffer
    for (char* p = b.begin();