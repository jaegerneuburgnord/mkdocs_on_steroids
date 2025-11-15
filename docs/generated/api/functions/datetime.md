# libtorrent Python Bindings - datetime.cpp API Documentation

## Function: convert (Duration)

- **Signature**: `static PyObject* convert(Duration const& d)`
- **Description**: Converts a libtorrent Duration type to a Python datetime.timedelta object. This function extracts microseconds from the duration and creates a timedelta object with appropriate days, seconds, and microseconds components.
- **Parameters**:
  - `d` (Duration const&): The libtorrent duration object to convert. Must be a valid Duration object representing time duration.
- **Return Value**:
  - Returns a PyObject* representing a Python datetime.timedelta object. The returned object is owned by the caller and must be managed properly.
  - Returns nullptr on error (though this is unlikely as the function doesn't check for errors).
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
  - The function assumes valid input and doesn't validate the Duration object.
- **Example**:
```cpp
auto result = convert(lt::duration(500000)); // 500,000 microseconds = 0.5 seconds
if (result != nullptr) {
    // Use the Python object
}
```
- **Preconditions**: The Duration object must be valid and contain a non-negative time value.
- **Postconditions**: A valid Python datetime.timedelta object is returned.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: convert(boost::posix_time::time_duration), bind_datetime

## Function: convert (time_duration)

- **Signature**: `static PyObject* convert(boost::posix_time::time_duration const& d)`
- **Description**: Converts a Boost.Python time_duration object to a Python datetime.timedelta object. The function extracts microseconds from the time duration and creates a timedelta object with appropriate days, seconds, and microseconds components.
- **Parameters**:
  - `d` (boost::posix_time::time_duration const&): The Boost time duration object to convert. Must be a valid time_duration object.
- **Return Value**:
  - Returns a PyObject* representing a Python datetime.timedelta object. The returned object is owned by the caller and must be managed properly.
  - Returns nullptr on error (though this is unlikely as the function doesn't check for errors).
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
  - The function assumes valid input and doesn't validate the time_duration object.
- **Example**:
```cpp
auto result = convert(boost::posix_time::time_duration(1, 2, 3)); // 1 hour, 2 minutes, 3 seconds
if (result != nullptr) {
    // Use the Python object
}
```
- **Preconditions**: The time_duration object must be valid and contain a non-negative time value.
- **Postconditions**: A valid Python datetime.timedelta object is returned.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: convert(Duration), bind_datetime

## Function: now (time_point)

- **Signature**: `lt::time_point now(::tag<lt::time_point>)`
- **Description**: Returns the current time point from the libtorrent clock. This function is used to get the current time in the libtorrent system clock, which is typically based on high-resolution time sources.
- **Parameters**:
  - `tag<lt::time_point>`: A tag type used to disambiguate overloads. This parameter is used for function overloading and doesn't have a runtime value.
- **Return Value**:
  - Returns a lt::time_point object representing the current time.
  - The returned time point is guaranteed to be valid and represents the current time.
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
- **Example**:
```cpp
auto current_time = now(::tag<lt::time_point>());
if (current_time != lt::time_point()) {
    // Use the current time point
}
```
- **Preconditions**: The libtorrent clock must be initialized and functional.
- **Postconditions**: A valid time point representing the current time is returned.
- **Thread Safety**: Thread-safe as it only calls a thread-safe clock function.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: now(time_point32), bind_datetime

## Function: now (time_point32)

- **Signature**: `lt::time_point32 now(::tag<lt::time_point32>)`
- **Description**: Returns the current time point from the libtorrent clock, but casts it to a 32-bit time point. This function is used to get the current time in a 32-bit representation, which may be useful for compatibility with systems that have limited time precision.
- **Parameters**:
  - `tag<lt::time_point32>`: A tag type used to disambiguate overloads. This parameter is used for function overloading and doesn't have a runtime value.
- **Return Value**:
  - Returns a lt::time_point32 object representing the current time in 32-bit precision.
  - The returned time point is guaranteed to be valid and represents the current time.
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
- **Example**:
```cpp
auto current_time = now(::tag<lt::time_point32>());
if (current_time != lt::time_point32()) {
    // Use the current time point
}
```
- **Preconditions**: The libtorrent clock must be initialized and functional.
- **Postconditions**: A valid time point in 32-bit precision representing the current time is returned.
- **Thread Safety**: Thread-safe as it only calls a thread-safe clock function.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: now(time_point), bind_datetime

## Function: convert (T)

- **Signature**: `static PyObject* convert(T const pt)`
- **Description**: Generic conversion function that converts various time point types to a Python datetime object. This function extracts time information from the given time point and creates a datetime object with appropriate year, month, day, hour, minute, second, and microsecond components.
- **Parameters**:
  - `pt` (T const): The time point object to convert. This can be any type that supports comparison with T() and has a system_clock::to_time_t conversion.
- **Return Value**:
  - Returns a PyObject* representing a Python datetime object. The returned object is owned by the caller and must be managed properly.
  - Returns nullptr on error (though this is unlikely as the function doesn't check for errors).
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
  - The function assumes valid input and doesn't validate the time point object.
- **Example**:
```cpp
auto result = convert(lt::time_point(std::chrono::steady_clock::now()));
if (result != nullptr) {
    // Use the Python object
}
```
- **Preconditions**: The time point object must be valid and contain a non-negative time value.
- **Postconditions**: A valid Python datetime object is returned.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: convert(boost::posix_time::ptime), bind_datetime

## Function: convert (ptime)

- **Signature**: `static PyObject* convert(boost::posix_time::ptime const& pt)`
- **Description**: Converts a Boost.Python ptime object to a Python datetime.datetime object. The function extracts date and time components from the ptime object and creates a datetime object with appropriate year, month, day, hour, minute, second, and microsecond components.
- **Parameters**:
  - `pt` (boost::posix_time::ptime const&): The Boost ptime object to convert. Must be a valid ptime object.
- **Return Value**:
  - Returns a PyObject* representing a Python datetime.datetime object. The returned object is owned by the caller and must be managed properly.
  - Returns nullptr on error (though this is unlikely as the function doesn't check for errors).
- **Exceptions/Errors**:
  - No exceptions thrown in normal operation.
  - The function assumes valid input and doesn't validate the ptime object.
- **Example**:
```cpp
auto result = convert(boost::posix_time::ptime(boost::gregorian::date(2023, 1, 1), boost::posix_time::time_duration(12, 30, 0)));
if (result != nullptr) {
    // Use the Python object
}
```
- **Preconditions**: The ptime object must be valid and contain a non-negative time value.
- **Postconditions**: A valid Python datetime.datetime object is returned.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: convert(T), bind_datetime

## Function: bind_datetime

- **Signature**: `void bind_datetime()`
- **Description**: Binds the datetime functionality to Python, creating the necessary Python objects and converters. This function imports the datetime module, creates references to datetime and timedelta classes, and registers converters for various time types.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - Could throw Python exceptions if the datetime module cannot be imported or if there are issues with the converter registration.
- **Example**:
```cpp
bind_datetime();
// Now datetime functionality is available in Python bindings
```
- **Preconditions**: The Python interpreter must be initialized and the Python C API must be available.
- **Postconditions**: The datetime functionality is bound to Python, making datetime objects and converters available.
- **Thread Safety**: Not thread-safe as it modifies global state.
- **Complexity**: O(1) time, O(1) space.
- **See Also**: convert(Duration), convert(boost::posix_time::time_duration)

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/bindings/python/src/datetime.hpp>
#include <iostream>

void example_basic_usage() {
    // Convert a duration to timedelta
    auto duration = lt::duration(1000000); // 1 second
    auto timedelta = convert(duration);
    if (timedelta != nullptr) {
        // Use the Python object
        // In practice, this would be passed to Python code
        std::cout << "Duration converted to timedelta" << std::endl;
    }
    
    // Get current time
    auto current_time = now(::tag<lt::time_point>());
    std::cout << "Current time: " << current_time.time_since_epoch().count() << std::endl;
    
    // Convert ptime to datetime
    auto ptime = boost::posix_time::ptime(boost::gregorian::date(2023, 1, 1), boost::posix_time::time_duration(12, 0, 0));
    auto datetime = convert(ptime);
    if (datetime != nullptr) {
        std::cout << "Ptime converted to datetime" << std::endl;
    }
}
```

## Error Handling

```cpp
#include <libtorrent/bindings/python/src/datetime.hpp>
#include <iostream>

void example_error_handling() {
    try {
        // Attempt to bind datetime functionality
        bind_datetime();
        
        // Convert a time duration
        auto duration = lt::duration(500000); // 0.5 seconds
        auto timedelta = convert(duration);
        
        if (timedelta == nullptr) {
            std::cerr << "Failed to convert duration to timedelta" << std::endl;
            return;
        }
        
        // Get current time
        auto current_time = now(::tag<lt::time_point>());
        
        if (current_time == lt::time_point()) {
            std::cerr << "Failed to get current time" << std::endl;
            return;
        }
        
        std::cout << "All operations successful" << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << "Exception occurred: " << e.what() << std::endl;
    }
    catch (...) {
        std::cerr << "Unknown exception occurred" << std::endl;
    }
}
```

## Edge Cases

```cpp
#include <libtorrent/bindings/python/src/datetime.hpp>
#include <iostream>

void example_edge_cases() {
    // Test with zero duration
    auto zero_duration = lt::duration(0);
    auto zero_timedelta = convert(zero_duration);
    if (zero_timedelta != nullptr) {
        std::cout << "Zero duration converted successfully" << std::endl;
    }
    
    // Test with negative duration (should be handled as zero)
    auto negative_duration = lt::duration(-1000000);
    auto negative_timedelta = convert(negative_duration);
    if (negative_timedelta != nullptr) {
        std::cout << "Negative duration converted successfully" << std::endl;
    }
    
    // Test with maximum duration
    auto max_duration = lt::duration::max();
    auto max_timedelta = convert(max_duration);
    if (max_timedelta != nullptr) {
        std::cout << "Maximum duration converted successfully" << std::endl;
    }
    
    // Test with minimum duration
    auto min_duration = lt::duration::min();
    auto min_timedelta = convert(min_duration);
    if (min_timedelta != nullptr) {
        std::cout << "Minimum duration converted successfully" << std::endl;
    }
}
```

# Best Practices

## Effective Usage

1. **Use appropriate conversion functions**: Use the specific conversion function for your data type (Duration, time_duration, ptime, etc.) rather than generic functions.

2. **Handle null returns**: Always check for null returns from conversion functions, especially when working with Python objects.

3. **Bind datetime early**: Call bind_datetime() early in your application startup to ensure datetime functionality is available when needed.

4. **Use const references**: When passing objects to conversion functions, use const references to avoid unnecessary copies.

5. **Consider time precision**: Be aware of the time precision differences between time_point and time_point32 when choosing which to use.

## Common Mistakes to Avoid

1. **Not checking return values**: Always check for null return values from conversion functions to avoid undefined behavior.

2. **Using invalid time points**: Ensure time points are valid before conversion to avoid undefined behavior.

3. **Ignoring thread safety**: Be aware that bind_datetime() is not thread-safe and should be called during initialization.

4. **Using outdated time types**: Prefer newer time types over older ones when possible.

5. **Not understanding the conversion**: Understand what each conversion function does and which one is appropriate for your use case.

## Performance Tips

1. **Minimize conversions**: Only convert when necessary, as conversions have overhead.

2. **Cache converted objects**: If you need to use the same time object multiple times, consider caching the converted Python object.

3. **Use appropriate time types**: Use time_point32 when you don't need high precision to save memory.

4. **Avoid unnecessary bindings**: Only bind what you need to avoid bloating your application.

5. **Profile conversion performance**: If conversions are a bottleneck, consider optimizing your time handling strategy.

# Code Review & Improvement Suggestions

## Function: convert (Duration)

**Issue**: The function doesn't validate the input duration before processing.
**Severity**: Medium
**Impact**: Could lead to undefined behavior if invalid duration is passed.
**Fix**: Add validation for the duration parameter.
```cpp
static PyObject* convert(Duration const& d)
{
    if (d <= Duration::zero()) {
        // Return zero duration
        object result = datetime_timedelta(
            0 // days
          , 0 // seconds
          , 0 // microseconds
        );
        return incref(result.ptr());
    }
    
    std::int64_t const us = lt::total_microseconds(d);
    object result = datetime_timedelta(
        0 // days
      , us / 1000000 // seconds
      , us % 1000000 // microseconds
    );

    return incref(result.ptr());
}
```

## Function: convert (time_duration)

**Issue**: The function doesn't validate the input time_duration before processing.
**Severity**: Medium
**Impact**: Could lead to undefined behavior if invalid time_duration is passed.
**Fix**: Add validation for the time_duration parameter.
```cpp
static PyObject* convert(boost::posix_time::time_duration const& d)
{
    if (d <= boost::posix_time::time_duration::zero()) {
        // Return zero duration
        object result = datetime_timedelta(
            0 // days
          , 0 // seconds
          , 0 // microseconds
        );
        return incref(result.ptr());
    }
    
    object result = datetime_timedelta(
        0 // days
      , 0 // seconds
      , d.total_microseconds()
    );

    return incref(result.ptr());
}
```

## Function: convert (T)

**Issue**: The function is incomplete and contains syntax errors.
**Severity**: Critical
**Impact**: The function will not compile or will produce incorrect results.
**Fix**: Complete the function implementation.
```cpp
static PyObject* convert(T const pt)
{
    using std::chrono::system_clock;
    using std::chrono::duration_cast;
    object result;
    if (pt > T())
    {
        time_t const tm = system_clock::to_time_t(system_clock::now()
            + duration_cast<system_clock::duration>(pt));
        // Complete the implementation
        // ...
    }
    else
    {
        // Handle zero or negative time
        object result = datetime_datetime(1970, 1, 1, 0, 0, 0);
        return incref(result.ptr());
    }
}
```

## Function: convert (ptime)

**Issue**: The function is incomplete and contains syntax errors.
**Severity**: Critical
**Impact**: The function will not compile or will produce incorrect results.
**Fix**: Complete the function implementation.
```cpp
static PyObject* convert(boost::posix_time::ptime const& pt)
{
    boost::gregorian::date date = pt.date();
    boost::posix_time::time_duration td = pt.time_of_day();

    object result = datetime_datetime(
        (int)date.year()
      , (int)date.month()
      , (int)date.day()
      , (int)td.hours()
      , (int)td.minutes()
      , (int)td.seconds()
      , (