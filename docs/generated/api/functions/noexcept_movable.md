# API Documentation for `aux_/noexcept_movable.hpp`

This file contains utility functions and types designed to facilitate move operations with guaranteed no-throw behavior, particularly for debugging and ensuring exception safety in the libtorrent library. The primary focus is on creating types that can be moved without throwing exceptions, even when the underlying type `T` might throw.

## `wrap`

- **Signature**: `T&& wrap(T&& v)`
- **Description**: This function serves as a wrapper that increments a global counter (`g_must_not_fail`) when a move operation occurs, ensuring that the operation is deemed "noexcept" for debugging purposes. It forwards the value as an rvalue reference, allowing the move constructor to proceed without exception.
- **Parameters**:
  - `v` (T&&): The rvalue reference to the object to be wrapped. This parameter must be a valid, non-null object of type `T` that can be moved.
- **Return Value**:
  - Returns an rvalue reference to the wrapped object (`T&&`). The returned value is the same as the input, but with the global counter incremented to indicate a successful move operation.
- **Exceptions/Errors**:
  - No exceptions are thrown by this function. It is designed to be noexcept.
- **Example**:
```cpp
int value = 42;
auto moved_value = wrap(std::move(value));
```
- **Preconditions**: The parameter `v` must be a valid object of type `T` that can be moved.
- **Postconditions**: The global counter `g_must_not_fail` is incremented by 1.
- **Thread Safety**: This function is not thread-safe due to the shared global variable `g_must_not_fail`.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable`, `noexcept_move_only`

## `noexcept_movable`

- **Signature**: `noexcept_movable() = default;`
- **Description**: Default constructor for the `noexcept_movable` class template. This constructor is declared as `= default`, meaning the compiler will generate a default constructor that performs no additional actions.
- **Parameters**: None
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
noexcept_movable<int> obj;
```
- **Preconditions**: None
- **Postconditions**: The object is default-constructed and ready for use.
- **Thread Safety**: Thread-safe if the default constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(T&& rhs)`, `noexcept_movable(noexcept_movable<T>&& rhs)`

## `noexcept_movable`

- **Signature**: `noexcept_movable(noexcept_movable<T>&& rhs) noexcept : T(std::forward<T>(wrap(rhs))) { --g_must_not_fail; }`
- **Description**: Move constructor for the `noexcept_movable` class template. This constructor takes an rvalue reference to another `noexcept_movable` object and initializes the current object by moving the underlying `T` object. It uses the `wrap` function to ensure the move is noexcept, and decrements the `g_must_not_fail` counter after the move.
- **Parameters**:
  - `rhs` (noexcept_movable<T>&&): An rvalue reference to the source object from which to move.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_movable<int> obj1;
noexcept_movable<int> obj2 = std::move(obj1);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`, and the `g_must_not_fail` counter is decremented.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(T&& rhs)`, `wrap`

## `noexcept_movable`

- **Signature**: `noexcept_movable(T&& rhs) noexcept : T(std::forward<T>(wrap(rhs))) // NOLINT { --g_must_not_fail; }`
- **Description**: Move constructor for the `noexcept_movable` class template that takes an rvalue reference to a `T` object directly. This constructor forwards the `T` object to the base class constructor, ensuring that the move is noexcept. It also decrements the `g_must_not_fail` counter after the move.
- **Parameters**:
  - `rhs` (T&&): An rvalue reference to the source `T` object to be moved.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_movable<int> obj1;
int value = 42;
noexcept_movable<int> obj2 = std::move(value);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`, and the `g_must_not_fail` counter is decremented.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(noexcept_movable<T>&& rhs)`, `wrap`

## `noexcept_movable`

- **Signature**: `noexcept_movable(noexcept_movable<T>&& rhs) noexcept : T(std::forward<T>(rhs)) {}`
- **Description**: Move constructor for the `noexcept_movable` class template that takes an rvalue reference to another `noexcept_movable` object and directly moves the `T` object without using the `wrap` function. This constructor assumes that the move is already noexcept.
- **Parameters**:
  - `rhs` (noexcept_movable<T>&&): An rvalue reference to the source object from which to move.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_movable<int> obj1;
noexcept_movable<int> obj2 = std::move(obj1);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(T&& rhs)`, `wrap`

## `noexcept_movable`

- **Signature**: `noexcept_movable(T&& rhs) noexcept : T(std::forward<T>(rhs)) {}`
- **Description**: Move constructor for the `noexcept_movable` class template that takes an rvalue reference to a `T` object directly and moves it without using the `wrap` function. This constructor assumes that the move is already noexcept.
- **Parameters**:
  - `rhs` (T&&): An rvalue reference to the source `T` object to be moved.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_movable<int> obj1;
int value = 42;
noexcept_movable<int> obj2 = std::move(value);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(noexcept_movable<T>&& rhs)`, `wrap`

## `noexcept_movable`

- **Signature**: `noexcept_movable(noexcept_movable<T> const& rhs) = default;`
- **Description**: Copy constructor for the `noexcept_movable` class template. This constructor is declared as `= default`, meaning the compiler will generate a default copy constructor that performs a shallow copy of the object.
- **Parameters**:
  - `rhs` (noexcept_movable<T> const&): A const reference to the source object from which to copy.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `= default` declaration.
- **Example**:
```cpp
noexcept_movable<int> obj1;
noexcept_movable<int> obj2 = obj1;
```
- **Preconditions**: The source object `rhs` must be valid and in a copy-able state.
- **Postconditions**: The current object contains a copy of the data from `rhs`.
- **Thread Safety**: Thread-safe if the copy constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(T const& rhs)`, `wrap`

## `noexcept_movable`

- **Signature**: `noexcept_movable(T const& rhs) : T(rhs) {}`
- **Description**: Copy constructor for the `noexcept_movable` class template that takes a const reference to a `T` object and copies it. This constructor forwards the `T` object to the base class constructor.
- **Parameters**:
  - `rhs` (T const&): A const reference to the source `T` object to be copied.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the constructor's implementation.
- **Example**:
```cpp
noexcept_movable<int> obj1;
int value = 42;
noexcept_movable<int> obj2 = obj1;
```
- **Preconditions**: The source object `rhs` must be valid and in a copy-able state.
- **Postconditions**: The current object contains a copy of the data from `rhs`.
- **Thread Safety**: Thread-safe if the copy constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_movable(noexcept_movable<T> const& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(noexcept_move_only<T>&& rhs) noexcept : T(std::forward<T>(wrap(rhs))) { --g_must_not_fail; }`
- **Description**: Move constructor for the `noexcept_move_only` class template. This constructor takes an rvalue reference to another `noexcept_move_only` object and initializes the current object by moving the underlying `T` object. It uses the `wrap` function to ensure the move is noexcept, and decrements the `g_must_not_fail` counter after the move.
- **Parameters**:
  - `rhs` (noexcept_move_only<T>&&): An rvalue reference to the source object from which to move.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
noexcept_move_only<int> obj2 = std::move(obj1);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`, and the `g_must_not_fail` counter is decremented.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_move_only(T&& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(T&& rhs) noexcept : T(std::forward<T>(wrap(rhs))) // NOLINT { --g_must_not_fail; }`
- **Description**: Move constructor for the `noexcept_move_only` class template that takes an rvalue reference to a `T` object directly. This constructor forwards the `T` object to the base class constructor, ensuring that the move is noexcept. It also decrements the `g_must_not_fail` counter after the move.
- **Parameters**:
  - `rhs` (T&&): An rvalue reference to the source `T` object to be moved.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
int value = 42;
noexcept_move_only<int> obj2 = std::move(value);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`, and the `g_must_not_fail` counter is decremented.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_move_only(noexcept_move_only<T>&& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(noexcept_move_only<T>&& rhs) noexcept : T(std::forward<T>(rhs)) {}`
- **Description**: Move constructor for the `noexcept_move_only` class template that takes an rvalue reference to another `noexcept_move_only` object and directly moves the `T` object without using the `wrap` function. This constructor assumes that the move is already noexcept.
- **Parameters**:
  - `rhs` (noexcept_move_only<T>&&): An rvalue reference to the source object from which to move.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
noexcept_move_only<int> obj2 = std::move(obj1);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_move_only(T&& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(T&& rhs) noexcept : T(std::forward<T>(rhs)) {}`
- **Description**: Move constructor for the `noexcept_move_only` class template that takes an rvalue reference to a `T` object directly and moves it without using the `wrap` function. This constructor assumes that the move is already noexcept.
- **Parameters**:
  - `rhs` (T&&): An rvalue reference to the source `T` object to be moved.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `noexcept` specifier.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
int value = 42;
noexcept_move_only<int> obj2 = std::move(value);
```
- **Preconditions**: The source object `rhs` must be valid and in a move-able state.
- **Postconditions**: The current object contains the moved data from `rhs`.
- **Thread Safety**: Thread-safe if the move constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_move_only(noexcept_move_only<T>&& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(noexcept_move_only<T> const& rhs) = default;`
- **Description**: Copy constructor for the `noexcept_move_only` class template. This constructor is declared as `= default`, meaning the compiler will generate a default copy constructor that performs a shallow copy of the object.
- **Parameters**:
  - `rhs` (noexcept_move_only<T> const&): A const reference to the source object from which to copy.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the `= default` declaration.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
noexcept_move_only<int> obj2 = obj1;
```
- **Preconditions**: The source object `rhs` must be valid and in a copy-able state.
- **Postconditions**: The current object contains a copy of the data from `rhs`.
- **Thread Safety**: Thread-safe if the copy constructor of `T` is thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `noexcept_move_only(T const& rhs)`, `wrap`

## `noexcept_move_only`

- **Signature**: `noexcept_move_only(T const& rhs) : T(rhs) {}`
- **Description**: Copy constructor for the `noexcept_move_only` class template that takes a const reference to a `T` object and copies it. This constructor forwards the `T` object to the base class constructor.
- **Parameters**:
  - `rhs` (T const&): A const reference to the source `T` object to be copied.
- **Return Value**: None (constructor does not return a value).
- **Exceptions/Errors**:
  - No exceptions are thrown due to the constructor's implementation.
- **Example**:
```cpp
noexcept_move_only<int> obj1;
int value = 42;
noexcept_move_only<int> obj2 = obj1;
``