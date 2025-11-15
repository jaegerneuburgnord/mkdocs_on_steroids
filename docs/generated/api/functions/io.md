# libtorrent IO API Documentation

## read_impl

### Signature
`template <typename T> auto read_impl(InIt& start, type<T>)`

### Description
Reads a value of type T from the input iterator position and returns it. This function is a generic implementation for reading various integer types from a byte stream. It handles the byte-ordering by reading bytes from least significant to most significant, shifting each byte into place.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the data to read. This parameter is modified to point to the position after the read value.
- `type<T>`: A type tag indicating the type of value to read. This is used for template specialization.

### Return Value
- Returns the value of type T read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes that the input iterator has sufficient valid data for the requested type.

### Example
```cpp
std::vector<uint8_t> data = {0x01, 0x00, 0x00, 0x00}; // 1 in little-endian
auto it = data.begin();
std::uint32_t result = read_impl(it, type<std::uint32_t>());
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least sizeof(T) bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by sizeof(T) positions.
- The returned value contains the bytes from the input stream in the correct order.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `write_impl()`
- `read_uint32()`

---

## read_impl (std::uint8_t)

### Signature
`std::uint8_t read_impl(InIt& start, type<std::uint8_t>)`

### Description
Specialized version of `read_impl` for reading a single byte (std::uint8_t). This is a more efficient implementation for reading individual bytes.

### Parameters
- `start` (InIt&): Iterator pointing to the byte to read. This parameter is modified to point to the next byte.
- `type<std::uint8_t>`: A type tag indicating the type of value to read.

### Return Value
- Returns the byte value as std::uint8_t.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the iterator points to valid memory.

### Example
```cpp
std::vector<uint8_t> data = {0x42};
auto it = data.begin();
std::uint8_t result = read_impl(it, type<std::uint8_t>());
// result = 66 (0x42 in decimal)
```

### Preconditions
- The input iterator must point to valid memory.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 1 position.
- The returned value contains the byte at the original iterator position.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_uint8()`

---

## read_impl (std::int8_t)

### Signature
`std::int8_t read_impl(InIt& start, type<std::int8_t>)`

### Description
Specialized version of `read_impl` for reading a single signed byte (std::int8_t). This implementation handles signed integers correctly.

### Parameters
- `start` (InIt&): Iterator pointing to the byte to read. This parameter is modified to point to the next byte.
- `type<std::int8_t>`: A type tag indicating the type of value to read.

### Return Value
- Returns the signed byte value as std::int8_t.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the iterator points to valid memory.

### Example
```cpp
std::vector<uint8_t> data = {0xFF}; // -1 in two's complement
auto it = data.begin();
std::int8_t result = read_impl(it, type<std::int8_t>());
// result = -1
```

### Preconditions
- The input iterator must point to valid memory.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 1 position.
- The returned value contains the byte at the original iterator position, interpreted as a signed integer.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_int8()`

---

## write_impl (Integral Types)

### Signature
```cpp
typename std::enable_if<(std::is_integral<In>::value
    && !std::is_same<In, bool>::value)
    || std::is_enum<In>::value, void>::type
write_impl(In data, OutIt& start)
```

### Description
Generic implementation for writing integral types (including enums) to an output iterator. This function writes the data in little-endian byte order, one byte at a time.

### Parameters
- `data` (In): The value to write to the output stream.
- `start` (OutIt&): Iterator pointing to the location where the data should be written. This parameter is modified to point to the position after the written data.

### Return Value
- void

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the output iterator has sufficient space for the data.

### Example
```cpp
std::vector<uint8_t> buffer(4);
auto it = buffer.begin();
write_impl<std::uint32_t>(0x12345678, it);
// buffer = {0x78, 0x56, 0x34, 0x12}
```

### Preconditions
- The output iterator must be dereferenceable and have sufficient space for the data.
- The data type must be an integral type or enum.

### Postconditions
- The iterator is advanced by sizeof(In) positions.
- The memory at the original iterator position contains the bytes of the data in little-endian order.

### Thread Safety
- The function is thread-safe as long as the output iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `write_impl<bool>()`
- `write_uint32()`

---

## write_impl (bool)

### Signature
```cpp
typename std::enable_if<std::is_same<Val, bool>::value, void>::type
write_impl(Val val, OutIt& start)
```

### Description
Specialized implementation for writing boolean values to an output iterator. This function converts the boolean value to 1 or 0 and writes the result.

### Parameters
- `val` (Val): The boolean value to write. True values are written as 1, false as 0.
- `start` (OutIt&): Iterator pointing to the location where the data should be written. This parameter is modified to point to the position after the written data.

### Return Value
- void

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the output iterator has sufficient space for the data.

### Example
```cpp
std::vector<uint8_t> buffer(1);
auto it = buffer.begin();
write_impl(true, it);
// buffer = {0x01}
```

### Preconditions
- The output iterator must be dereferenceable and have sufficient space for the data.
- The data type must be boolean.

### Postconditions
- The iterator is advanced by 1 position.
- The memory at the original iterator position contains 1 if val is true, 0 otherwise.

### Thread Safety
- The function is thread-safe as long as the output iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `write_impl<Integral Types>()`
- `write_bool()`

---

## read_int64

### Signature
`std::int64_t read_int64(InIt& start)`

### Description
Reads an int64_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 64-bit integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the int64_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 64-bit integer.

### Example
```cpp
std::vector<uint8_t> data = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01}; // 1 in little-endian
auto it = data.begin();
std::int64_t result = read_int64(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 8 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 8 positions.
- The returned value contains the 64-bit integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_uint64()`

---

## read_uint64

### Signature
`std::uint64_t read_uint64(InIt& start)`

### Description
Reads a uint64_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 64-bit unsigned integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the uint64_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 64-bit unsigned integer.

### Example
```cpp
std::vector<uint8_t> data = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01}; // 1 in little-endian
auto it = data.begin();
std::uint64_t result = read_uint64(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 8 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 8 positions.
- The returned value contains the 64-bit unsigned integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_int64()`

---

## read_uint32

### Signature
`std::uint32_t read_uint32(InIt& start)`

### Description
Reads a uint32_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 32-bit unsigned integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the uint32_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 32-bit unsigned integer.

### Example
```cpp
std::vector<uint8_t> data = {0x01, 0x00, 0x00, 0x00}; // 1 in little-endian
auto it = data.begin();
std::uint32_t result = read_uint32(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 4 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 4 positions.
- The returned value contains the 32-bit unsigned integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_int32()`

---

## read_int32

### Signature
`std::int32_t read_int32(InIt& start)`

### Description
Reads an int32_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 32-bit integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the int32_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 32-bit integer.

### Example
```cpp
std::vector<uint8_t> data = {0x01, 0x00, 0x00, 0x00}; // 1 in little-endian
auto it = data.begin();
std::int32_t result = read_int32(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 4 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 4 positions.
- The returned value contains the 32-bit integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_uint32()`

---

## read_int16

### Signature
`std::int16_t read_int16(InIt& start)`

### Description
Reads an int16_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 16-bit integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the int16_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 16-bit integer.

### Example
```cpp
std::vector<uint8_t> data = {0x01, 0x00}; // 1 in little-endian
auto it = data.begin();
std::int16_t result = read_int16(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 2 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 2 positions.
- The returned value contains the 16-bit integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_uint16()`

---

## read_uint16

### Signature
`std::uint16_t read_uint16(InIt& start)`

### Description
Reads a uint16_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 16-bit unsigned integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the uint16_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the 16-bit unsigned integer.

### Example
```cpp
std::vector<uint8_t> data = {0x01, 0x00}; // 1 in little-endian
auto it = data.begin();
std::uint16_t result = read_uint16(it);
// result = 1
```

### Preconditions
- The input iterator must point to valid memory containing at least 2 bytes.
- The iterator must be dereferenceable.

### Postconditions
- The iterator is advanced by 2 positions.
- The returned value contains the 16-bit unsigned integer from the input stream.

### Thread Safety
- The function is thread-safe as long as the input iterator is not being modified by other threads concurrently.

### Complexity
- Time: O(1)
- Space: O(1)

### See Also
- `read_impl()`
- `read_int16()`

---

## read_int8

### Signature
`std::int8_t read_int8(InIt& start)`

### Description
Reads an int8_t value from the input iterator position. This function is a convenience wrapper around the generic `read_impl` function.

### Parameters
- `start` (InIt&): Iterator pointing to the beginning of the 8-bit integer to read. This parameter is modified to point to the position after the read value.

### Return Value
- Returns the int8_t value read from the input stream.

### Exceptions/Errors
- No exceptions are thrown.
- The function assumes the input iterator has sufficient valid data for the