# libtorrent Heterogeneous Queue API Documentation

## operator

- **Signature**: `void operator()(char* ptr)`
- **Description**: Deleter function that calls `std::free()` on the provided pointer. This function is used as a custom deleter for `std::unique_ptr` to properly deallocate memory allocated with `std::malloc`.
- **Parameters**:
  - `ptr` (char*): Pointer to memory that was allocated with `std::malloc`. The function will call `std::free()` on this pointer.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
// This function is typically used as a deleter for unique_ptr
std::unique_ptr<char, aux::free_deleter> ptr(static_cast<char*>(std::malloc(1024)));
// When ptr goes out of scope, operator() will be called automatically
```
- **Preconditions**: The pointer must have been allocated with `std::malloc` or similar function.
- **Postconditions**: The memory at the pointer address will be freed and made available for reuse.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `std::unique_ptr`, `aux::free_deleter`

## calculate_pad_bytes

- **Signature**: `std::size_t calculate_pad_bytes(char const* inptr, std::size_t alignment)`
- **Description**: Calculates the number of bytes needed to pad a pointer to achieve the specified alignment. This function is used to ensure proper memory alignment for objects stored in the heterogeneous queue.
- **Parameters**:
  - `inptr` (char const*): Pointer to the current position in memory where an object will be placed.
  - `alignment` (std::size_t): The alignment requirement (must be a power of 2).
- **Return Value**: The number of padding bytes needed to align the next object.
- **Exceptions/Errors**: None
- **Example**:
```cpp
char* current_position = some_memory;
std::size_t padding = calculate_pad_bytes(current_position, 16);
// Use padding to align the next object
```
- **Preconditions**: `alignment` must be a power of 2 and greater than 0.
- **Postconditions**: Returns a value between 0 and `alignment - 1` inclusive.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `heterogeneous_queue`, `alignof`

## heterogeneous_queue

- **Signature**: `heterogeneous_queue()`
- **Description**: Default constructor for the `heterogeneous_queue` class. Initializes an empty queue with no items.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
heterogeneous_queue<int> queue;
// queue is now initialized with no items
```
- **Preconditions**: None
- **Postconditions**: The queue is in a valid, empty state.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `~heterogeneous_queue`, `clear`

## heterogeneous_queue (Copy Constructor)

- **Signature**: `heterogeneous_queue(heterogeneous_queue const&) = delete;`
- **Description**: Deleted copy constructor. This prevents copying of `heterogeneous_queue` objects, ensuring that each queue owns its memory exclusively.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**: This function cannot be called directly as it is deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `swap`, `move`

## emplace_back

- **Signature**: `typename std::enable_if<std::is_base_of<T, U>::value, U&>::type emplace_back(Args&&... args)`
- **Description**: Adds a new object of type `U` to the end of the queue. The object is constructed in-place using the provided arguments. This function uses SFINAE to ensure that `U` is a derived class of `T`.
- **Parameters**:
  - `args` (Args&&...): Arguments to forward to the constructor of the object being created.
- **Return Value**: A reference to the newly created object of type `U`.
- **Exceptions/Errors**: May throw exceptions during object construction if the constructor throws.
- **Example**:
```cpp
struct Base {};
struct Derived : Base {};
heterogeneous_queue<Base> queue;
Derived& obj = queue.emplace_back(42); // Constructs Derived with argument 42
```
- **Preconditions**: The queue must not be in a deleted state and `U` must be a derived class of `T`.
- **Postconditions**: The object is constructed in the queue's memory and a reference to it is returned. The queue size is increased by one.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(1) amortized, O(n) in the worst case when memory needs to be reallocated.
- **See Also**: `clear`, `grow_capacity`

## get_pointers

- **Signature**: `void get_pointers(std::vector<T*>& out)`
- **Description**: Retrieves all pointers to objects in the queue that are of type `T` or its derived types. This function is useful for iterating over all objects in the queue that match a specific type.
- **Parameters**:
  - `out` (std::vector<T*>&): Reference to a vector that will be populated with pointers to objects of type `T`.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
std::vector<int*> pointers;
queue.get_pointers(pointers);
for (int* ptr : pointers) {
    // Process each pointer
}
```
- **Preconditions**: The queue must be in a valid state and `T` must be the base type of the objects in the queue.
- **Postconditions**: The vector `out` contains pointers to all objects of type `T` in the queue, in order of insertion.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(n) where n is the number of items in the queue.
- **See Also**: `front`, `size`

## swap

- **Signature**: `void swap(heterogeneous_queue& rhs)`
- **Description**: Swaps the contents of this queue with another queue. This operation is efficient and does not involve copying the actual data.
- **Parameters**:
  - `rhs` (heterogeneous_queue&): Reference to the other queue to swap with.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
heterogeneous_queue<int> queue1;
heterogeneous_queue<int> queue2;
queue1.swap(queue2); // Efficiently swaps contents
```
- **Preconditions**: The `rhs` queue must be in a valid state.
- **Postconditions**: The contents of this queue and the `rhs` queue are exchanged. The queue sizes remain unchanged.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(1)
- **See Also**: `clear`, `grow_capacity`

## size

- **Signature**: `int size() const`
- **Description**: Returns the number of items currently in the queue.
- **Parameters**: None
- **Return Value**: The number of items in the queue as an integer.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int count = queue.size();
if (count > 0) {
    // Process items in queue
}
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: The returned value accurately reflects the current number of items in the queue.
- **Thread Safety**: Thread-safe (reads only).
- **Complexity**: O(1)
- **See Also**: `empty`, `front`

## empty

- **Signature**: `bool empty() const`
- **Description**: Checks if the queue is empty.
- **Parameters**: None
- **Return Value**: `true` if the queue has no items, `false` otherwise.
- **Exceptions/Errors**: None
- **Example**:
```cpp
if (queue.empty()) {
    // Queue is empty, handle accordingly
}
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: Returns `true` if the queue has zero items, `false` otherwise.
- **Thread Safety**: Thread-safe (reads only).
- **Complexity**: O(1)
- **See Also**: `size`, `clear`

## clear

- **Signature**: `void clear()`
- **Description**: Removes all items from the queue and frees the associated memory. This operation does not deallocate the underlying storage, but rather resets the queue to an empty state.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
queue.clear(); // Removes all items from the queue
// queue is now empty
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: The queue is empty and the memory is freed. The underlying storage capacity remains unchanged.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(n) where n is the number of items in the queue.
- **See Also**: `size`, `swap`

## front

- **Signature**: `T* front()`
- **Description**: Returns a pointer to the first item in the queue, or `nullptr` if the queue is empty. This function is useful for accessing the first item without removing it.
- **Parameters**: None
- **Return Value**: Pointer to the first item in the queue, or `nullptr` if the queue is empty.
- **Exceptions/Errors**: None
- **Example**:
```cpp
T* first_item = queue.front();
if (first_item != nullptr) {
    // Process the first item
}
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: Returns a pointer to the first item in the queue, or `nullptr` if the queue is empty.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(1)
- **See Also**: `size`, `empty`

## heterogeneous_queue (Destructor)

- **Signature**: `~heterogeneous_queue()`
- **Description**: Destructor for the `heterogeneous_queue` class. This function calls `clear()` to remove all items from the queue and frees any associated memory.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
{
    heterogeneous_queue<int> queue;
    // Use queue
} // queue is automatically destroyed here
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: The queue is destroyed and all associated memory is freed.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(n) where n is the number of items in the queue.
- **See Also**: `clear`, `~heterogeneous_queue`

## grow_capacity

- **Signature**: `void grow_capacity(int const size)`
- **Description**: Increases the capacity of the queue's internal storage. This function is used internally when the queue needs to grow to accommodate more items.
- **Parameters**:
  - `size` (int const): The current size of the queue that needs to be accommodated.
- **Return Value**: None
- **Exceptions/Errors**: May throw exceptions if memory allocation fails.
- **Example**:
```cpp
// This function is typically called internally and not directly
queue.grow_capacity(100); // Internal use only
```
- **Preconditions**: The queue must be in a valid state.
- **Postconditions**: The queue's capacity has been increased to accommodate the specified size, with a minimum growth factor of 3/2 or 128 bytes.
- **Thread Safety**: Not thread-safe due to shared state modifications.
- **Complexity**: O(n) where n is the new capacity.
- **See Also**: `emplace_back`, `clear`

## move

- **Signature**: `static void move(char* dst, char* src) noexcept`
- **Description**: Moves an object from the source location to the destination location. This function is used internally to move objects when the queue's storage is reallocated.
- **Parameters**:
  - `dst` (char*): Destination memory location.
  - `src` (char*): Source memory location.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
// This function is typically called internally and not directly
move(destination_ptr, source_ptr); // Internal use only
```
- **Preconditions**: The source and destination pointers must be valid and properly aligned.
- **Postconditions**: The object at the source location is moved to the destination location, and the source location is left in a valid state.
- **Thread Safety**: Thread-safe if the move is atomic.
- **Complexity**: O(1)
- **See Also**: `grow_capacity`, `emplace_back`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/aux_/heterogeneous_queue.hpp"
#include <vector>

// Define a base class
struct Base {
    virtual ~Base() = default;
};

// Define a derived class
struct Derived : Base {
    int value;
    Derived(int v) : value(v) {}
};

int main() {
    // Create a heterogeneous queue
    libtorrent::aux::heterogeneous_queue<Base> queue;
    
    // Add objects to the queue
    queue.emplace_back(42);  // Adds a Derived object with value 42
    queue.emplace_back(84);  // Adds another Derived object with value 84
    
    // Get pointers to all Base objects
    std::vector<Base*> pointers;
    queue.get_pointers(pointers);
    
    // Process the objects
    for (Base* ptr : pointers) {
        if (Derived* derived = dynamic_cast<Derived*>(ptr)) {
            // Process Derived object
            std::cout << "Value: " << derived->value << std::endl;
        }
    }
    
    // Clear the queue
    queue.clear();
    
    return 0;
}
```

## Error Handling

```cpp
#include "libtorrent/aux_/heterogeneous_queue.hpp"
#include <iostream>

struct Base {
    virtual ~Base() = default;
};

struct Derived : Base {
    int value;
    Derived(int v) : value(v) {}
};

int main() {
    libtorrent::aux::heterogeneous_queue<Base> queue;
    
    try {
        // Attempt to add an object
        Derived& obj = queue.emplace_back(100);
        
        // Check if the object was added successfully
        if (queue.empty()) {
            std::cerr << "Queue is unexpectedly empty after emplacement" << std::endl;
            return 1;
        }
        
        // Process the object
        std::cout << "Added object with value: " << obj.value << std::endl;
        
        // Clear the queue
        queue.clear();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include "libtorrent/aux_/heterogeneous_queue.hpp"
#include <vector>

struct Base {
    virtual ~Base() = default;
};

struct Derived : Base {
    int value;
    Derived(int v) : value(v) {}
};

int main() {
    libtorrent::aux::heterogeneous_queue<Base> queue;
    
    // Test with empty queue
    if (queue.empty()) {
        std::cout << "Queue is empty as expected" << std::endl;
    }
    
    // Test front on empty queue
    Base* front = queue.front();
    if (front == nullptr) {
        std::cout << "front() returns nullptr on empty queue" << std::endl;
    }
    
    // Test with single item
    queue.emplace_back(42);
    if (!queue.empty()) {
        Base* single_item = queue.front();
        if (single_item != nullptr) {
            std::cout << "Front item exists and is not null" << std::endl;
        }
    }
    
    // Test swap with empty queue
    libtorrent::aux::heterogeneous_queue<Base> empty_queue;
    queue.swap(empty_queue);
    if (queue.empty() && !empty_queue.empty()) {
        std::cout << "Swap operation worked correctly" << std::endl;
    }
    
    return 0;
}
```

# Best Practices

## Effective Usage

1. **Use emplace_back instead of push_back**: Since the queue uses in-place construction, prefer `emplace_back` which constructs objects directly in the storage.

2. **Check for empty before accessing**: Always check if the queue is empty before calling `front()` to avoid undefined behavior.

3. **Use get_pointers for type-specific processing**: When you need to process objects of a specific type, use `get_pointers` to get all relevant pointers.

4. **Handle memory allocation failures**: Be aware that `emplace_back` may throw exceptions if memory allocation fails.

5. **Use clear() for cleanup**: When you're done with a queue, call `clear()` to free memory.

## Common Mistakes to Avoid

1. **Accessing front() on empty queue**: This will return `nullptr`, but dereferencing it leads to undefined behavior.

2. **Assuming items are in a specific order**: The queue maintains insertion order, but this can be violated if objects are moved between queues.

3. **Not handling exceptions**: Memory allocation failures can cause exceptions in `emplace_back`.

4. **Copying queues**: The copy constructor is deleted, so you cannot copy queues using the assignment operator.

## Performance Tips

1. **Minimize allocations**: The queue allocates memory for all items in a contiguous block, so minimizing the number of allocations is beneficial.

2. **Use appropriate initial capacity**: If you know the approximate number of items you'll need, consider preallocating space to avoid multiple reallocations.

3. **Use move semantics**: When adding large objects, ensure they support move construction to avoid expensive copies.

4. **Batch operations**: When adding many items, consider adding them in batches to minimize reallocation overhead.

# Code Review & Improvement Suggestions

## Potential Issues

**Function