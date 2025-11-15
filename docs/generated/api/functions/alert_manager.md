# libtorrent Alert Manager API Documentation

## alert_manager

- **Signature**: `alert_manager(int queue_limit, alert_category_t alert_mask = alert_category::error)`
- **Description**: Constructs an alert manager with the specified queue size limit and alert category mask. The alert manager is responsible for managing and dispatching alerts in the libtorrent library. It maintains a queue of alerts and allows filtering based on alert categories.
- **Parameters**:
  - `queue_limit` (int): The maximum number of alerts that can be stored in the queue. Must be greater than 0. This limits the memory usage and prevents the queue from growing indefinitely.
  - `alert_mask` (alert_category_t): The category mask that determines which alerts should be posted. By default, only error alerts are posted. This can be combined with other alert categories using bitwise OR operations.
- **Return Value**: 
  - No return value (constructor)
- **Exceptions/Errors**:
  - None - this constructor does not throw exceptions
- **Example**:
```cpp
// Create an alert manager with a queue limit of 100 and all alert categories enabled
auto alert_manager = alert_manager(100, alert_category::all);
```
- **Preconditions**: 
  - `queue_limit > 0`
  - `alert_mask` must be a valid alert category value
- **Postconditions**: 
  - A valid alert_manager instance is created
  - The alert queue is initialized with the specified size limit
  - The alert mask is set to the specified value
- **Thread Safety**: 
  - Not thread-safe during construction - the object must be constructed before any threads use it
- **Complexity**: 
  - O(1) time and space complexity
- **See Also**: `emplace_alert()`, `set_alert_mask()`, `alert_mask()`

## emplace_alert

- **Signature**: `void emplace_alert(Args&&... args) try`
- **Description**: Emplaces an alert of type T into the alert queue. This function creates an alert in-place using the provided arguments and adds it to the appropriate queue. The alert is only added if it passes the category filter and there's space in the queue.
- **Parameters**:
  - `args` (Args&&...): Arguments to forward to the constructor of the alert type T. These arguments are used to construct the alert object in-place.
- **Return Value**: 
  - void
- **Exceptions/Errors**:
  - No exceptions are thrown by this function
  - The function uses a try block to handle any potential exceptions that might occur during alert construction
- **Example**:
```cpp
// Create a peer_connection_closed_alert with specific parameters
alert_manager em(100);
em.emplace_alert("peer disconnected", 12345);
```
- **Preconditions**: 
  - The alert manager must be valid and not destroyed
  - The alert type T must be constructible with the provided arguments
- **Postconditions**: 
  - An alert of type T is created and added to the alert queue (if it passes filtering and there's space)
  - The alert is added to the queue corresponding to the current generation
- **Thread Safety**: 
  - Thread-safe - uses a recursive mutex to protect the alert queue
- **Complexity**: 
  - O(1) time complexity for the alert creation and queue insertion
- **See Also**: `alert_manager()`, `should_post()`, `set_alert_mask()`

## should_post

- **Signature**: `bool should_post() const`
- **Description**: Checks whether alerts of a specific category should be posted based on the current alert mask. This function is typically used by individual alert types to determine if they should be posted to the alert queue.
- **Parameters**: 
  - None
- **Return Value**: 
  - `true` if alerts of the specified category should be posted
  - `false` otherwise
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// Check if error alerts should be posted
if (alert_manager.should_post<error_alert>()) {
    // Post error alert
}
```
- **Preconditions**: 
  - The alert manager must be valid and not destroyed
- **Postconditions**: 
  - The function returns the result of the category check
- **Thread Safety**: 
  - Thread-safe - uses relaxed memory ordering for the atomic load
- **Complexity**: 
  - O(1) time complexity
- **See Also**: `set_alert_mask()`, `alert_mask()`, `emplace_alert()`

## set_alert_mask

- **Signature**: `void set_alert_mask(alert_category_t const m) noexcept`
- **Description**: Sets the alert category mask to control which alerts are posted. This function allows runtime configuration of which types of alerts are enabled or disabled.
- **Parameters**:
  - `m` (alert_category_t const): The new alert category mask. This is a bitwise OR of alert categories. For example, to enable both error and status alerts: `alert_category::error | alert_category::status`.
- **Return Value**: 
  - void
- **Exceptions/Errors**:
  - None - marked as noexcept
- **Example**:
```cpp
// Enable all alerts
alert_manager.set_alert_mask(alert_category::all);

// Enable only error and warning alerts
alert_manager.set_alert_mask(alert_category::error | alert_category::warning);
```
- **Preconditions**: 
  - The alert manager must be valid and not destroyed
- **Postconditions**: 
  - The alert mask is updated to the specified value
  - Future alerts will be filtered according to the new mask
- **Thread Safety**: 
  - Thread-safe - uses atomic operations to update the mask
- **Complexity**: 
  - O(1) time complexity
- **See Also**: `alert_mask()`, `should_post()`, `emplace_alert()`

## alert_mask

- **Signature**: `alert_category_t alert_mask() const noexcept`
- **Description**: Returns the current alert category mask. This function allows querying the current set of enabled alert categories.
- **Parameters**: 
  - None
- **Return Value**: 
  - The current alert category mask as an alert_category_t value
- **Exceptions/Errors**:
  - None - marked as noexcept
- **Example**:
```cpp
// Get the current alert mask
auto mask = alert_manager.alert_mask();

// Check if error alerts are enabled
if (mask & alert_category::error) {
    // Error alerts are enabled
}
```
- **Preconditions**: 
  - The alert manager must be valid and not destroyed
- **Postconditions**: 
  - Returns the current alert mask value
- **Thread Safety**: 
  - Thread-safe - uses relaxed memory ordering for the atomic load
- **Complexity**: 
  - O(1) time complexity
- **See Also**: `set_alert_mask()`, `should_post()`, `emplace_alert()`

## alert_queue_size_limit

- **Signature**: `int alert_queue_size_limit() const noexcept`
- **Description**: Returns the maximum number of alerts that can be stored in the queue. This provides a way to check the current queue size limit that was specified during construction.
- **Parameters**: 
  - None
- **Return Value**: 
  - The maximum number of alerts that can be stored in the queue
- **Exceptions/Errors**:
  - None - marked as noexcept
- **Example**:
```cpp
// Get the current queue size limit
int limit = alert_manager.alert_queue_size_limit();

// Check if the limit is reasonable
if (limit > 1000) {
    // Limit is higher than typical
}
```
- **Preconditions**: 
  - The alert manager must be valid and not destroyed
- **Postconditions**: 
  - Returns the queue size limit that was specified during construction
- **Thread Safety**: 
  - Thread-safe - the value is read with relaxed memory ordering
- **Complexity**: 
  - O(1) time complexity
- **See Also**: `alert_manager()`, `emplace_alert()`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/alert_manager.hpp>

// Create an alert manager with default settings
libtorrent::aux::alert_manager alert_manager(100);

// Set custom alert mask to include all categories
alert_manager.set_alert_mask(libtorrent::alert_category::all);

// Check if a specific alert type should be posted
if (alert_manager.should_post<libtorrent::peer_connection_closed_alert>()) {
    // Post the alert
    alert_manager.emplace_alert("peer disconnected", 12345);
}

// Get the current queue size limit
int limit = alert_manager.alert_queue_size_limit();
```

## Error Handling

```cpp
#include <libtorrent/aux_/alert_manager.hpp>
#include <iostream>

void handle_alerts() {
    try {
        libtorrent::aux::alert_manager alert_manager(50);
        
        // Set alert mask to include only error and warning categories
        alert_manager.set_alert_mask(libtorrent::alert_category::error | libtorrent::alert_category::warning);
        
        // Check if error alerts should be posted
        if (alert_manager.should_post<libtorrent::error_alert>()) {
            alert_manager.emplace_alert("connection failed", "timeout");
        }
        
        // Check if the alert queue is full
        if (alert_manager.alert_queue_size_limit() == 0) {
            std::cerr << "Alert queue is disabled" << std::endl;
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Error creating alert manager: " << e.what() << std::endl;
    }
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/alert_manager.hpp>
#include <thread>
#include <atomic>

// Test with very small queue limit
void test_small_queue() {
    libtorrent::aux::alert_manager alert_manager(1);
    
    // Try to add multiple alerts
    for (int i = 0; i < 5; ++i) {
        if (alert_manager.should_post<libtorrent::status_alert>()) {
            alert_manager.emplace_alert("status update " + std::to_string(i));
        }
    }
    
    // Check if alerts were actually posted (only one should be stored)
    if (alert_manager.alert_queue_size_limit() == 1) {
        // Only one alert can be stored
    }
}

// Test with zero queue limit (invalid)
void test_zero_queue() {
    try {
        // This will likely cause an assertion failure or exception
        libtorrent::aux::alert_manager alert_manager(0);
    } catch (const std::exception& e) {
        std::cout << "Caught exception: " << e.what() << std::endl;
    }
}
```

# Best Practices

## Effective Usage

1. **Set appropriate queue limits**: Choose a queue size that balances memory usage and the need to capture important alerts. A typical value is 100-500 alerts.

2. **Use selective alert filtering**: Only enable the alert categories you actually need to avoid overwhelming your application with unnecessary notifications.

3. **Check alert limits before posting**: Use `alert_queue_size_limit()` to determine if alerts can be posted.

4. **Use const-correctness**: Use `const` where appropriate to ensure thread safety and prevent unintended modifications.

## Common Mistakes to Avoid

1. **Ignoring queue limits**: Don't assume alerts will always be posted. Always check if there's room in the queue.

2. **Unnecessary alert creation**: Only create alerts when they're actually needed. Creating alerts for debug purposes can impact performance.

3. **Incorrect alert categories**: Be careful when combining alert categories. Use the provided constants and ensure the combinations make sense.

4. **Not handling thread safety**: While the alert manager itself is thread-safe, be aware of the locking mechanism used.

## Performance Tips

1. **Use emplace_alert for efficiency**: Use `emplace_alert` instead of `push_alert` when possible to avoid unnecessary copy construction.

2. **Minimize alert creation**: Only create alerts when they're actually needed. Excessive alert creation can impact performance.

3. **Batch alerts when possible**: If you need to post multiple related alerts, consider batching them or using a single alert with a collection of data.

4. **Use the alert mask effectively**: Set the alert mask to only include the categories you need to reduce the overhead of processing irrelevant alerts.

# Code Review & Improvement Suggestions

## Potential Issues

**Function**: `alert_manager`
**Issue**: Missing bounds checking for queue_limit parameter
**Severity**: Medium
**Impact**: Could lead to undefined behavior if queue_limit is 0 or negative
**Fix**: Add validation for queue_limit parameter

```cpp
explicit alert_manager(int queue_limit, alert_category_t alert_mask = alert_category::error)
    : m_queue_size_limit(queue_limit > 0 ? queue_limit : 1)
    , m_alert_mask(alert_mask)
{
    // Ensure queue_limit is positive
    TORRENT_ASSERT(queue_limit > 0);
}
```

**Function**: `emplace_alert`
**Issue**: No check for alert queue overflow in the main logic
**Severity**: High
**Impact**: Could lead to memory exhaustion if alerts are constantly being added without space
**Fix**: Add explicit overflow checking

```cpp
void emplace_alert(Args&&... args) try
{
    std::unique_lock<std::recursive_mutex> lock(m_mutex);
    
    heterogeneous_queue<alert>& queue = m_alerts[m_generation & 1];
    
    // Check if queue is at capacity
    if (queue.size() >= static_cast<size_t>(m_queue_size_limit)) {
        // Queue is full, skip adding this alert
        return;
    }
    
    // Check if alert should be posted based on category
    if (!should_post<T>()) {
        return;
    }
    
    // Add alert to queue
    queue.emplace(std::forward<Args>(args)...);
    
    // Increment generation if needed
    if (queue.size() == 1) {
        ++m_generation;
    }
}
```

**Function**: `should_post`
**Issue**: No validation of T::static_category
**Severity**: Low
**Impact**: Could lead to incorrect filtering if the static_category is not properly defined
**Fix**: Add assertion to ensure static_category is properly defined

```cpp
bool should_post() const
{
    TORRENT_ASSERT((T::static_category & alert_category::all) != 0);
    return bool(m_alert_mask.load(std::memory_order_relaxed) & T::static_category);
}
```

## Modernization Opportunities

**Function**: `alert_manager`
**Opportunity**: Use C++11's noexcept specification for constructor
**Benefit**: Improves performance by allowing compiler optimizations
**Example**:
```cpp
explicit alert_manager(int queue_limit, alert_category_t alert_mask = alert_category::error) noexcept;
```

**Function**: `set_alert_mask`
**Opportunity**: Use std::atomic_flag for better performance in some cases
**Benefit**: More efficient for simple boolean operations
**Example**:
```cpp
// Could use std::atomic_flag if we only needed to set/reset the mask
// However, for bitmask operations, std::atomic<alert_category_t> is appropriate
```

**Function**: `emplace_alert`
**Opportunity**: Use C++17's std::optional for error handling
**Benefit**: Clearer error reporting if alert creation fails
**Example**:
```cpp
// Not applicable since the function uses try-catch already
// But could return std::optional<bool> if we wanted to indicate success/failure
```

## Refactoring Suggestions

**Function**: `alert_manager`
**Suggestion**: Move alert queue management to a separate class
**Benefit**: Improves modularity and makes the alert_manager class easier to test
**Example**:
```cpp
// Could extract the alert queue management into a separate AlertQueue class
// This would make the alert_manager class more focused on its primary responsibility
```

**Function**: `should_post`
**Suggestion**: Move should_post check to a separate method
**Benefit**: Improves code readability and reusability
**Example**:
```cpp
// Could extract the category checking logic to a separate method
// This would make it easier to extend or modify the alert filtering logic
```

## Performance Optimizations

**Function**: `emplace_alert`
**Opportunity**: Use move semantics for alert construction
**Benefit**: Reduces unnecessary copying of alert data
**Example**:
```cpp
// The function already uses perfect forwarding, which is optimal
// However, ensure that any data passed to the alert constructor is moveable
```

**Function**: `alert_mask`
**Opportunity**: Use const reference for return value
**Benefit**: Avoids unnecessary copying of the return value
**Example**:
```cpp
// The function already returns by value, which is fine for small types
// But could return a const reference if the type were larger
```

**Function**: `set_alert_mask`
**Opportunity**: Add noexcept specification
**Benefit**: Improves performance and allows compiler optimizations
**Example**:
```cpp
void set_alert_mask(alert_category_t const m) noexcept
{
    m_alert_mask = m;
}
```