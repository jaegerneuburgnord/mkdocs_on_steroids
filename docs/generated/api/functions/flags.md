# libtorrent Flags API Documentation

## bit_t

- **Signature**: `explicit constexpr bit_t(int b)`
- **Description**: Constructs a `bit_t` object representing a specific bit position. This is a lightweight wrapper around an integer that represents a bit index, primarily used to create bitfield flags.
- **Parameters**:
  - `b` (int): The bit index to represent. Must be a non-negative integer. Values beyond the range of the underlying type may result in undefined behavior.
- **Return Value**:
  - A `bit_t` object representing the specified bit position.
- **Exceptions/Errors**:
  - None. The constructor is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
auto bit = bit_t{5}; // Create a bit_t representing bit 5
```
- **Preconditions**: None.
- **Postconditions**: The constructed `bit_t` object will represent the specified bit index.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `operator ""_bit`, `bitfield_flag`

## int

- **Signature**: `explicit constexpr operator int() const`
- **Description**: Converts a `bit_t` object to an integer representing the bit index. This operator allows implicit conversion of `bit_t` objects to integers.
- **Parameters**: None.
- **Return Value**:
  - The integer value representing the bit index.
- **Exceptions/Errors**:
  - None. The conversion is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
auto bit = bit_t{5};
int bit_index = bit; // bit_index will be 5
```
- **Preconditions**: The `bit_t` object must have been constructed with a valid bit index.
- **Postconditions**: The returned integer will represent the bit index stored in the `bit_t` object.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bit_t`, `operator ""_bit`

## _bit

- **Signature**: `constexpr bit_t operator ""_bit(unsigned long long int b)`
- **Description**: Literal operator for creating `bit_t` objects from integer literals. This operator allows the use of bit positions in a more readable syntax, such as `5_bit`.
- **Parameters**:
  - `b` (unsigned long long int): The bit index to represent. Must be a non-negative integer.
- **Return Value**:
  - A `bit_t` object representing the specified bit index.
- **Exceptions/Errors**:
  - None. The operator is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
auto bit = 5_bit; // Create a bit_t representing bit 5
```
- **Preconditions**: The bit index must be a non-negative integer.
- **Postconditions**: The returned `bit_t` object will represent the specified bit index.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bit_t`, `int`

## bitfield_flag (copy constructor)

- **Signature**: `constexpr bitfield_flag(bitfield_flag const& rhs) noexcept`
- **Description**: Copy constructor for `bitfield_flag`. Creates a new `bitfield_flag` object as a copy of another `bitfield_flag` object. This constructor is `constexpr` and `noexcept`.
- **Parameters**:
  - `rhs` (bitfield_flag const&): The `bitfield_flag` object to copy.
- **Return Value**:
  - A new `bitfield_flag` object as a copy of `rhs`.
- **Exceptions/Errors**:
  - None. The constructor is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag1;
bitfield_flag flag2 = flag1; // Copy constructor called
```
- **Preconditions**: The `bitfield_flag` object `rhs` must be valid.
- **Postconditions**: The new `bitfield_flag` object will have the same value as `rhs`.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bitfield_flag (move constructor)`, `bitfield_flag (default constructor)`

## bitfield_flag (move constructor)

- **Signature**: `constexpr bitfield_flag(bitfield_flag&& rhs) noexcept`
- **Description**: Move constructor for `bitfield_flag`. Transfers ownership of the value from another `bitfield_flag` object to a new `bitfield_flag` object. This constructor is `constexpr` and `noexcept`.
- **Parameters**:
  - `rhs` (bitfield_flag&&): The `bitfield_flag` object to move from.
- **Return Value**:
  - A new `bitfield_flag` object with the value moved from `rhs`.
- **Exceptions/Errors**:
  - None. The constructor is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag1;
bitfield_flag flag2 = std::move(flag1); // Move constructor called
```
- **Preconditions**: The `bitfield_flag` object `rhs` must be valid.
- **Postconditions**: The new `bitfield_flag` object will have the value of `rhs`, and `rhs` will be in a valid but unspecified state.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bitfield_flag (copy constructor)`, `bitfield_flag (default constructor)`

## bitfield_flag (default constructor)

- **Signature**: `constexpr bitfield_flag() noexcept`
- **Description**: Default constructor for `bitfield_flag`. Creates a `bitfield_flag` object initialized to zero (no bits set).
- **Parameters**: None.
- **Return Value**:
  - A `bitfield_flag` object with all bits cleared (value 0).
- **Exceptions/Errors**:
  - None. The constructor is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag; // flag is initialized to 0
```
- **Preconditions**: None.
- **Postconditions**: The `bitfield_flag` object will have a value of 0.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bitfield_flag (explicit constructor)`, `bitfield_flag (bit constructor)`

## bitfield_flag (explicit constructor)

- **Signature**: `explicit constexpr bitfield_flag(UnderlyingType const val) noexcept`
- **Description**: Explicit constructor for `bitfield_flag`. Creates a `bitfield_flag` object with the specified value.
- **Parameters**:
  - `val` (UnderlyingType const): The initial value of the bitfield flag.
- **Return Value**:
  - A `bitfield_flag` object with the specified value.
- **Exceptions/Errors**:
  - None. The constructor is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag(0x01); // Create a bitfield flag with value 1
```
- **Preconditions**: The `val` parameter must be a valid `UnderlyingType` value.
- **Postconditions**: The `bitfield_flag` object will have the specified value.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bitfield_flag (default constructor)`, `bitfield_flag (bit constructor)`

## bitfield_flag (bit constructor)

- **Signature**: `constexpr bitfield_flag(bit_t const bit) noexcept`
- **Description**: Constructor for `bitfield_flag` that creates a flag with a single bit set. The bit index is specified using a `bit_t` object.
- **Parameters**:
  - `bit` (bit_t const): The bit position to set.
- **Return Value**:
  - A `bitfield_flag` object with the specified bit set.
- **Exceptions/Errors**:
  - None. The constructor is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
auto bit = 5_bit;
bitfield_flag flag(bit); // Create a bitfield flag with bit 5 set
```
- **Preconditions**: The `bit` parameter must be a valid `bit_t` object.
- **Postconditions**: The `bitfield_flag` object will have the specified bit set and all other bits cleared.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bit_t`, `bitfield_flag (default constructor)`, `bitfield_flag (explicit constructor)`

## UnderlyingType (implicit conversion)

- **Signature**: `constexpr operator UnderlyingType() const noexcept`
- **Description**: Implicit conversion operator to the underlying type. This allows a `bitfield_flag` object to be used wherever the underlying type is expected.
- **Parameters**: None.
- **Return Value**:
  - The underlying integer value of the bitfield flag.
- **Exceptions/Errors**:
  - None. The conversion is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag;
UnderlyingType value = flag; // Implicit conversion
```
- **Preconditions**: The `bitfield_flag` object must be valid.
- **Postconditions**: The returned value will be the underlying integer value of the bitfield flag.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `UnderlyingType (explicit conversion)`, `bitfield_flag`

## UnderlyingType (explicit conversion)

- **Signature**: `explicit constexpr operator UnderlyingType() const noexcept`
- **Description**: Explicit conversion operator to the underlying type. This allows a `bitfield_flag` object to be converted to the underlying type, but requires explicit casting.
- **Parameters**: None.
- **Return Value**:
  - The underlying integer value of the bitfield flag.
- **Exceptions/Errors**:
  - None. The conversion is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag;
UnderlyingType value = static_cast<UnderlyingType>(flag); // Explicit conversion
```
- **Preconditions**: The `bitfield_flag` object must be valid.
- **Postconditions**: The returned value will be the underlying integer value of the bitfield flag.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `UnderlyingType (implicit conversion)`, `bitfield_flag`

## bool

- **Signature**: `explicit constexpr operator bool() const noexcept`
- **Description**: Explicit conversion operator to `bool`. This operator allows a `bitfield_flag` object to be used in boolean contexts, returning `true` if any bit is set and `false` otherwise.
- **Parameters**: None.
- **Return Value**:
  - `true` if any bit is set in the bitfield flag, `false` otherwise.
- **Exceptions/Errors**:
  - None. The conversion is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag;
if (flag) {
    // flag has at least one bit set
}
```
- **Preconditions**: The `bitfield_flag` object must be valid.
- **Postconditions**: The returned value will be `true` if any bit is set, `false` otherwise.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `UnderlyingType`, `bitfield_flag`

## all

- **Signature**: `static constexpr bitfield_flag all()`
- **Description**: Returns a `bitfield_flag` object with all bits set. This is useful for creating a bitfield flag that represents all possible bits.
- **Parameters**: None.
- **Return Value**:
  - A `bitfield_flag` object with all bits set.
- **Exceptions/Errors**:
  - None. The function is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag all_bits = bitfield_flag::all(); // all_bits has all bits set
```
- **Preconditions**: None.
- **Postconditions**: The returned `bitfield_flag` object will have all bits set.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `bitfield_flag`, `operator|`, `operator&`, `operator^`

## bitfield_flag (operator|)

- **Signature**: `bitfield_flag operator|(bitfield_flag const lhs, bitfield_flag const rhs) noexcept`
- **Description**: Bitwise OR operator for `bitfield_flag` objects. Returns a new `bitfield_flag` object with all bits set that are set in either of the operands.
- **Parameters**:
  - `lhs` (bitfield_flag const): The left-hand side operand.
  - `rhs` (bitfield_flag const): The right-hand side operand.
- **Return Value**:
  - A `bitfield_flag` object with all bits set that are set in either `lhs` or `rhs`.
- **Exceptions/Errors**:
  - None. The operator is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag1;
bitfield_flag flag2;
bitfield_flag result = flag1 | flag2; // result has all bits set that are set in either flag1 or flag2
```
- **Preconditions**: Both `lhs` and `rhs` must be valid `bitfield_flag` objects.
- **Postconditions**: The returned `bitfield_flag` object will have all bits set that are set in either `lhs` or `rhs`.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `operator&`, `operator^`, `operator~`, `all`

## bitfield_flag (operator&)

- **Signature**: `bitfield_flag operator&(bitfield_flag const lhs, bitfield_flag const rhs) noexcept`
- **Description**: Bitwise AND operator for `bitfield_flag` objects. Returns a new `bitfield_flag` object with bits set only where both operands have bits set.
- **Parameters**:
  - `lhs` (bitfield_flag const): The left-hand side operand.
  - `rhs` (bitfield_flag const): The right-hand side operand.
- **Return Value**:
  - A `bitfield_flag` object with bits set only where both `lhs` and `rhs` have bits set.
- **Exceptions/Errors**:
  - None. The operator is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag1;
bitfield_flag flag2;
bitfield_flag result = flag1 & flag2; // result has bits set only where both flag1 and flag2 have bits set
```
- **Preconditions**: Both `lhs` and `rhs` must be valid `bitfield_flag` objects.
- **Postconditions**: The returned `bitfield_flag` object will have bits set only where both `lhs` and `rhs` have bits set.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `operator|`, `operator^`, `operator~`, `all`

## bitfield_flag (operator^)

- **Signature**: `bitfield_flag operator^(bitfield_flag const lhs, bitfield_flag const rhs) noexcept`
- **Description**: Bitwise XOR operator for `bitfield_flag` objects. Returns a new `bitfield_flag` object with bits set where exactly one of the operands has a bit set.
- **Parameters**:
  - `lhs` (bitfield_flag const): The left-hand side operand.
  - `rhs` (bitfield_flag const): The right-hand side operand.
- **Return Value**:
  - A `bitfield_flag` object with bits set where exactly one of `lhs` or `rhs` has a bit set.
- **Exceptions/Errors**:
  - None. The operator is `noexcept` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag1;
bitfield_flag flag2;
bitfield_flag result = flag1 ^ flag2; // result has bits set where exactly one of flag1 and flag2 has a bit set
```
- **Preconditions**: Both `lhs` and `rhs` must be valid `bitfield_flag` objects.
- **Postconditions**: The returned `bitfield_flag` object will have bits set where exactly one of `lhs` or `rhs` has a bit set.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `operator|`, `operator&`, `operator~`, `all`

## bitfield_flag (operator~)

- **Signature**: `constexpr bitfield_flag operator~() const noexcept`
- **Description**: Bitwise NOT operator for `bitfield_flag` objects. Returns a new `bitfield_flag` object with all bits flipped (0 becomes 1, 1 becomes 0).
- **Parameters**: None.
- **Return Value**:
  - A `bitfield_flag` object with all bits flipped.
- **Exceptions/Errors**:
  - None. The operator is `constexpr` and does not throw exceptions.
- **Example**:
```cpp
bitfield_flag flag;
bitfield_flag result = ~flag; // result has all bits flipped
```
- **Preconditions**: The `bitfield_flag` object must be valid.
- **Postconditions**: The returned `bitfield_flag` object will have all bits flipped.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `operator|`, `operator&`, `operator^`, `all`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/flags.hpp"

int main() {
    // Create bitfield flags using different methods
    auto bit5 = 5_bit; // Using literal operator
    bitfield_flag flag1(bit5); // Using bit_t constructor
    bitfield_flag flag2(0x01); // Using explicit constructor
    bitfield_flag flag3; // Using default constructor (all bits cleared)
    
    // Combine flags using bitwise operations
    bitfield_flag combined = flag1 | flag2;
