# C++ Python Binding Utilities API Documentation

## allow_threading_guard

- **Signature**: `auto allow_threading_guard()`
- **Description**: RAII guard that saves the GIL (Global Interpreter Lock) state and restores it upon destruction. This allows the thread to release the GIL temporarily, enabling other Python threads to run while this guard is active. This is useful when calling blocking C++ functions that don't need to interact with Python.
- **Parameters**:
  - None
- **Return Value**:
  - An instance of `allow_threading_guard` that automatically restores the GIL state when destroyed.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
{
    allow_threading_guard guard;
    // Code here can run without holding the GIL
    // This is useful for blocking operations
}
// GIL is automatically restored when guard goes out of scope
```
- **Preconditions**: Must be called from a thread that has the GIL.
- **Postconditions**: The GIL state is restored when the guard goes out of scope.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## allow_threading_guard

- **Signature**: `auto ~allow_threading_guard()`
- **Description**: Destructor for the `allow_threading_guard` class that restores the saved GIL state. This ensures that the GIL is properly restored when the guard goes out of scope, even if an exception is thrown.
- **Parameters**:
  - None
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
{
    allow_threading_guard guard;  // GIL is saved here
    // ... perform operations that don't need the GIL
} // GIL is automatically restored here
```
- **Preconditions**: The guard must have been constructed with a valid saved GIL state.
- **Postconditions**: The GIL state is restored to what it was when the guard was constructed.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## lock_gil

- **Signature**: `auto lock_gil()`
- **Description**: RAII guard that ensures the GIL is held during the lifetime of the object. This is useful when calling Python C API functions that require the GIL to be held.
- **Parameters**:
  - None
- **Return Value**:
  - An instance of `lock_gil` that automatically releases the GIL when destroyed.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
{
    lock_gil gil;
    // Code here runs with the GIL held
    // This is necessary when calling Python C API functions
}
// GIL is automatically released when gil goes out of scope
```
- **Preconditions**: Must be called from a thread that has the GIL.
- **Postconditions**: The GIL is released when the object goes out of scope.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## lock_gil

- **Signature**: `auto ~lock_gil()`
- **Description**: Destructor for the `lock_gil` class that releases the GIL. This ensures that the GIL is properly released when the guard goes out of scope, even if an exception is thrown.
- **Parameters**:
  - None
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
{
    lock_gil gil;  // GIL is acquired here
    // ... perform operations that need the GIL
} // GIL is automatically released here
```
- **Preconditions**: The guard must have been constructed with a valid GIL state.
- **Postconditions**: The GIL is released to what it was before the guard was constructed.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## allow_threading

- **Signature**: `auto allow_threading(F fn)`
- **Description**: Creates a callable object that allows threading by releasing the GIL before invoking the provided function. This is useful for wrapping C++ functions that may block and don't need to interact with Python.
- **Parameters**:
  - `fn`: The function to call, which will be executed with the GIL released.
- **Return Value**:
  - A callable object that can be invoked with the same arguments as the original function.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto threaded_func = allow_threading([](int x) { return x * x; });
int result = threaded_func(5); // GIL is released during the call
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is executed with the GIL released, and the GIL is restored when the function returns.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## operator()

- **Signature**: `auto operator()(Self&& s, Args&&... args)`
- **Description**: Overloaded operator() for the `allow_threading` class that executes the wrapped function with the GIL released. This allows the function to run without holding the GIL, enabling other Python threads to run concurrently.
- **Parameters**:
  - `s`: The object to call the function on (if it's a member function).
  - `args`: The arguments to pass to the function.
- **Return Value**:
  - The return value of the function call.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto threaded_func = allow_threading([](int x) { return x * x; });
int result = threaded_func(5); // GIL is released during the call
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is executed with the GIL released, and the GIL is restored when the function returns.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## visitor

- **Signature**: `auto visitor(F fn)`
- **Description**: Creates a visitor object that can be used to register a function with a Python class. This is used in the context of the Boost.Python library to register C++ functions with Python.
- **Parameters**:
  - `fn`: The function to register.
- **Return Value**:
  - A visitor object that can be used to register the function with a Python class.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = visitor([](int x) { return x * x; });
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## visit_aux

- **Signature**: `auto visit_aux(Class& cl, char const* name, Options const& options, Signature const& signature)`
- **Description**: Internal function used to register a function with a Python class. This function is typically called by the `visit` function to register the function with the Python class.
- **Parameters**:
  - `cl`: The Python class to register the function with.
  - `name`: The name of the function in Python.
  - `options`: Options for the function registration.
  - `signature`: The signature of the function.
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = visitor([](int x) { return x * x; });
visitor.visit_aux(cl, "name", options, signature);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## visit

- **Signature**: `auto visit(Class& cl, char const* name, Options const& options)`
- **Description**: Registers a function with a Python class. This function is used to register a C++ function with a Python class so that it can be called from Python.
- **Parameters**:
  - `cl`: The Python class to register the function with.
  - `name`: The name of the function in Python.
  - `options`: Options for the function registration.
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = visitor([](int x) { return x * x; });
visitor.visit(cl, "name", options);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## allow_threads

- **Signature**: `auto allow_threads(F fn)`
- **Description**: Creates a visitor object that allows threading by releasing the GIL before invoking the provided function. This is useful for wrapping C++ functions that may block and don't need to interact with Python.
- **Parameters**:
  - `fn`: The function to call, which will be executed with the GIL released.
- **Return Value**:
  - A visitor object that can be used to register the function with a Python class.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = allow_threads([](int x) { return x * x; });
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## invoke

- **Signature**: `auto invoke(Fn&& fn, Self&& s) -> decltype(auto)`
- **Description**: Invokes a function with the provided arguments. This function is used to call C++ functions from Python code, with special handling for different return types based on the `TORRENT_AUTO_RETURN_TYPES` macro.
- **Parameters**:
  - `fn`: The function to invoke.
  - `s`: The object to call the function on (if it's a member function).
- **Return Value**:
  - The return value of the function call.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto result = invoke([](int x) { return x * x; }, 5);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is executed with the GIL released, and the GIL is restored when the function returns.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## invoke

- **Signature**: `auto invoke(Fn&& fn, Args&&... args) -> decltype(auto)`
- **Description**: Invokes a function with the provided arguments. This function is used to call C++ functions from Python code, with special handling for different return types based on the `TORRENT_AUTO_RETURN_TYPES` macro.
- **Parameters**:
  - `fn`: The function to invoke.
  - `args`: The arguments to pass to the function.
- **Return Value**:
  - The return value of the function call.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto result = invoke([](int x, int y) { return x + y; }, 5, 3);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is executed with the GIL released, and the GIL is restored when the function returns.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## deprecated_fun

- **Signature**: `auto deprecated_fun(F fn, char const* name)`
- **Description**: Creates a deprecated function wrapper that issues a deprecation warning when called. This is used to mark functions as deprecated and provide a warning to users.
- **Parameters**:
  - `fn`: The function to wrap.
  - `name`: The name of the function, used in the deprecation message.
- **Return Value**:
  - A callable object that can be used to call the deprecated function.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto deprecated_func = deprecated_fun([](int x) { return x * x; }, "old_function");
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## operator()

- **Signature**: `auto operator()(Args&&... args) -> R`
- **Description**: Overloaded operator() for the `deprecated_fun` class that calls the wrapped function and issues a deprecation warning. This allows the function to be called as if it were the original function, but with a warning.
- **Parameters**:
  - `args`: The arguments to pass to the function.
- **Return Value**:
  - The return value of the function call.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto deprecated_func = deprecated_fun([](int x) { return x * x; }, "old_function");
int result = deprecated_func(5); // Deprecation warning is issued
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is executed with the GIL released, and the GIL is restored when the function returns.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## deprecate_visitor

- **Signature**: `auto deprecate_visitor(F fn)`
- **Description**: Creates a visitor object that marks a function as deprecated. This is used to register deprecated functions with a Python class.
- **Parameters**:
  - `fn`: The function to mark as deprecated.
- **Return Value**:
  - A visitor object that can be used to register the function with a Python class.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = deprecate_visitor([](int x) { return x * x; });
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## visit_aux

- **Signature**: `auto visit_aux(Class& cl, char const* name, Options const& options, Signature const& signature)`
- **Description**: Internal function used to register a deprecated function with a Python class. This function is typically called by the `visit` function to register the function with the Python class.
- **Parameters**:
  - `cl`: The Python class to register the function with.
  - `name`: The name of the function in Python.
  - `options`: Options for the function registration.
  - `signature`: The signature of the function.
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = deprecate_visitor([](int x) { return x * x; });
visitor.visit_aux(cl, "name", options, signature);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## visit

- **Signature**: `auto visit(Class& cl, char const* name, Options const& options)`
- **Description**: Registers a deprecated function with a Python class. This function is used to register a C++ function with a Python class so that it can be called from Python, with a deprecation warning.
- **Parameters**:
  - `cl`: The Python class to register the function with.
  - `name`: The name of the function in Python.
  - `options`: Options for the function registration.
- **Return Value**:
  - None
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = deprecate_visitor([](int x) { return x * x; });
visitor.visit(cl, "name", options);
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

## depr

- **Signature**: `auto depr(F fn)`
- **Description**: Creates a visitor object that marks a function as deprecated. This is used to register deprecated functions with a Python class.
- **Parameters**:
  - `fn`: The function to mark as deprecated.
- **Return Value**:
  - A visitor object that can be used to register the function with a Python class.
- **Exceptions/Errors**:
  - No exceptions thrown under normal conditions.
- **Example**:
```cpp
auto visitor = depr([](int x) { return x * x; });
```
- **Preconditions**: The function must be safe to call without the GIL.
- **Postconditions**: The function is registered with the Python class.
- **Thread Safety**: Thread-safe when used correctly.
- **Complexity**: O(1) time and space complexity.

# Usage Examples

## Basic Usage

```