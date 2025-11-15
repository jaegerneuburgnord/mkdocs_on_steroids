# API Documentation for `scope_end` Utility Functions

## Function: `scope_end_impl`

- **Signature**: `scope_end_impl(Fun f)`
- **Description**: Constructs a scope-end handler that will execute the provided function `f` when the scope-end object goes out of scope. This is a helper class that implements the RAII (Resource Acquisition Is Initialization) pattern for cleanup operations.
- **Parameters**:
  - `f` (Fun): A callable object (function, lambda, functor) that will be executed when the scope-end object is destroyed. The callable must be movable and callable with no arguments.
- **Return Value**:
  - Returns an instance of `scope_end_impl<Fun>` that will execute the provided function when it goes out of scope.
  - The returned object is used as a local variable in a scope, and its destruction triggers the execution of the function.
- **Exceptions/Errors**:
  - Throws if the provided function `f` cannot be moved (if it's not movable).
  - Throws if `f()` throws during destruction (this is the expected behavior when the function itself throws).
- **Example**:
```cpp
{
    auto cleanup = scope_end_impl([]() { 
        std::cout << "Cleanup executed" << std::endl; 
    });
    // ... do work ...
    // Cleanup will be automatically called when cleanup goes out of scope
}
```
- **Preconditions**: The function `f` must be movable and callable with no arguments.
- **Postconditions**: The function `f` will be executed exactly once when the `scope_end_impl` object is destroyed, unless `disarm()` is called first.
- **Thread Safety**: The class itself is not thread-safe. Multiple threads should not access the same `scope_end_impl` instance concurrently.
- **Complexity**: O(1) time and space complexity for construction.
- **See Also**: `scope_end()`, `disarm()`

## Function: `scope_end_impl`

- **Signature**: `~scope_end_impl()`
- **Description**: Destructor that executes the stored function `m_fun()` if `m_armed` is true. This is the core of the RAII pattern - the function is called when the object goes out of scope.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**:
  - May throw if the stored function `m_fun()` throws.
  - The exception will propagate to the caller of the destructor.
- **Example**:
```cpp
{
    auto cleanup = scope_end_impl([]() { 
        std::cout << "Cleanup executed" << std::endl; 
    });
    // When cleanup goes out of scope, the lambda will be executed
}
```
- **Preconditions**: None.
- **Postconditions**: If `m_armed` is true, the stored function `m_fun()` will be executed exactly once.
- **Thread Safety**: The destructor may be called from any thread, but the stored function should be thread-safe if called from multiple threads.
- **Complexity**: O(1) time complexity, depends on the cost of executing the stored function.
- **See Also**: `scope_end_impl(Fun f)`, `disarm()`

## Function: `scope_end_impl`

- **Signature**: `scope_end_impl(scope_end_impl&&) noexcept = default;`
- **Description**: Move constructor that allows the scope-end object to be moved from one scope to another. This is essential for the RAII pattern when objects need to be passed between functions.
- **Parameters**: 
  - `other` (scope_end_impl&&): The source object to move from. The source object will be in a valid but unspecified state after the move.
- **Return Value**: None.
- **Exceptions/Errors**: Never throws, as specified by `noexcept`.
- **Example**:
```cpp
auto create_cleanup() {
    return scope_end_impl([]() { 
        std::cout << "Cleanup executed" << std::endl; 
    });
}

{
    auto cleanup = create_cleanup(); // Move constructor called
    // cleanup will execute when it goes out of scope
}
```
- **Preconditions**: The source object must be in a valid state.
- **Postconditions**: The target object will contain the same function as the source, and the source will be in a valid but unspecified state.
- **Thread Safety**: The move constructor is thread-safe as long as the function being moved is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `scope_end_impl(Fun f)`, `disarm()`

## Function: `scope_end_impl`

- **Signature**: `scope_end_impl(scope_end_impl const&) = delete;`
- **Description**: Deleted copy constructor to prevent copying of the scope-end object. This is intentional to enforce move semantics and prevent accidental copying, which could lead to double-execution of the cleanup function.
- **Parameters**: 
  - `other` (const scope_end_impl&): The source object to copy from.
- **Return Value**: None.
- **Exceptions/Errors**: Compilation error if attempted to copy.
- **Example**:
```cpp
// This will cause a compilation error:
// auto cleanup1 = scope_end_impl([]() { std::cout << "Cleanup" << std::endl; });
// auto cleanup2 = cleanup1; // Error: copy constructor is deleted
```
- **Preconditions**: None (but the copy is not allowed).
- **Postconditions**: None (copy is not allowed).
- **Thread Safety**: Not applicable, as copying is not allowed.
- **Complexity**: N/A.
- **See Also**: `scope_end_impl(scope_end_impl&&)`, `scope_end()`

## Function: `disarm`

- **Signature**: `void disarm()`
- **Description**: Disarms the scope-end handler by setting `m_armed` to false, preventing the stored function from being executed when the object goes out of scope. This is useful when you want to conditionally execute or skip the cleanup.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: None.
- **Example**:
```cpp
{
    auto cleanup = scope_end_impl([]() { 
        std::cout << "Cleanup executed" << std::endl; 
    });
    
    if (some_condition) {
        cleanup.disarm(); // Prevent cleanup from executing
    }
    // If some_condition is true, cleanup will NOT execute
}
```
- **Preconditions**: The function must be called on a valid `scope_end_impl` object.
- **Postconditions**: The stored function will not be executed when the object goes out of scope.
- **Thread Safety**: The function is thread-safe if the cleanup function is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `scope_end_impl()`, `scope_end()`

## Function: `scope_end`

- **Signature**: `scope_end_impl<Fun> scope_end(Fun f)`
- **Description**: Creates a `scope_end_impl` object with the provided function, enabling the RAII pattern for cleanup operations. This is the primary factory function for creating scope-end handlers.
- **Parameters**:
  - `f` (Fun): A callable object (function, lambda, functor) that will be executed when the scope-end object goes out of scope. The callable must be movable and callable with no arguments.
- **Return Value**: Returns a `scope_end_impl<Fun>` object that will execute the provided function when it goes out of scope.
- **Exceptions/Errors**: 
  - Throws if the provided function `f` cannot be moved (if it's not movable).
- **Example**:
```cpp
{
    auto cleanup = scope_end([]() { 
        std::cout << "Cleanup executed" << std::endl; 
    });
    // ... do work ...
    // Cleanup will be automatically called when cleanup goes out of scope
}
```
- **Preconditions**: The function `f` must be movable and callable with no arguments.
- **Postconditions**: A `scope_end_impl` object is created that will execute the provided function when it goes out of scope.
- **Thread Safety**: The function is thread-safe as long as the provided function is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `scope_end_impl()`, `disarm()`

# Usage Examples

## 1. Basic Usage

```cpp
#include <iostream>
#include <vector>

// Example: Using scope_end to ensure cleanup of a file handle
void process_with_cleanup() {
    FILE* file = fopen("test.txt", "w");
    if (!file) {
        std::cerr << "Failed to open file" << std::endl;
        return;
    }
    
    // Create a scope-end handler to close the file when we leave the scope
    auto cleanup = scope_end([file]() { 
        fclose(file); 
        std::cout << "File closed" << std::endl; 
    });
    
    // ... do work with the file ...
    fprintf(file, "Hello, World!");
    
    // The file will be automatically closed when cleanup goes out of scope
}

// Example: Using scope_end to manage a mutex lock
void process_with_lock() {
    std::mutex mtx;
    std::unique_lock<std::mutex> lock(mtx);
    
    // Create a scope-end handler to release the lock
    auto unlock = scope_end([lock = std::move(lock)]() { 
        // The lock will be released when this function is called
    });
    
    // ... do work with the lock ...
    std::cout << "Working with locked resource" << std::endl;
    
    // The lock will be automatically released when unlock goes out of scope
}
```

## 2. Error Handling

```cpp
#include <iostream>
#include <stdexcept>
#include <memory>

// Example: Using scope_end with error handling
void process_with_error_handling() {
    // Create a scope-end handler for cleanup
    auto cleanup = scope_end([]() { 
        std::cout << "Cleanup: Resources released" << std::endl; 
    });
    
    try {
        // Simulate some work that might fail
        std::unique_ptr<int> resource(new int(42));
        
        if (some_condition) {
            throw std::runtime_error("Something went wrong");
        }
        
        // If we get here, work succeeded
        std::cout << "Work succeeded" << std::endl;
        
        // The cleanup will be executed even if an exception is thrown
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        // The cleanup will still execute due to RAII
        throw; // Re-throw the exception
    }
}
```

## 3. Edge Cases

```cpp
#include <iostream>
#include <vector>
#include <memory>

// Example: Using scope_end with temporary objects and complex scenarios
void complex_scenarios() {
    // Edge case 1: Disarming the cleanup
    auto cleanup = scope_end([]() { 
        std::cout << "Cleanup: This should not execute" << std::endl; 
    });
    
    cleanup.disarm(); // Prevent execution of cleanup
    // The cleanup will not be executed when cleanup goes out of scope
    
    // Edge case 2: Moving the cleanup object
    auto cleanup2 = scope_end([]() { 
        std::cout << "Cleanup: This will execute" << std::endl; 
    });
    
    auto cleanup3 = std::move(cleanup2); // Move the cleanup object
    // cleanup2 is now in a valid but unspecified state
    // cleanup3 will execute the cleanup when it goes out of scope
    
    // Edge case 3: Multiple cleanup objects in the same scope
    auto cleanup4 = scope_end([]() { 
        std::cout << "Cleanup 1" << std::endl; 
    });
    
    auto cleanup5 = scope_end([]() { 
        std::cout << "Cleanup 2" << std::endl; 
    });
    
    // Both cleanup objects will execute their functions when they go out of scope
}
```

# Best Practices

## How to Use These Functions Effectively

1. **Use `scope_end` to implement RAII patterns**: Always use `scope_end` to manage resources that need to be cleaned up when exiting a scope, such as file handles, mutex locks, or memory allocations.

2. **Capture variables by reference when needed**: When your cleanup function needs to access variables from the current scope, capture them by reference in the lambda to avoid dangling references.

3. **Use `disarm()` to conditionally skip cleanup**: Use `disarm()` when you want to prevent the cleanup function from executing under certain conditions (e.g., when a critical error occurs).

4. **Avoid storing `scope_end` objects in classes**: If you need to manage resources that span multiple function calls, consider using a class with proper RAII semantics rather than storing `scope_end` objects.

5. **Use `std::move` to transfer ownership**: When passing a `scope_end` object to another function, use `std::move` to transfer ownership and avoid copying.

## Common Mistakes to Avoid

1. **Copying `scope_end` objects**: Never copy a `scope_end` object because the copy constructor is deleted. Use `std::move` instead.

2. **Forgetting to disarm**: If you want to prevent cleanup from executing, remember to call `disarm()` before the object goes out of scope.

3. **Using the object after moving**: After moving a `scope_end` object, the source object is in a valid but unspecified state. Do not use it after moving.

4. **Not handling exceptions properly**: Remember that `scope_end` objects will execute their cleanup functions even if an exception is thrown, so make sure your cleanup code is exception-safe.

## Performance Tips

1. **Use `std::move` to avoid unnecessary copies**: When passing a `scope_end` object, use `std::move` to avoid copying the object.

2. **Minimize the cost of the cleanup function**: Keep the cleanup function as lightweight as possible to avoid performance overhead.

3. **Consider the scope of the cleanup**: Only use `scope_end` for cleanup operations that are relevant to the current scope. For longer-lived resources, consider other RAII patterns.

# Code Review & Improvement Suggestions

## Function: `scope_end_impl(Fun f)`

- **Issue**: No explicit documentation of the `Fun` template parameter
- **Severity**: Low
- **Impact**: Users may not know what kind of function types are supported
- **Fix**: Add documentation for the `Fun` template parameter in the function signature and description

## Function: `scope_end_impl()`

- **Issue**: No documentation for the destructor's behavior
- **Severity**: Low
- **Impact**: Users may not understand when the cleanup function is executed
- **Fix**: Add documentation explaining that the destructor executes the stored function when the object goes out of scope

## Function: `scope_end_impl(scope_end_impl&&)`

- **Issue**: No documentation for move semantics
- **Severity**: Low
- **Impact**: Users may not understand the behavior of moving the object
- **Fix**: Add documentation explaining that this function allows the object to be moved from one scope to another

## Function: `scope_end_impl(scope_end_impl const&)`

- **Issue**: No documentation for the deleted copy constructor
- **Severity**: Low
- **Impact**: Users may not understand why copying is not allowed
- **Fix**: Add documentation explaining that copying is intentionally prevented to avoid double-execution of cleanup functions

## Function: `disarm()`

- **Issue**: No documentation for the `m_armed` member variable
- **Severity**: Low
- **Impact**: Users may not understand the internal state of the object
- **Fix**: Add documentation explaining the role of the `m_armed` variable in controlling cleanup execution

## Function: `scope_end()`

- **Issue**: No documentation for the return type
- **Severity**: Low
- **Impact**: Users may not understand the type of object returned
- **Fix**: Add documentation explaining that the function returns a `scope_end_impl<Fun>` object

# Modernization Opportunities

1. **Use `[[nodiscard]]` for functions that return important values**:
```cpp
[[nodiscard]] scope_end_impl<Fun> scope_end(Fun f);
```

2. **Use `std::move` for better performance**:
The code already uses `std::move` appropriately, which is good.

3. **Use `constexpr` where possible**:
The functions cannot be `constexpr` because they involve non-constant operations like function calls and memory management.

4. **Use concepts (C++20) for template constraints**:
```cpp
template <typename Fun>
requires std::invocable<Fun>
scope_end_impl<Fun> scope_end(Fun f) {
    return scope_end_impl<Fun>(std::move(f));
}
```

5. **Use `std::expected` (C++23) for error handling**:
Not applicable here since these functions don't return error values.

# Refactoring Suggestions

1. **Split into smaller functions**: The functions are already appropriately small and focused.

2. **Combine with similar functions**: No similar functions need to be combined.

3. **Make into class methods**: The functions are already in a logical structure.

4. **Move to a utility namespace**: The `aux_` namespace is appropriate for internal utility functions.

# Performance Optimizations

1. **Use move semantics**: The code already uses move semantics appropriately.

2. **Return by value for RVO**: The functions return by value, which allows for Return Value Optimization.

3. **Use string_view for read-only strings**: Not applicable here as the functions don't handle strings.

4. **Add `noexcept` where applicable**: The move constructor and destructor should be marked as `noexcept` since they don't throw exceptions.

```cpp
// Add noexcept to the move constructor
scope_end_impl(scope_end_impl&&) noexcept = default;

// Add noexcept to the destructor
~scope_end_impl() noexcept { if (m_armed) m_fun(); }
```