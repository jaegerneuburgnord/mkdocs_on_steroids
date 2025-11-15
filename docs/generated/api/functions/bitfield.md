# libtorrent::bitfield API Documentation

## bitfield (Default Constructor)

- **Signature**: `bitfield() noexcept = default;`
- **Description**: Default constructor that creates an empty bitfield. The bitfield starts with zero bits and no allocated storage.
- **Parameters**: None
- **Return Value**: A new bitfield object initialized to empty state
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf;
// bf is now an empty bitfield
```
- **Preconditions**: None
- **Postconditions**: The bitfield is in a valid state with size 0
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## bitfield (Size Constructor)

- **Signature**: `explicit bitfield(int bits);`
- **Description**: Constructs a bitfield of specified size, initializing all bits to 0.
- **Parameters**:
  - `bits` (int): The number of bits to allocate in the bitfield. Must be non-negative.
- **Return Value**: A new bitfield object initialized with the specified size
- **Exceptions/Errors**: None (but may throw if memory allocation fails)
- **Example**:
```cpp
bitfield bf(100);
// bf is now a bitfield of 100 bits, all set to 0
```
- **Preconditions**: `bits >= 0`
- **Postconditions**: The bitfield has the specified size with all bits initialized to 0
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) amortized for the resize operation

## bitfield (Size and Value Constructor)

- **Signature**: `bitfield(int bits, bool val);`
- **Description**: Constructs a bitfield of specified size, initializing all bits to the specified value.
- **Parameters**:
  - `bits` (int): The number of bits to allocate in the bitfield. Must be non-negative.
  - `val` (bool): The value to initialize all bits to (true for 1, false for 0).
- **Return Value**: A new bitfield object initialized with the specified size and value
- **Exceptions/Errors**: None (but may throw if memory allocation fails)
- **Example**:
```cpp
bitfield bf(100, true);
// bf is now a bitfield of 100 bits, all set to 1
```
- **Preconditions**: `bits >= 0`
- **Postconditions**: The bitfield has the specified size with all bits initialized to `val`
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) amortized for the resize operation

## bitfield (Buffer Constructor)

- **Signature**: `bitfield(char const* b, int bits);`
- **Description**: Constructs a bitfield from a buffer of bytes, using the specified number of bits.
- **Parameters**:
  - `b` (char const*): Pointer to a buffer containing bit data.
  - `bits` (int): The number of bits to read from the buffer. Must be non-negative.
- **Return Value**: A new bitfield object initialized with the specified data
- **Exceptions/Errors**: None (but may throw if memory allocation fails)
- **Example**:
```cpp
char buffer[10] = {0x01, 0x02, 0x03, 0x04, 0x05};
bitfield bf(buffer, 40);
// bf is now a bitfield of 40 bits with data from the buffer
```
- **Preconditions**: `bits >= 0`, `b` must be valid for `bits` bits
- **Postconditions**: The bitfield has the specified size with data copied from the buffer
- **Thread Safety**: Thread-safe
- **Complexity**: O(bits/8)

## bitfield (Copy Constructor)

- **Signature**: `bitfield(bitfield const& rhs);`
- **Description**: Copy constructor that creates a bitfield identical to the given bitfield.
- **Parameters**:
  - `rhs` (bitfield const&): The bitfield to copy from.
- **Return Value**: A new bitfield object with the same content as the source
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf1(100);
bitfield bf2(bf1);
// bf2 is now a copy of bf1
```
- **Preconditions**: `rhs` must be a valid bitfield
- **Postconditions**: The new bitfield has the same size and bit values as the source
- **Thread Safety**: Thread-safe
- **Complexity**: O(bits/8)

## bitfield (Move Constructor)

- **Signature**: `bitfield(bitfield&& rhs) noexcept;`
- **Description**: Move constructor that transfers ownership of the bitfield data from the source.
- **Parameters**:
  - `rhs` (bitfield&&): The bitfield to move from.
- **Return Value**: A new bitfield object with the data from the source
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf1(100);
bitfield bf2(std::move(bf1));
// bf2 now owns the data that bf1 previously owned
```
- **Preconditions**: `rhs` must be a valid bitfield
- **Postconditions**: The source bitfield is left in a valid but unspecified state, the destination bitfield has the same content as the source
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## assign

- **Signature**: `void assign(char const* b, int const bits);`
- **Description**: Assigns the specified number of bits from a buffer to the bitfield, resizing if necessary.
- **Parameters**:
  - `b` (char const*): Pointer to a buffer containing bit data.
  - `bits` (int): The number of bits to assign from the buffer. Must be non-negative.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf;
bf.assign(buffer, 40);
// bf now contains 40 bits from the buffer
```
- **Preconditions**: `bits >= 0`, `b` must be valid for `bits` bits
- **Postconditions**: The bitfield has the specified size with data copied from the buffer
- **Thread Safety**: Thread-safe
- **Complexity**: O(bits/8)

## operator[] (Bit Access)

- **Signature**: `bool operator[](int index) const noexcept;`
- **Description**: Accesses the bit at the specified index (0-based).
- **Parameters**:
  - `index` (int): The index of the bit to access. Must be in range [0, size()).
- **Return Value**: The value of the bit at the specified index (true or false)
- **Exceptions/Errors**: None (but asserts if index is out of bounds)
- **Example**:
```cpp
bitfield bf(100);
bf[50] = true;
bool value = bf[50];
// value is now true
```
- **Preconditions**: `index >= 0`, `index < size()`
- **Postconditions**: The bit at the specified index is accessed
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## get_bit

- **Signature**: `bool get_bit(int index) const noexcept;`
- **Description**: Gets the bit value at the specified index (0-based).
- **Parameters**:
  - `index` (int): The index of the bit to get. Must be in range [0, size()).
- **Return Value**: The value of the bit at the specified index (true or false)
- **Exceptions/Errors**: None (but asserts if index is out of bounds)
- **Example**:
```cpp
bitfield bf(100);
bf.set_bit(50);
bool value = bf.get_bit(50);
// value is now true
```
- **Preconditions**: `index >= 0`, `index < size()`
- **Postconditions**: The bit at the specified index is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## clear_bit

- **Signature**: `void clear_bit(int index) noexcept;`
- **Description**: Clears the bit at the specified index (sets it to 0).
- **Parameters**:
  - `index` (int): The index of the bit to clear. Must be in range [0, size()).
- **Return Value**: None
- **Exceptions/Errors**: None (but asserts if index is out of bounds)
- **Example**:
```cpp
bitfield bf(100);
bf.set_bit(50);
bf.clear_bit(50);
// The bit at index 50 is now 0
```
- **Preconditions**: `index >= 0`, `index < size()`
- **Postconditions**: The bit at the specified index is cleared (set to 0)
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## set_bit

- **Signature**: `void set_bit(int index) noexcept;`
- **Description**: Sets the bit at the specified index (sets it to 1).
- **Parameters**:
  - `index` (int): The index of the bit to set. Must be in range [0, size()).
- **Return Value**: None
- **Exceptions/Errors**: None (but asserts if index is out of bounds)
- **Example**:
```cpp
bitfield bf(100);
bf.set_bit(50);
// The bit at index 50 is now 1
```
- **Preconditions**: `index >= 0`, `index < size()`
- **Postconditions**: The bit at the specified index is set (set to 1)
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## none_set

- **Signature**: `bool none_set() const noexcept;`
- **Description**: Checks if no bits are set in the bitfield.
- **Parameters**: None
- **Return Value**: True if no bits are set, false otherwise
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
bool all_clear = bf.none_set();
// all_clear is true if no bits are set
```
- **Preconditions**: None
- **Postconditions**: The result indicates whether any bits are set
- **Thread Safety**: Thread-safe
- **Complexity**: O(num_words())

## size

- **Signature**: `int size() const noexcept;`
- **Description**: Gets the number of bits in the bitfield.
- **Parameters**: None
- **Return Value**: The number of bits in the bitfield
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
int bits = bf.size();
// bits is now 100
```
- **Preconditions**: None
- **Postconditions**: The size of the bitfield is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## num_words

- **Signature**: `int num_words() const noexcept;`
- **Description**: Gets the number of 32-bit words needed to store the bitfield.
- **Parameters**: None
- **Return Value**: The number of 32-bit words needed to store the bitfield
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
int words = bf.num_words();
// words is now 4 (100 bits require 4 32-bit words)
```
- **Preconditions**: None
- **Postconditions**: The number of words needed is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## num_bytes

- **Signature**: `int num_bytes() const noexcept;`
- **Description**: Gets the number of bytes needed to store the bitfield.
- **Parameters**: None
- **Return Value**: The number of bytes needed to store the bitfield
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
int bytes = bf.num_bytes();
// bytes is now 13 (100 bits require 13 bytes)
```
- **Preconditions**: None
- **Postconditions**: The number of bytes needed is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## empty

- **Signature**: `bool empty() const noexcept;`
- **Description**: Checks if the bitfield is empty (has zero bits).
- **Parameters**: None
- **Return Value**: True if the bitfield has zero bits, false otherwise
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(0);
bool is_empty = bf.empty();
// is_empty is true
```
- **Preconditions**: None
- **Postconditions**: The result indicates whether the bitfield is empty
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## data (const)

- **Signature**: `char const* data() const noexcept;`
- **Description**: Gets a pointer to the underlying data buffer.
- **Parameters**: None
- **Return Value**: A pointer to the first byte of the bitfield data
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
char const* data = bf.data();
// data points to the first byte of the bitfield
```
- **Preconditions**: None
- **Postconditions**: A pointer to the underlying data is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## data

- **Signature**: `char* data() noexcept;`
- **Description**: Gets a pointer to the underlying data buffer (non-const version).
- **Parameters**: None
- **Return Value**: A pointer to the first byte of the bitfield data
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
char* data = bf.data();
// data points to the first byte of the bitfield
```
- **Preconditions**: None
- **Postconditions**: A pointer to the underlying data is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## bytes (Deprecated)

- **Signature**: `TORRENT_DEPRECATED char const* bytes() const;`
- **Description**: Gets a pointer to the underlying data buffer. This function is deprecated and should not be used in new code.
- **Parameters**: None
- **Return Value**: A pointer to the first byte of the bitfield data
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
char const* data = bf.bytes();
// data points to the first byte of the bitfield
```
- **Preconditions**: None
- **Postconditions**: A pointer to the underlying data is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `data()`

## operator=

- **Signature**: `bitfield& operator=(bitfield const& rhs) &;`
- **Description**: Assignment operator that copies the content of another bitfield.
- **Parameters**:
  - `rhs` (bitfield const&): The bitfield to copy from.
- **Return Value**: A reference to the current bitfield
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf1(100);
bitfield bf2(200);
bf2 = bf1;
// bf2 now contains the same data as bf1
```
- **Preconditions**: `rhs` must be a valid bitfield
- **Postconditions**: The bitfield has the same content as the source
- **Thread Safety**: Thread-safe
- **Complexity**: O(bits/8)

## swap

- **Signature**: `void swap(bitfield& rhs) noexcept;`
- **Description**: Swaps the contents of two bitfields.
- **Parameters**:
  - `rhs` (bitfield&): The bitfield to swap with.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf1(100);
bitfield bf2(200);
bf1.swap(bf2);
// bf1 now contains the data that bf2 previously had
```
- **Preconditions**: `rhs` must be a valid bitfield
- **Postconditions**: The contents of the two bitfields are swapped
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## operator*

- **Signature**: `bool operator*() noexcept;`
- **Description**: Returns the value of the current bit in the iterator.
- **Parameters**: None
- **Return Value**: The value of the current bit (true or false)
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
auto it = bf.begin();
bool value = *it;
// value contains the value of the first bit
```
- **Preconditions**: The iterator must be valid
- **Postconditions**: The value of the current bit is returned
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## operator++ (Pre-increment)

- **Signature**: `const_iterator& operator++() noexcept;`
- **Description**: Pre-increment operator that advances the iterator to the next bit.
- **Parameters**: None
- **Return Value**: A reference to the updated iterator
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
auto it = bf.begin();
++it;
// it now points to the second bit
```
- **Preconditions**: The iterator must be valid
- **Postconditions**: The iterator is advanced to the next bit
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)

## operator++ (Post-increment)

- **Signature**: `const_iterator operator++(int) noexcept;`
- **Description**: Post-increment operator that advances the iterator to the next bit.
- **Parameters**: None
- **Return Value**: A copy of the iterator before the increment
- **Exceptions/Errors**: None
- **Example**:
```cpp
bitfield bf(100);
auto it = bf.begin();
auto old_it = it++;
//