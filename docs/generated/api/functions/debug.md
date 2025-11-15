# libtorrent Debug API Documentation

## async_t

- **Signature**: `async_t()`
- **Description**: Default constructor for the `async_t` structure, which tracks the number of outstanding asynchronous operations and their call stacks.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
async_t async_instance;
```
- **Preconditions**: None
- **Postconditions**: The `async_t` instance is initialized with `refs` set to 0.
- **Thread Safety**: Not thread-safe (constructor is not synchronized)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `add_outstanding_async`, `complete_async`

## has_outstanding_async

- **Signature**: `bool has_outstanding_async(char const* name)`
- **Description**: Checks if there are any outstanding asynchronous operations with the specified name.
- **Parameters**:
  - `name` (char const*): The name of the asynchronous operation to check
- **Return Value**: 
  - `true` if there are outstanding operations with the given name
  - `false` if no outstanding operations with the given name
- **Exceptions/Errors**: None
- **Example**:
```cpp
if (has_outstanding_async("download")) {
    std::cout << "There are outstanding download operations" << std::endl;
}
```
- **Preconditions**: The function name must be a valid C-string.
- **Postconditions**: Returns the status of outstanding operations for the specified name.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(log n) time (map lookup), O(1) space
- **See Also**: `add_outstanding_async`, `complete_async`

## add_outstanding_async

- **Signature**: `void add_outstanding_async(char const* name)`
- **Description**: Registers an outstanding asynchronous operation with the given name and captures the current call stack.
- **Parameters**:
  - `name` (char const*): The name of the asynchronous operation
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
add_outstanding_async("upload");
// Operation is now tracked
```
- **Preconditions**: The function name must be a valid C-string.
- **Postconditions**: The operation is registered as outstanding with its call stack captured.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(log n) time (map insertion), O(1) space
- **See Also**: `has_outstanding_async`, `complete_async`

## complete_async

- **Signature**: `void complete_async(char const* name)`
- **Description**: Marks an asynchronous operation as complete, decrementing its reference count and recording the completion in the wakeups queue.
- **Parameters**:
  - `name` (char const*): The name of the asynchronous operation to complete
- **Return Value**: None
- **Exceptions/Errors**: 
  - `TORRENT_ASSERT` may trigger if `refs` is <= 0
- **Example**:
```cpp
complete_async("download");
// Operation is marked as complete
```
- **Preconditions**: The operation must be registered as outstanding.
- **Postconditions**: The operation's reference count is decremented, and the completion is recorded.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(log n) time (map lookup), O(1) space
- **See Also**: `add_outstanding_async`, `has_outstanding_async`

## async_inc_threads

- **Signature**: `void async_inc_threads()`
- **Description**: Increments the counter for the number of active asynchronous operations threads.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
async_inc_threads();
// Number of active threads is incremented
```
- **Preconditions**: None
- **Postconditions**: The `_async_ops_nthreads` counter is incremented by 1.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `async_dec_threads`

## async_dec_threads

- **Signature**: `void async_dec_threads()`
- **Description**: Decrements the counter for the number of active asynchronous operations threads.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
async_dec_threads();
// Number of active threads is decremented
```
- **Preconditions**: None
- **Postconditions**: The `_async_ops_nthreads` counter is decremented by 1.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `async_inc_threads`

## log_async

- **Signature**: `int log_async()`
- **Description**: Logs information about outstanding asynchronous operations that have more references than the number of active threads minus one.
- **Parameters**: None
- **Return Value**: 
  - The total number of outstanding references across all operations that meet the condition
- **Exceptions/Errors**: None
- **Example**:
```cpp
int outstanding_refs = log_async();
if (outstanding_refs > 0) {
    std::cout << "There are " << outstanding_refs << " outstanding references" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: Logs information about outstanding operations and returns the total count of references.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(n) time (iterating through operations), O(1) space
- **See Also**: `has_outstanding_async`, `add_outstanding_async`

## log_handler_allocators

- **Signature**: `void log_handler_allocators() noexcept`
- **Description**: Logs information about handler allocators, including their types and memory usage.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
log_handler_allocators();
// Handler allocator information is logged
```
- **Preconditions**: The function must be called in a context where the handler storage mutex is accessible.
- **Postconditions**: Information about handler allocators is logged to the output.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(n) time (iterating through handlers), O(1) space
- **See Also**: `record_handler_allocation`

## record_handler_allocation

- **Signature**: `void record_handler_allocation(int const type, std::size_t const capacity)`
- **Description**: Records the allocation of a handler with the specified type and capacity.
- **Parameters**:
  - `type` (int const): The type of handler being allocated
  - `capacity` (std::size_t const): The capacity of the handler allocation
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
record_handler_allocation(0, 1024);
// Handler allocation is recorded
```
- **Preconditions**: The type must be a valid handler type.
- **Postconditions**: The handler allocation is recorded in the handler storage.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `log_handler_allocators`

## single_threaded

- **Signature**: `single_threaded()`
- **Description**: Default constructor for the `single_threaded` structure, which tracks whether a thread is running in a single-threaded context.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
single_threaded s;
// single_threaded instance is created
```
- **Preconditions**: None
- **Postconditions**: The `single_threaded` instance is initialized with `m_id` set to the default thread ID.
- **Thread Safety**: Not thread-safe (constructor is not synchronized)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `is_single_thread`, `is_not_thread`

## is_single_thread

- **Signature**: `bool is_single_thread() const`
- **Description**: Checks if the current thread is the same as the thread that created the `single_threaded` instance.
- **Parameters**: None
- **Return Value**: 
  - `true` if the current thread is the same as the stored thread ID
  - `false` otherwise
- **Exceptions/Errors**: None
- **Example**:
```cpp
single_threaded s;
if (s.is_single_thread()) {
    std::cout << "Running in single-threaded context" << std::endl;
}
```
- **Preconditions**: The `single_threaded` instance must be initialized.
- **Postconditions**: Returns whether the current thread matches the stored thread ID.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `is_not_thread`, `thread_started`

## is_not_thread

- **Signature**: `bool is_not_thread() const`
- **Description**: Checks if the current thread is different from the thread that created the `single_threaded` instance.
- **Parameters**: None
- **Return Value**: 
  - `true` if the current thread is different from the stored thread ID
  - `false` otherwise
- **Exceptions/Errors**: None
- **Example**:
```cpp
single_threaded s;
if (s.is_not_thread()) {
    std::cout << "Running in different thread context" << std::endl;
}
```
- **Preconditions**: The `single_threaded` instance must be initialized.
- **Postconditions**: Returns whether the current thread differs from the stored thread ID.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `is_single_thread`, `thread_started`

## thread_started

- **Signature**: `void thread_started()`
- **Description**: Records the current thread as the thread that started executing.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
single_threaded s;
s.thread_started();
// Thread start is recorded
```
- **Preconditions**: The `single_threaded` instance must be initialized.
- **Postconditions**: The current thread ID is recorded in the `single_threaded` instance.
- **Thread Safety**: Thread-safe (uses mutex protection)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `is_single_thread`, `is_not_thread`

## increment_guard

- **Signature**: `explicit increment_guard(int& c)`
- **Description**: Constructor for the increment_guard class, which increments a counter when created and decrements it when destroyed.
- **Parameters**:
  - `c` (int&): Reference to the counter to increment
- **Return Value**: None
- **Exceptions/Errors**: 
  - `TORRENT_ASSERT` may trigger if `m_cnt` is negative
- **Example**:
```cpp
int counter = 0;
{
    increment_guard guard(counter);
    // counter is incremented
}
// counter is decremented when guard goes out of scope
```
- **Preconditions**: The counter must be non-negative.
- **Postconditions**: The counter is incremented by 1.
- **Thread Safety**: Not thread-safe (no synchronization)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `increment_guard` destructor

## increment_guard

- **Signature**: `~increment_guard()`
- **Description**: Destructor for the increment_guard class, which decrements a counter when the object is destroyed.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: 
  - `TORRENT_ASSERT` may trigger if `m_cnt` is negative
- **Example**:
```cpp
int counter = 0;
{
    increment_guard guard(counter);
    // counter remains incremented
}
// counter is decremented when guard goes out of scope
```
- **Preconditions**: The increment_guard must have been constructed with a valid counter.
- **Postconditions**: The counter is decremented by 1.
- **Thread Safety**: Not thread-safe (no synchronization)
- **Complexity**: O(1) time, O(1) space
- **See Also**: `increment_guard` constructor

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/debug.hpp"

void example_usage() {
    // Track asynchronous operations
    if (has_outstanding_async("download")) {
        add_outstanding_async("download");
    }
    
    // Log outstanding operations
    int outstanding = log_async();
    if (outstanding > 0) {
        std::cout << "Found " << outstanding << " outstanding operations" << std::endl;
    }
    
    // Use single-threaded context
    single_threaded s;
    if (s.is_single_thread()) {
        std::cout << "Running in single-threaded context" << std::endl;
    }
    
    // Use increment guard
    int counter = 0;
    {
        increment_guard guard(counter);
        std::cout << "Counter is now: " << counter << std::endl;
    }
    std::cout << "Counter is now: " << counter << std::endl;
}
```

## Error Handling

```cpp
#include "libtorrent/debug.hpp"
#include <iostream>
#include <vector>

void error_handling_example() {
    try {
        // Check for outstanding operations before starting
        if (has_outstanding_async("upload")) {
            std::cerr << "Warning: There are outstanding upload operations!" << std::endl;
            // Handle the situation appropriately
        }
        
        // Start a new operation
        add_outstanding_async("upload");
        
        // Use the increment guard with proper error handling
        int counter = 0;
        increment_guard guard(counter);
        
        // Ensure the guard is properly used
        if (guard) {
            std::cout << "Guard is active, counter is: " << counter << std::endl;
        }
        
        // Clean up
        complete_async("upload");
    }
    catch (const std::exception& e) {
        std::cerr << "Error in debug operations: " << e.what() << std::endl;
        // Handle the error gracefully
    }
}
```

## Edge Cases

```cpp
#include "libtorrent/debug.hpp"
#include <iostream>
#include <string>

void edge_cases_example() {
    // Test with empty string name
    if (has_outstanding_async("")) {
        std::cout << "Unexpected: empty name has outstanding operations" << std::endl;
    }
    
    // Test with null pointer (undefined behavior)
    // Note: This is undefined behavior and should be avoided
    // if (has_outstanding_async(nullptr)) {
    //     std::cout << "Unexpected: null name has outstanding operations" << std::endl;
    // }
    
    // Test with very long name
    std::string long_name(1000, 'a');
    add_outstanding_async(long_name.c_str());
    if (has_outstanding_async(long_name.c_str())) {
        std::cout << "Found long name operation" << std::endl;
    }
    
    // Test with single-threaded context across threads
    single_threaded s;
    s.thread_started();
    
    // This should return false if called from a different thread
    std::cout << "Is single thread: " << s.is_single_thread() << std::endl;
    
    // Test increment guard with zero
    int zero_counter = 0;
    increment_guard guard(zero_counter);
    std::cout << "Zero counter after increment: " << zero_counter << std::endl;
}
```

# Best Practices

## Usage Guidelines

1. **Use `add_outstanding_async` and `complete_async` in pairs**: Always ensure that every `add_outstanding_async` call has a corresponding `complete_async` call.

2. **Check for outstanding operations before starting new ones**: Use `has_outstanding_async` to detect if there are existing operations that might conflict with new ones.

3. **Use `log_async` for debugging**: Call `log_async` periodically to monitor the state of asynchronous operations.

4. **Use `single_threaded` for thread safety**: Use the `single_threaded` class to ensure that certain operations only run on the correct thread.

5. **Use `increment_guard` for reference counting**: Use `increment_guard` to safely manage reference counts in multithreaded environments.

## Performance Tips

1. **Minimize mutex contention**: Since many of these functions use mutexes, minimize the frequency of calls to reduce contention.

2. **Avoid frequent logging**: The `log_async` function is expensive and should not be called too frequently in production code.

3. **Use `log_handler_allocators` sparingly**: This function can be expensive due to the detailed logging it performs.

4. **Optimize for the common case**: Most operations will be successful, so optimize for the path where everything works correctly.

## Common Mistakes to Avoid

1. **Missing `complete_async` calls**: Always ensure that every `add_outstanding_async` call is matched with a `complete_async` call.

2. **Using `single_threaded` incorrectly**: Ensure that `thread_started` is called before `is_single_thread` to avoid false negatives.

3. **Ignoring return values**: While most functions don't return values, the `log_async` function returns a count that should be checked.

4. **Using `increment_guard` without proper scope**: Ensure that the `increment_guard` object is properly scoped to avoid premature destruction.

# Code Review & Improvement Suggestions

## Potential Issues

**Function**: `add_outstanding_async`
**Issue**: Buffer overflow risk in `print_backtrace` call
**Severity**: Medium
**Impact**: Could lead to buffer overflow and undefined behavior
**Fix**: Add bounds checking and use safer alternatives:
```cpp
inline void add_outstanding_async(char const* name)
{
    std::lock_guard<std::mutex> l(_async_ops_mutex);
    async_t& a = _async_ops[name];
    if (a.stack.empty())
    {
        char stack_text[10000];
        // Add bounds checking
        if (print_backtrace(stack_text, sizeof(stack_text), 9) != 0) {
            // Handle error
        }
        
        // Skip the stack frame of 'add_out