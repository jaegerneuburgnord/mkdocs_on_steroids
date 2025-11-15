# libtorrent Torrent View API Documentation

## Function: torrent_state

- **Signature**: `std::string torrent_state(lt::torrent_status const& s)`
- **Description**: Converts a torrent status into a human-readable string representation, including error messages when applicable. The function maps internal torrent state codes to descriptive strings and handles error conditions.
- **Parameters**:
  - `s` (lt::torrent_status const&): The torrent status object to convert to string. This must be a valid torrent status object.
- **Return Value**:
  - Returns a string representation of the torrent state. This includes:
    - Error messages if `s.errc` is set
    - State names from the state_str array for normal states
    - Empty string for unknown states
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles invalid state values by returning an empty string
- **Example**:
```cpp
auto status = get_torrent_status();
auto state_str = torrent_state(status);
std::cout << "Torrent state: " << state_str << std::endl;
```
- **Preconditions**: The `lt::torrent_status` object must be valid and not corrupted.
- **Postconditions**: Returns a string representation of the torrent state, even if the state is invalid.
- **Thread Safety**: The function is thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `lt::torrent_status`, `lt::error_code`

## Function: cmp_torrent_position

- **Signature**: `bool cmp_torrent_position(lt::torrent_status const* lhs, lt::torrent_status const* rhs)`
- **Description**: Compares two torrent status objects by their queue position, used for sorting torrents in the view. Prioritizes torrents based on their position in the download queue.
- **Parameters**:
  - `lhs` (lt::torrent_status const*): Pointer to the first torrent status object to compare
  - `rhs` (lt::torrent_status const*): Pointer to the second torrent status object to compare
- **Return Value**:
  - Returns `true` if the first torrent should appear before the second in the sorted order
  - Returns `false` otherwise
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function assumes valid pointers to torrent status objects
- **Example**:
```cpp
// This function would typically be used in a sorting operation
std::sort(torrents.begin(), torrents.end(), &cmp_torrent_position);
```
- **Preconditions**: Both pointers must be valid and point to existing torrent status objects.
- **Postconditions**: Returns a boolean indicating the relative order of the two torrents.
- **Thread Safety**: The function is thread-safe for concurrent read-only access to the data.
- **Complexity**: O(1) time complexity.
- **See Also**: `std::sort`, `cmp_torrent_name`, `cmp_torrent_size`

## Function: cmp_torrent_name

- **Signature**: `bool cmp_torrent_name(lt::torrent_status const* lhs, lt::torrent_status const* rhs)`
- **Description**: Compares two torrent status objects by their names, used for sorting torrents in the view. This provides lexicographic ordering of torrent names.
- **Parameters**:
  - `lhs` (lt::torrent_status const*): Pointer to the first torrent status object to compare
  - `rhs` (lt::torrent_status const*): Pointer to the second torrent status object to compare
- **Return Value**:
  - Returns `true` if the first torrent's name comes before the second's in lexicographic order
  - Returns `false` otherwise
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function assumes valid pointers to torrent status objects
- **Example**:
```cpp
// This function would typically be used in a sorting operation
std::sort(torrents.begin(), torrents.end(), &cmp_torrent_name);
```
- **Preconditions**: Both pointers must be valid and point to existing torrent status objects.
- **Postconditions**: Returns a boolean indicating the relative order of the two torrents.
- **Thread Safety**: The function is thread-safe for concurrent read-only access to the data.
- **Complexity**: O(n) time complexity where n is the length of the shorter name.
- **See Also**: `std::sort`, `cmp_torrent_position`, `cmp_torrent_size`

## Function: cmp_torrent_size

- **Signature**: `bool cmp_torrent_size(lt::torrent_status const* lhs, lt::torrent_status const* rhs)`
- **Description**: Compares two torrent status objects by their total download size, used for sorting torrents in the view. Sorts by total download size in descending order.
- **Parameters**:
  - `lhs` (lt::torrent_status const*): Pointer to the first torrent status object to compare
  - `rhs` (lt::torrent_status const*): Pointer to the second torrent status object to compare
- **Return Value**:
  - Returns `true` if the first torrent has a larger total download size than the second
  - Returns `false` otherwise
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function assumes valid pointers to torrent status objects
- **Example**:
```cpp
// This function would typically be used in a sorting operation
std::sort(torrents.begin(), torrents.end(), &cmp_torrent_size);
```
- **Preconditions**: Both pointers must be valid and point to existing torrent status objects.
- **Postconditions**: Returns a boolean indicating the relative order of the two torrents.
- **Thread Safety**: The function is thread-safe for concurrent read-only access to the data.
- **Complexity**: O(1) time complexity.
- **See Also**: `std::sort`, `cmp_torrent_position`, `cmp_torrent_name`

## Function: torrent_view

- **Signature**: `torrent_view::torrent_view()`
- **Description**: Default constructor for the torrent_view class. Initializes the view with default settings and creates an empty torrent view.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The constructor ensures all member variables are properly initialized
- **Example**:
```cpp
torrent_view view;
// The view is now ready to be used
```
- **Preconditions**: None
- **Postconditions**: The torrent_view object is in a valid state with all member variables initialized to default values.
- **Thread Safety**: The constructor is not thread-safe and should only be called from a single thread during object creation.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `set_size`, `set_filter`, `set_sort_order`

## Function: set_size

- **Signature**: `void torrent_view::set_size(int width, int height)`
- **Description**: Sets the size of the torrent view and triggers a re-render if the dimensions have changed. This function updates the view's dimensions and refreshes the display.
- **Parameters**:
  - `width` (int): The new width of the view in characters
  - `height` (int): The new height of the view in characters
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles invalid dimensions gracefully
- **Example**:
```cpp
view.set_size(80, 24);
// The view is now sized to 80x24 characters
```
- **Preconditions**: The view must be constructed and valid.
- **Postconditions**: The view dimensions are updated to the specified values and a render operation is triggered if dimensions changed.
- **Thread Safety**: The function is not thread-safe and should only be called from the main thread.
- **Complexity**: O(1) time complexity.
- **See Also**: `height`, `render`, `update_filtered_torrents`

## Function: filter

- **Signature**: `int torrent_view::filter() const`
- **Description**: Gets the current filter setting for the torrent view. Returns the current filter mode that determines which torrents are displayed.
- **Parameters**: None
- **Return Value**:
  - Returns an integer representing the current filter setting
  - The value corresponds to one of the filter constants (e.g., torrents_all, torrents_downloading, etc.)
- **Exceptions/Errors**:
  - No exceptions are thrown
- **Example**:
```cpp
int current_filter = view.filter();
if (current_filter == torrents_downloading) {
    std::cout << "Filtering downloading torrents" << std::endl;
}
```
- **Preconditions**: The view must be constructed and valid.
- **Postconditions**: Returns the current filter setting.
- **Thread Safety**: The function is thread-safe for concurrent read access.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_filter`, `show_torrent`, `update_filtered_torrents`

## Function: set_filter

- **Signature**: `void torrent_view::set_filter(int filter)`
- **Description**: Sets the filter for the torrent view and triggers a re-render. Updates which torrents are displayed based on the filter setting.
- **Parameters**:
  - `filter` (int): The new filter setting to apply
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles invalid filter values by ignoring them
- **Example**:
```cpp
view.set_filter(torrents_downloading);
// Now only downloading torrents will be displayed
```
- **Preconditions**: The view must be constructed and valid.
- **Postconditions**: The filter setting is updated and the view is re-rendered to reflect the new filter.
- **Thread Safety**: The function is not thread-safe and should only be called from the main thread.
- **Complexity**: O(n) time complexity where n is the number of torrents.
- **See Also**: `filter`, `show_torrent`, `update_filtered_torrents`

## Function: sort_order

- **Signature**: `int torrent_view::sort_order() const`
- **Description**: Gets the current sort order setting for the torrent view. Returns the current sorting criterion used to organize torrents.
- **Parameters**: None
- **Return Value**:
  - Returns an integer representing the current sort order
  - The value corresponds to one of the sort order constants (e.g., order::queue, order::name, etc.)
- **Exceptions/Errors**:
  - No exceptions are thrown
- **Example**:
```cpp
int current_sort = view.sort_order();
if (current_sort == order::name) {
    std::cout << "Torrents are sorted by name" << std::endl;
}
```
- **Preconditions**: The view must be constructed and valid.
- **Postconditions**: Returns the current sort order setting.
- **Thread Safety**: The function is thread-safe for concurrent read access.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_sort_order`, `update_sort_order`, `update_filtered_torrents`

## Function: set_sort_order

- **Signature**: `void torrent_view::set_sort_order(int const o)`
- **Description**: Sets the sort order for the torrent view and triggers a re-render. Updates how torrents are organized in the view based on the specified sort order.
- **Parameters**:
  - `o` (int const): The new sort order to apply
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles invalid sort order values by ignoring them
- **Example**:
```cpp
view.set_sort_order(order::name);
// T
```

## Function: get_active_torrent

- **Signature**: `lt::torrent_status const& torrent_view::get_active_torrent() const`
- **Description**: Retrieves the torrent status of the currently active torrent in the view. Returns a reference to the torrent status object corresponding to the currently selected torrent.
- **Parameters**: None
- **Return Value**:
  - Returns a const reference to the torrent status of the active torrent
  - The reference is valid only if there are torrents in the view
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function ensures the active torrent index is valid before returning the reference
- **Example**:
```cpp
auto& active_torrent = view.get_active_torrent();
std::cout << "Active torrent: " << active_torrent.name << std::endl;
```
- **Preconditions**: The view must be constructed and valid. There must be at least one torrent in the view.
- **Postconditions**: Returns a valid reference to the active torrent's status, or the last torrent if no active torrent exists.
- **Thread Safety**: The function is thread-safe for concurrent read access to the data.
- **Complexity**: O(1) time complexity.
- **See Also**: `get_active_handle`, `update_torrents`, `render`

## Function: get_active_handle

- **Signature**: `lt::torrent_handle torrent_view::get_active_handle() const`
- **Description**: Retrieves the torrent handle of the currently active torrent in the view. Returns the handle for the torrent that is currently selected.
- **Parameters**: None
- **Return Value**:
  - Returns the torrent handle for the active torrent
  - Returns an empty handle if no active torrent exists
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function ensures the active torrent index is valid before returning the handle
- **Example**:
```cpp
auto handle = view.get_active_handle();
if (handle.is_valid()) {
    std::cout << "Active torrent handle: " << handle.info_hash() << std::endl;
}
```
- **Preconditions**: The view must be constructed and valid. There must be at least one torrent in the view.
- **Postconditions**: Returns a valid torrent handle if one exists, or an empty handle if no active torrent is selected.
- **Thread Safety**: The function is thread-safe for concurrent read access to the data.
- **Complexity**: O(1) time complexity.
- **See Also**: `get_active_torrent`, `update_torrents`, `remove_torrent`

## Function: remove_torrent

- **Signature**: `void torrent_view::remove_torrent(lt::torrent_handle h)`
- **Description**: Removes a torrent from the view based on its handle. This function removes the torrent from both the internal data structures and the display.
- **Parameters**:
  - `h` (lt::torrent_handle): The handle of the torrent to remove
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles non-existent torrents gracefully
- **Example**:
```cpp
view.remove_torrent(torrent_handle);
// The torrent is now removed from the view
```
- **Preconditions**: The view must be constructed and valid. The handle must be a valid torrent handle.
- **Postconditions**: The torrent is removed from the view and a re-render is triggered if necessary.
- **Thread Safety**: The function is not thread-safe and should only be called from the main thread.
- **Complexity**: O(n) time complexity where n is the number of torrents in the view.
- **See Also**: `update_torrents`, `set_filter`, `render`

## Function: update_torrents

- **Signature**: `void torrent_view::update_torrents(std::vector<lt::torrent_status> st)`
- **Description**: Updates the torrent view with new torrent status information. This function processes the provided torrent status vector and updates the internal state of the view.
- **Parameters**:
  - `st` (std::vector<lt::torrent_status>): A vector of torrent status objects to update
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles empty vectors and invalid status objects
- **Example**:
```cpp
std::vector<lt::torrent_status> status_updates = get_torrent_status_updates();
view.update_torrents(status_updates);
// The view is now updated with the latest torrent status
```
- **Preconditions**: The view must be constructed and valid. The vector of status objects must be valid.
- **Postconditions**: The internal state of the view is updated with the new status information and the view may be re-rendered.
- **Thread Safety**: The function is not thread-safe and should only be called from the main thread.
- **Complexity**: O(n log n) time complexity where n is the number of torrents in the view.
- **See Also**: `update_filtered_torrents`, `update_sort_order`, `render`

## Function: height

- **Signature**: `int torrent_view::height() const`
- **Description**: Gets the height of the torrent view in characters. Returns the current height setting of the view.
- **Parameters**: None
- **Return Value**:
  - Returns the height of the view in characters
  - Returns 0 if the view has not been sized
- **Exceptions/Errors**:
  - No exceptions are thrown
- **Example**:
```cpp
int view_height = view.height();
std::cout << "View height: " << view_height << " characters" << std::endl;
```
- **Preconditions**: The view must be constructed and valid.
- **Postconditions**: Returns the current height setting of the view.
- **Thread Safety**: The function is thread-safe for concurrent read access.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_size`, `render`, `arrow_up`

## Function: arrow_up

- **Signature**: `void torrent_view::arrow_up()`
- **Description**: Moves the active torrent selection up by one position. This function handles the navigation of the active torrent selection in the view.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions are thrown
  - The function handles empty views and already at top positions gracefully
- **Example**:
```cpp
view.arrow_up();
// The active torrent selection moves up by one
```
- **Preconditions**: The view must be constructed and valid. There must be at least one torrent in the view.
- **Postconditions**: The active torrent selection is moved up by one position, or remains at the top if already at the top.
- **Thread Safety**: The function is not thread-safe and should only be called from the main thread.
- **Complexity**: O(1) time complexity.
- **See Also**: `arrow_down`, `get_active_torrent`, `render`

## Function: arrow_down

- **Signature**: `void torrent_view::