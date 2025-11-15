# API Documentation for libtorrent Alert Types

## peer_alert

- **Signature**: `auto peer_alert()`
- **Description**: This alert is generated when a peer-related event occurs in the torrent client. It serves as a base class for more specific peer alerts. This alert contains information about the peer that triggered the event, including the torrent handle, peer endpoint, and peer ID.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the peer is associated with. This handle is used to identify the torrent in the library's internal state.
  - `i` (tcp::endpoint const&): The endpoint (IP address and port) of the peer that triggered the alert.
  - `pi` (peer_id const&): The peer ID of the peer that triggered the alert. This is a unique identifier for the peer in the torrent network.
- **Return Value**: This function returns an instance of the `peer_alert` class. The returned object contains the peer-related information and can be used to determine the type of peer event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the peer endpoint is malformed.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle and peer endpoint
auto peer_alert_instance = peer_alert(alloc, torrent_handle, tcp::endpoint("192.168.1.1", 6881), peer_id("ABC123"));
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `i` and `pi` parameters must be valid peer endpoint and peer ID, respectively.
- **Postconditions**: The returned `peer_alert` object is valid and contains the provided information about the peer event.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `peer_connect_alert`, `peer_disconnect_alert`, `peer_error_alert`

## tracker_alert

- **Signature**: `auto tracker_alert()`
- **Description**: This alert is generated when a tracker-related event occurs in the torrent client. It serves as a base class for more specific tracker alerts. This alert contains information about the tracker that triggered the event, including the torrent handle, tracker endpoint, and URL.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the tracker is associated with. This handle is used to identify the torrent in the library's internal state.
  - `ep` (tcp::endpoint const&): The endpoint (IP address and port) of the tracker that triggered the alert.
  - `u` (string_view): The URL of the tracker that triggered the alert.
- **Return Value**: This function returns an instance of the `tracker_alert` class. The returned object contains the tracker-related information and can be used to determine the type of tracker event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the tracker endpoint is malformed.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle and tracker endpoint
auto tracker_alert_instance = tracker_alert(alloc, torrent_handle, tcp::endpoint("192.168.1.1", 80), "http://example.com/announce");
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `ep` and `u` parameters must be valid tracker endpoint and URL, respectively.
- **Postconditions**: The returned `tracker_alert` object is valid and contains the provided information about the tracker event.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `tracker_error_alert`, `tracker_warning_alert`, `tracker_reply_alert`

## torrent_added_alert

- **Signature**: `auto torrent_added_alert()`
- **Description**: This alert is generated when a new torrent is added to the torrent client. It provides information about the torrent that was added, including the torrent handle.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that was added. This handle is used to identify the torrent in the library's internal state.
- **Return Value**: This function returns an instance of the `torrent_added_alert` class. The returned object contains the torrent-related information and can be used to determine the type of torrent event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle
auto torrent_added_alert_instance = torrent_added_alert(alloc, torrent_handle);
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, and the `h` parameter must be a valid torrent handle.
- **Postconditions**: The returned `torrent_added_alert` object is valid and contains the provided information about the torrent that was added.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `torrent_removed_alert`, `add_torrent_alert`

## torrent_removed_alert

- **Signature**: `auto torrent_removed_alert()`
- **Description**: This alert is generated when a torrent is removed from the torrent client. It provides information about the torrent that was removed, including the torrent handle, info hash, and user data.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that was removed. This handle is used to identify the torrent in the library's internal state.
  - `ih` (info_hash_t const&): The info hash of the torrent that was removed. This hash is used to uniquely identify the torrent in the torrent network.
  - `userdata` (client_data_t): User data associated with the torrent that was removed. This data can be used to store additional information about the torrent.
- **Return Value**: This function returns an instance of the `torrent_removed_alert` class. The returned object contains the torrent-related information and can be used to determine the type of torrent event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the info hash is malformed.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle, info hash, and user data
auto torrent_removed_alert_instance = torrent_removed_alert(alloc, torrent_handle, info_hash_t("ABC123"), client_data_t("MyTorrent"));
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `ih` parameter must be a valid info hash.
- **Postconditions**: The returned `torrent_removed_alert` object is valid and contains the provided information about the torrent that was removed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `torrent_added_alert`, `torrent_deleted_alert`

## read_piece_alert

- **Signature**: `auto read_piece_alert()`
- **Description**: This alert is generated when a piece of a torrent is read from the disk. It provides information about the piece that was read, including the piece index, the data read, and the size of the data.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the piece belongs to. This handle is used to identify the torrent in the library's internal state.
  - `p` (piece_index_t): The index of the piece that was read.
  - `d` (boost::shared_array<char>): A shared array containing the data of the piece that was read.
  - `s` (int): The size of the data in the shared array.
- **Return Value**: This function returns an instance of the `read_piece_alert` class. The returned object contains the piece-related information and can be used to determine the type of piece event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the piece index is out of range.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle, piece index, and data
auto read_piece_alert_instance = read_piece_alert(alloc, torrent_handle, piece_index_t(0), boost::shared_array<char>(new char[1024]), 1024);
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, the `p` parameter must be a valid piece index, and the `d` and `s` parameters must be valid data and size, respectively.
- **Postconditions**: The returned `read_piece_alert` object is valid and contains the provided information about the piece that was read.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `piece_finished_alert`, `block_finished_alert`

## file_completed_alert

- **Signature**: `auto file_completed_alert()`
- **Description**: This alert is generated when a file within a torrent is completed. It provides information about the file that was completed, including the file index.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the file belongs to. This handle is used to identify the torrent in the library's internal state.
  - `idx` (file_index_t): The index of the file that was completed.
- **Return Value**: This function returns an instance of the `file_completed_alert` class. The returned object contains the file-related information and can be used to determine the type of file event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the file index is out of range.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle and file index
auto file_completed_alert_instance = file_completed_alert(alloc, torrent_handle, file_index_t(0));
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `idx` parameter must be a valid file index.
- **Postconditions**: The returned `file_completed_alert` object is valid and contains the provided information about the file that was completed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `file_renamed_alert`, `file_rename_failed_alert`

## file_renamed_alert

- **Signature**: `auto file_renamed_alert()`
- **Description**: This alert is generated when a file within a torrent is renamed. It provides information about the file that was renamed, including the new name, old name, and file index.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the file belongs to. This handle is used to identify the torrent in the library's internal state.
  - `n` (string_view): The new name of the file.
  - `old` (string_view): The old name of the file.
  - `idx` (file_index_t): The index of the file that was renamed.
- **Return Value**: This function returns an instance of the `file_renamed_alert` class. The returned object contains the file-related information and can be used to determine the type of file event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the file index is out of range.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle, new name, old name, and file index
auto file_renamed_alert_instance = file_renamed_alert(alloc, torrent_handle, "new_name.txt", "old_name.txt", file_index_t(0));
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `idx` parameter must be a valid file index.
- **Postconditions**: The returned `file_renamed_alert` object is valid and contains the provided information about the file that was renamed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `file_completed_alert`, `file_rename_failed_alert`

## file_rename_failed_alert

- **Signature**: `auto file_rename_failed_alert()`
- **Description**: This alert is generated when a file within a torrent fails to be renamed. It provides information about the file that failed to be renamed, including the error code, file index, and user data.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the file belongs to. This handle is used to identify the torrent in the library's internal state.
  - `idx` (file_index_t): The index of the file that failed to be renamed.
  - `ec` (error_code): The error code that indicates why the rename operation failed.
- **Return Value**: This function returns an instance of the `file_rename_failed_alert` class. The returned object contains the file-related information and can be used to determine the type of file event that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the file index is out of range.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle, file index, and error code
auto file_rename_failed_alert_instance = file_rename_failed_alert(alloc, torrent_handle, file_index_t(0), error_code(1, boost::system::generic_category()));
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `idx` parameter must be a valid file index.
- **Postconditions**: The returned `file_rename_failed_alert` object is valid and contains the provided information about the file that failed to be renamed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `file_renamed_alert`, `file_error_alert`

## setting

- **Signature**: `auto setting()`
- **Description**: This alert is generated when a performance warning occurs in the torrent client. It provides information about the performance warning, including the type of warning and the current performance settings.
- **Parameters**:
  - `alloc` (aux::stack_allocator&): Allocator used for constructing the alert. This is typically used internally by the library to manage memory allocation efficiently.
  - `h` (torrent_handle const&): The handle to the torrent that the performance warning is associated with. This handle is used to identify the torrent in the library's internal state.
  - `st` (torrent_status::state_t): The current state of the torrent.
  - `prev_st` (torrent_status::state_t): The previous state of the torrent.
- **Return Value**: This function returns an instance of the `performance_alert` class. The returned object contains the performance-related information and can be used to determine the type of performance warning that occurred.
- **Exceptions/Errors**: This function does not throw exceptions. However, it may fail if the provided parameters are invalid, such as if the torrent handle is invalid or if the state is not a valid torrent status.
- **Example**:
```cpp
// This example assumes that you have a valid torrent handle and states
auto performance_alert_instance = performance_alert(alloc, torrent_handle, torrent_status::state_t::downloading, torrent_status::state_t::seeding);
```
- **Preconditions**: The `alloc` parameter must be a valid stack allocator, the `h` parameter must be a valid torrent handle, and the `st` and `prev_st` parameters must be valid torrent states.
- **Postconditions**: The returned `performance_alert` object is valid and contains the provided information about the performance warning.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: The time and space complexity are constant, O(1), as it involves simple memory allocation and object construction.
- **See Also**: `state_changed_alert`, `torrent_error_alert`

##