# libtorrent Python Bindings API Documentation

## url_seeds

- **Signature**: `list url_seeds(torrent_handle& handle)`
- **Description**: Retrieves the list of URL seeds currently associated with the torrent. URL seeds are alternative sources for torrent data, often used for faster downloads or to bypass tracker limitations.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing all URL seeds as strings.
  - Empty list if no URL seeds are configured.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
seeds = url_seeds(torrent_handle)
for seed in seeds:
    print(f"URL Seed: {seed}")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of URL seeds, or an empty list if none are configured.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of URL seeds.
- **See Also**: `http_seeds()`, `trackers()`

## http_seeds

- **Signature**: `list http_seeds(torrent_handle& handle)`
- **Description**: Retrieves the list of HTTP seeds currently associated with the torrent. HTTP seeds allow torrents to download data from traditional web servers.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing all HTTP seeds as strings.
  - Empty list if no HTTP seeds are configured.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
http_seeds_list = http_seeds(torrent_handle)
for seed in http_seeds_list:
    print(f"HTTP Seed: {seed}")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of HTTP seeds, or an empty list if none are configured.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of HTTP seeds.
- **See Also**: `url_seeds()`, `trackers()`

## piece_availability

- **Signature**: `list piece_availability(torrent_handle& handle)`
- **Description**: Retrieves the availability status of each piece in the torrent. This indicates how many peers have each piece, which helps determine download progress and quality.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing the availability count for each piece in the torrent.
  - The list is ordered by piece index, with availability counts indicating how many peers have each piece.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
availability = piece_availability(torrent_handle)
for i, count in enumerate(availability):
    print(f"Piece {i}: {count} peers")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of availability counts for each piece in the torrent.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of pieces in the torrent.
- **See Also**: `piece_priorities()`, `get_download_queue()`

## piece_priorities

- **Signature**: `list piece_priorities(torrent_handle& handle)`
- **Description**: Retrieves the download priorities for each piece in the torrent. This indicates which pieces the client should prioritize when downloading.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing the download priority for each piece in the torrent.
  - The list is ordered by piece index, with priority values indicating download priority.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
priorities = piece_priorities(torrent_handle)
for i, priority in enumerate(priorities):
    print(f"Piece {i}: Priority {priority}")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of download priorities for each piece in the torrent.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of pieces in the torrent.
- **See Also**: `file_priorities()`, `prioritize_pieces()`

## file_progress

- **Signature**: `list file_progress(torrent_handle& handle, file_progress_flags_t const flags)`
- **Description**: Retrieves the download progress for each file in the torrent. This function provides information about how much of each file has been downloaded.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
  - `flags` (file_progress_flags_t const): Flags controlling the behavior of the function (e.g., whether to include file sizes, partial progress, etc.).
- **Return Value**: 
  - `list`: A Python list containing the download progress for each file in the torrent.
  - The list is ordered by file index, with progress values indicating download completion.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
progress = file_progress(torrent_handle, file_progress_flags_t.NORMAL)
for i, progress in enumerate(progress):
    print(f"File {i}: {progress}% complete")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of file progress values for each file in the torrent.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of files in the torrent.
- **See Also**: `file_priorities()`, `get_torrent_info()`

## get_peer_info

- **Signature**: `list get_peer_info(torrent_handle const& handle)`
- **Description**: Retrieves information about all peers currently connected to the torrent. This includes connection status, upload/download rates, and other metrics.
- **Parameters**:
  - `handle` (torrent_handle const&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing `peer_info` objects for each connected peer.
  - Each `peer_info` object contains detailed information about a peer's connection and transfer statistics.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
peers = get_peer_info(torrent_handle)
for peer in peers:
    print(f"Peer: {peer.ip}, Upload: {peer.upload_rate}, Download: {peer.download_rate}")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of peer information objects for all connected peers.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of connected peers.
- **See Also**: `get_download_queue()`, `trackers()`

## extract_fn

- **Signature**: `T extract_fn(object o)`
- **Description**: Extracts a value from a Python object using boost::python's extraction mechanism. This is a generic template function for type-safe extraction.
- **Parameters**:
  - `o` (object): The Python object to extract from.
- **Return Value**: 
  - `T`: The extracted value of type T from the Python object.
  - The type T must be compatible with boost::python's extraction mechanism.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the extraction fails due to type mismatch.
- **Example**:
```python
value = extract_fn<int>(python_object)
```
- **Preconditions**: The Python object must be of a type that can be extracted to the target type T.
- **Postconditions**: Returns the extracted value of type T.
- **Thread Safety**: Thread-safe if the Python interpreter is properly thread-safe.
- **Complexity**: O(1) - the extraction process is typically constant time.
- **See Also**: `dict_to_announce_entry()`, `add_tracker()`

## prioritize_pieces

- **Signature**: `void prioritize_pieces(torrent_handle& info, object o)`
- **Description**: Sets the download priorities for pieces in a torrent. This function allows users to specify which pieces should be downloaded first.
- **Parameters**:
  - `info` (torrent_handle&): Reference to the torrent handle object representing the torrent to modify.
  - `o` (object): Python object containing the priority information, which can be either a list of priorities or a list of piece -> priority mappings.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the input object cannot be processed.
  - `std::out_of_range`: Thrown if the piece index in the mappings is invalid.
- **Example**:
```python
prioritize_pieces(torrent_handle, [1, 0, 1, 1])  # Prioritize first 4 pieces
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: The piece priorities have been updated according to the input.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of pieces to prioritize.
- **See Also**: `prioritize_files()`, `piece_priorities()`

## prioritize_files

- **Signature**: `void prioritize_files(torrent_handle& info, object o)`
- **Description**: Sets the download priorities for files in a torrent. This function allows users to specify which files should be downloaded first.
- **Parameters**:
  - `info` (torrent_handle&): Reference to the torrent handle object representing the torrent to modify.
  - `o` (object): Python object containing the priority information as a list of download_priority_t values.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the input object cannot be processed.
  - `std::out_of_range`: Thrown if the file index in the mappings is invalid.
- **Example**:
```python
prioritize_files(torrent_handle, [high_priority, normal_priority, low_priority])
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: The file priorities have been updated according to the input.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of files in the torrent.
- **See Also**: `file_priorities()`, `file_priority0()`

## file_priorities

- **Signature**: `list file_priorities(torrent_handle& handle)`
- **Description**: Retrieves the download priorities for each file in the torrent. This indicates which files the client should prioritize when downloading.
- **Parameters**:
  - `handle` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
- **Return Value**: 
  - `list`: A Python list containing the download priority for each file in the torrent.
  - The list is ordered by file index, with priority values indicating download priority.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
priorities = file_priorities(torrent_handle)
for i, priority in enumerate(priorities):
    print(f"File {i}: Priority {priority}")
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns a list of download priorities for each file in the torrent.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of files in the torrent.
- **See Also**: `prioritize_files()`, `file_priority0()`

## file_priority0

- **Signature**: `download_priority_t file_priority0(torrent_handle& h, file_index_t index)`
- **Description**: Retrieves the download priority for a specific file in the torrent.
- **Parameters**:
  - `h` (torrent_handle&): Reference to the torrent handle object representing the torrent to query.
  - `index` (file_index_t): The index of the file whose priority should be retrieved.
- **Return Value**: 
  - `download_priority_t`: The download priority of the specified file.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
priority = file_priority0(torrent_handle, 0)  # Get priority of first file
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: Returns the download priority of the specified file.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(1) - constant time lookup.
- **See Also**: `file_priority1()`, `file_priorities()`

## file_priority1

- **Signature**: `void file_priority1(torrent_handle& h, file_index_t index, download_priority_t prio)`
- **Description**: Sets the download priority for a specific file in the torrent.
- **Parameters**:
  - `h` (torrent_handle&): Reference to the torrent handle object representing the torrent to modify.
  - `index` (file_index_t): The index of the file whose priority should be set.
  - `prio` (download_priority_t): The new download priority for the file.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - None explicitly thrown, but may throw exceptions from the underlying libtorrent library.
- **Example**:
```python
file_priority1(torrent_handle, 0, high_priority)  # Set first file to high priority
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: The download priority of the specified file has been updated.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(1) - constant time update.
- **See Also**: `file_priority0()`, `prioritize_files()`

## dict_to_announce_entry

- **Signature**: `void dict_to_announce_entry(dict d, announce_entry& ae)`
- **Description**: Converts a Python dictionary to an announce_entry structure used by libtorrent for tracker announcements.
- **Parameters**:
  - `d` (dict): Python dictionary containing tracker information.
  - `ae` (announce_entry&): Reference to the announce_entry structure to populate.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the dictionary contains invalid or missing keys.
- **Example**:
```python
tracker_dict = {"url": "http://example.com/announce", "tier": 0}
announce_entry entry;
dict_to_announce_entry(tracker_dict, entry);
```
- **Preconditions**: The dictionary must contain at least a "url" key.
- **Postconditions**: The announce_entry structure is populated with the values from the dictionary.
- **Thread Safety**: Not thread-safe as it modifies the announce_entry structure.
- **Complexity**: O(1) - constant time for dictionary processing.
- **See Also**: `add_tracker()`, `replace_trackers()`

## replace_trackers

- **Signature**: `void replace_trackers(torrent_handle& h, object trackers)`
- **Description**: Replaces all current trackers for a torrent with a new list of trackers.
- **Parameters**:
  - `h` (torrent_handle&): Reference to the torrent handle object representing the torrent to modify.
  - `trackers` (object): Python object containing the new list of trackers, which can be a list or iterable of dictionaries.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the input object cannot be processed.
  - `std::invalid_argument`: Thrown if the trackers list contains invalid entries.
- **Example**:
```python
trackers = [{"url": "http://tracker1.com", "tier": 0}, {"url": "http://tracker2.com", "tier": 1}]
replace_trackers(torrent_handle, trackers)
```
- **Preconditions**: The torrent handle must be valid and associated with an active torrent.
- **Postconditions**: All trackers for the torrent have been replaced with the new list.
- **Thread Safety**: Thread-safe due to the `allow_threading_guard` usage.
- **Complexity**: O(n) where n is the number of trackers to replace.
- **See Also**: `add_tracker()`, `trackers()`

## add_tracker

- **Signature**: `void add_tracker(torrent_handle& h, dict d)`
- **Description**: Adds a new tracker to the torrent's list of trackers.
- **Parameters**:
  - `h` (torrent_handle&): Reference to the torrent handle object representing the torrent to modify.
  - `d` (dict): Python dictionary containing the tracker information.
- **Return Value**: 
  - `void`: No return value.
- **Exceptions/Errors**:
  - `boost::python::error_already_set`: Thrown if the dictionary contains invalid or missing keys.
  - `std::invalid_argument`: Thrown if the tracker URL is invalid.
- **Example**:
```python
tracker = {"url": "http://newtracker.com", "