# API Documentation for `unique_ptr` Functions

## Function: `unique_ptr` (Default Constructor)

- **Signature**: `auto unique_ptr()`
- **Description**: Default constructor for the `unique_ptr` class template. Creates a `unique_ptr` instance that owns no resource. The pointer is initialized to `nullptr`.
- **Parameters**: None
- **Return Value**: 
  - Returns a `unique_ptr<T>` instance that owns no resource (i.e., the internal pointer is `nullptr`).
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
auto ptr = unique_ptr<int>();
if (!ptr) {
    // ptr is nullptr, no resource is owned
}
```
- **Preconditions**: None
- **Postconditions**: The `unique_ptr` instance is valid and owns no resource.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: `unique_ptr(T* arr)` (constructor with pointer), `operator[]`

---

## Function: `unique_ptr` (Constructor with Pointer)

- **Signature**: `auto unique_ptr(T* arr)`
- **Description**: Constructor that takes a raw pointer and transfers ownership to the `unique_ptr`. The `unique_ptr` will manage the lifetime of the pointed-to object and delete it when the `unique_ptr` is destroyed. This constructor is explicit to prevent accidental conversions from raw pointers.
- **Parameters**:
  - `arr` (T*): Raw pointer to an object or array to be owned by the `unique_ptr`. Must be a valid pointer or `nullptr`. Passing a dangling pointer results in undefined behavior.
- **Return Value**: 
  - Returns a `unique_ptr<T>` instance that owns the provided pointer.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
auto ptr = unique_ptr<int>(new int(42));
*ptr = 100; // Modify the owned object
// ptr will automatically delete the int when it goes out of scope
```
- **Preconditions**: `arr` must be a valid pointer or `nullptr`.
- **Postconditions**: The `unique_ptr` now owns the resource pointed to by `arr`, and the caller must not delete the resource manually.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: `unique_ptr()` (default constructor), `operator[]`

---

## Function: `operator[]`

- **Signature**: `auto decltype(auto) operator[](IndexType idx) const`
- **Description**: Overloaded subscript operator that allows access to elements in the `unique_ptr`-managed array. This function is marked as `const` and returns a reference to the element at the specified index.
- **Parameters**:
  - `idx` (IndexType): Index of the element to access. Must be non-negative. If the index is out of bounds, the behavior is undefined.
- **Return Value**: 
  - Returns a reference to the element at `idx`. The return type is `decltype(auto)` to preserve the exact type of the element (e.g., `T&` or `const T&`).
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - **Note**: This function uses `TORRENT_ASSERT(idx >= IndexType(0))` to check that the index is non-negative. If the assertion fails, it will trigger a debug assertion in debug builds.
- **Example**:
```cpp
auto ptr = unique_ptr<int[]>(new int[5]{1, 2, 3, 4, 5});
int value = ptr[2]; // Access the third element (3)
ptr[4] = 10;       // Modify the fifth element
```
- **Preconditions**: `idx` must be a valid index (i.e., `idx >= 0` and `idx < size of array`).
- **Postconditions**: The element at `idx` is accessed and returned. The `unique_ptr` maintains ownership of the array.
- **Thread Safety**: Thread-safe for concurrent reads, but writes to the same element may cause data races.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: `unique_ptr()`, `unique_ptr(T* arr)`

---

## Usage Examples

### 1. Basic Usage

```cpp
#include "libtorrent/aux_/unique_ptr.hpp"
#include <iostream>

int main() {
    // Create a unique_ptr owning an array of integers
    auto arr = unique_ptr<int[]>(new int[3]{1, 2, 3});

    // Access elements using operator[]
    for (int i = 0; i < 3; ++i) {
        std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
    }

    // Modify an element
    arr[1] = 42;

    return 0;
}
```

### 2. Error Handling

```cpp
#include "libtorrent/aux_/unique_ptr.hpp"
#include <iostream>
#include <cassert>

int main() {
    // Safe usage with assertions
    auto arr = unique_ptr<int[]>(new int[5]);

    // Access valid indices
    for (int i = 0; i < 5; ++i) {
        arr[i] = i * 10;
    }

    // This will trigger an assertion in debug builds
    // arr[10] = 100; // Uncommenting this will cause a debug assertion

    return 0;
}
```

### 3. Edge Cases

```cpp
#include "libtorrent/aux_/unique_ptr.hpp"
#include <iostream>

int main() {
    // Create a unique_ptr with null pointer (no resource)
    auto null_ptr = unique_ptr<int>();

    // Accessing a null pointer will trigger undefined behavior
    // This is unsafe and should be avoided
    // std::cout << null_ptr[0] << std::endl;

    // Create a unique_ptr with a single element
    auto single = unique_ptr<int[]>(new int[1]{42});

    // Access the only element
    std::cout << "single[0] = " << single[0] << std::endl;

    return 0;
}
```

---

## Best Practices

- **Use `unique_ptr` for automatic memory management**: Always use `unique_ptr` to manage dynamically allocated arrays to avoid memory leaks.
- **Avoid raw pointers**: Never manually delete the resource managed by a `unique_ptr`.
- **Use `make_unique` when possible**: Prefer `std::make_unique` for creating `unique_ptr` instances, though this specific implementation may not support it.
- **Check for null pointers**: Use `nullptr` checks before dereferencing or accessing elements.
- **Avoid out-of-bounds access**: Ensure indices are within valid bounds to prevent undefined behavior.

---

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `unique_ptr()`  
**Issue**: No documentation about the class template parameters or ownership semantics.  
**Severity**: Medium  
**Impact**: Users may not understand the template nature of the class or how ownership works.  
**Fix**: Add template parameter documentation and clarify ownership semantics in the header.

---

**Function**: `unique_ptr(T* arr)`  
**Issue**: The constructor is not marked `explicit` if `T` is a pointer type, which could lead to accidental conversions.  
**Severity**: Low  
**Impact**: Potential for unintended implicit conversions.  
**Fix**: Ensure the constructor is explicitly marked `explicit` if it's not already.

---

**Function**: `operator[]`  
**Issue**: Uses `TORRENT_ASSERT` for bounds checking, which only triggers in debug builds. This can lead to undefined behavior in release builds.  
**Severity**: High  
**Impact**: Accessing out-of-bounds indices can cause crashes or data corruption.  
**Fix**: Add runtime bounds checking in release builds or use `std::vector` for safer array access.

---

### Modernization Opportunities

- **Use `[[nodiscard]]`**: Mark the `operator[]` function as `[[nodiscard]]` to prevent discarding the result, which could lead to logic errors.
  ```cpp
  [[nodiscard]] decltype(auto) operator[](IndexType idx) const;
  ```
- **Use `std::span`**: Replace raw array access with `std::span` for safer and more expressive code.
  ```cpp
  std::span<T> as_span() const;
  ```
- **Use `constexpr`**: If the `unique_ptr` is used in compile-time contexts, consider making relevant operations `constexpr`.

---

### Refactoring Suggestions

- **Split `unique_ptr` into `unique_ptr<T>` and `unique_ptr<T[]>`**: Separate the class into specialized versions for single objects and arrays to improve clarity and safety.
- **Move to utility namespace**: Consider moving the `unique_ptr` class to a utility namespace like `libtorrent::util` for better organization.

---

### Performance Optimizations

- **Use move semantics**: Ensure the `unique_ptr` supports move semantics for efficient transfers.
- **Return by value**: Use `std::move` when transferring ownership to avoid unnecessary copies.
- **Add `noexcept`**: Mark the constructor and destructor as `noexcept` if they don't throw exceptions.
  ```cpp
  unique_ptr() noexcept = default;
  explicit unique_ptr(T* arr) noexcept : base(arr) {}
  ```