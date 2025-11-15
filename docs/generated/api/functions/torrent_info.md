# libtorrent Python Bindings API Documentation

## Function: begin_trackers

- **Signature**: `std::vector<announce_entry>::const_iterator begin_trackers(torrent_info& i)`
- **Description**: Returns an iterator pointing to the first tracker entry in the torrent info object. This iterator can be used to traverse all trackers in the torrent.
- **Parameters**:
  - `i` (torrent_info&): The torrent info object whose trackers should be iterated over.
- **Return Value**:
  - `std::vector<announce_entry>::const_iterator`: Iterator pointing to the first tracker entry. If the torrent has no trackers, this will point to the end of the tracker list.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```cpp
auto it = begin_trackers(torrent);
while (it != end_trackers(torrent)) {
    // Process tracker *it
    ++it;
}
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned iterator is valid and can be used to traverse the tracker list.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `end_trackers()`, `torrent_info::trackers()`

## Function: end_trackers

- **Signature**: `std::vector<announce_entry>::const_iterator end_trackers(torrent_info& i)`
- **Description**: Returns an iterator pointing to the end of the tracker list in the torrent info object. This iterator is used to terminate iteration through trackers.
- **Parameters**:
  - `i` (torrent_info&): The torrent info object whose trackers should be iterated over.
- **Return Value**:
  - `std::vector<announce_entry>::const_iterator`: Iterator pointing to the end of the tracker list.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```cpp
auto it = begin_trackers(torrent);
auto end = end_trackers(torrent);
while (it != end) {
    // Process tracker *it
    ++it;
}
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned iterator is valid and can be used to check the end of the tracker list.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `begin_trackers()`, `torrent_info::trackers()`

## Function: add_node

- **Signature**: `void add_node(torrent_info& ti, char const* hostname, int port)`
- **Description**: Adds a node to the torrent's DHT node list. This node will be used for DHT lookups and peer connections.
- **Parameters**:
  - `ti` (torrent_info&): The torrent info object to add the node to.
  - `hostname` (char const*): The hostname or IP address of the node to add. Must be a null-terminated string.
  - `port` (int): The port number of the node to add. Must be between 0 and 65535.
- **Return Value**:
  - `void`: This function returns no value.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```cpp
add_node(torrent, "dht.example.com", 6881);
```
- **Preconditions**: The `torrent_info` object must be valid and initialized. The hostname must be a valid string.
- **Postconditions**: The specified node is added to the torrent's DHT node list.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `nodes()`

## Function: nodes

- **Signature**: `list nodes(torrent_info const& ti)`
- **Description**: Returns a list of all nodes associated with the torrent. Each node is represented as a tuple of (hostname, port).
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object whose nodes should be retrieved.
- **Return Value**:
  - `list`: A Python list of tuples, where each tuple contains (hostname, port) for a node.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
nodes_list = nodes(torrent)
for hostname, port in nodes_list:
    print(f"Node: {hostname}:{port}")
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned list contains all nodes associated with the torrent.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(n) time complexity, where n is the number of nodes.
- **See Also**: `add_node()`

## Function: get_web_seeds

- **Signature**: `list get_web_seeds(torrent_info const& ti)`
- **Description**: Returns a list of all web seeds associated with the torrent. Web seeds are HTTP/HTTPS URLs that can be used to download torrent pieces.
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object whose web seeds should be retrieved.
- **Return Value**:
  - `list`: A Python list of dictionaries, where each dictionary represents a web seed with keys "url" and "type".
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
web_seeds = get_web_seeds(torrent)
for seed in web_seeds:
    print(f"URL: {seed['url']}, Type: {seed['type']}")
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned list contains all web seeds associated with the torrent.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(n) time complexity, where n is the number of web seeds.
- **See Also**: `set_web_seeds()`

## Function: set_web_seeds

- **Signature**: `void set_web_seeds(torrent_info& ti, list ws)`
- **Description**: Sets the web seeds for the torrent. This function replaces all existing web seeds with the provided list.
- **Parameters**:
  - `ti` (torrent_info&): The torrent info object whose web seeds should be set.
  - `ws` (list): A Python list of dictionaries, where each dictionary represents a web seed with keys "url" and "type".
- **Return Value**:
  - `void`: This function returns no value.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
web_seeds = [{"url": "http://example.com/file", "type": 1}]
set_web_seeds(torrent, web_seeds)
```
- **Preconditions**: The `torrent_info` object must be valid and initialized. The `ws` list must contain valid web seed dictionaries.
- **Postconditions**: All existing web seeds are replaced with the provided web seeds.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(n) time complexity, where n is the number of web seeds.
- **See Also**: `get_web_seeds()`

## Function: get_merkle_tree

- **Signature**: `list get_merkle_tree(torrent_info const& ti)`
- **Description**: Returns the Merkle tree for the torrent. The Merkle tree is used for piece verification in torrent files with Merkle hashing.
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object whose Merkle tree should be retrieved.
- **Return Value**:
  - `list`: A Python list of byte strings, where each byte string represents a SHA-1 hash in the Merkle tree.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
merkle_tree = get_merkle_tree(torrent)
for hash in merkle_tree:
    print(f"Hash: {hash.hex()}")
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned list contains all hashes in the Merkle tree.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(n) time complexity, where n is the number of hashes in the Merkle tree.
- **See Also**: `set_merkle_tree()`

## Function: set_merkle_tree

- **Signature**: `void set_merkle_tree(torrent_info& ti, list hashes)`
- **Description**: Sets the Merkle tree for the torrent. This function replaces the existing Merkle tree with the provided list of hashes.
- **Parameters**:
  - `ti` (torrent_info&): The torrent info object whose Merkle tree should be set.
  - `hashes` (list): A Python list of byte strings, where each byte string represents a SHA-1 hash.
- **Return Value**:
  - `void`: This function returns no value.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
merkle_tree = [b'\x00' * 20, b'\x01' * 20]  # Example hashes
set_merkle_tree(torrent, merkle_tree)
```
- **Preconditions**: The `torrent_info` object must be valid and initialized. The `hashes` list must contain valid SHA-1 hashes.
- **Postconditions**: The Merkle tree is replaced with the provided hashes.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(n) time complexity, where n is the number of hashes.
- **See Also**: `get_merkle_tree()`

## Function: hash_for_piece

- **Signature**: `bytes hash_for_piece(torrent_info const& ti, piece_index_t i)`
- **Description**: Returns the hash for a specific piece in the torrent. This hash is used to verify the integrity of the piece data.
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object from which to get the piece hash.
  - `i` (piece_index_t): The index of the piece whose hash should be retrieved. Must be a valid piece index.
- **Return Value**:
  - `bytes`: A byte string representing the SHA-1 hash of the piece.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
piece_hash = hash_for_piece(torrent, 0)
print(f"Hash for piece 0: {piece_hash.hex()}")
```
- **Preconditions**: The `torrent_info` object must be valid and initialized. The piece index must be within valid bounds.
- **Postconditions**: The returned hash corresponds to the specified piece index.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `torrent_info::hash_for_piece()`

## Function: metadata

- **Signature**: `bytes metadata(torrent_info const& ti)`
- **Description**: Returns the entire metadata section of the torrent as a byte string. This includes the info dictionary and other metadata.
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object whose metadata should be retrieved.
- **Return Value**:
  - `bytes`: A byte string containing the entire metadata section of the torrent.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
metadata_bytes = metadata(torrent)
# Process the metadata bytes as needed
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned byte string contains the complete metadata section.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `get_info_section()`

## Function: get_info_section

- **Signature**: `bytes get_info_section(torrent_info const& ti)`
- **Description**: Returns the info section of the torrent as a byte string. This is the core part of the torrent metadata that contains file information.
- **Parameters**:
  - `ti` (torrent_info const&): The torrent info object whose info section should be retrieved.
- **Return Value**:
  - `bytes`: A byte string containing the info section of the torrent.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
info_section = get_info_section(torrent)
# Process the info section as needed
```
- **Preconditions**: The `torrent_info` object must be valid and initialized.
- **Postconditions**: The returned byte string contains the info section of the torrent.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `metadata()`

## Function: map_block

- **Signature**: `list map_block(torrent_info& ti, piece_index_t piece, std::int64_t offset, int size)`
- **Description**: Maps a block of data from a piece to the underlying file system. This function returns a list of file slices that describe how the block is mapped to files.
- **Parameters**:
  - `ti` (torrent_info&): The torrent info object to map the block from.
  - `piece` (piece_index_t): The index of the piece containing the block.
  - `offset` (std::int64_t): The offset within the piece where the block starts.
  - `size` (int): The size of the block in bytes.
- **Return Value**:
  - `list`: A Python list of file_slice objects describing the mapping.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```python
slices = map_block(torrent, 0, 0, 1024)
for slice in slices:
    print(f"File: {slice.file_index}, Offset: {slice.offset}, Size: {slice.size}")
```
- **Preconditions**: The `torrent_info` object must be valid and initialized. The piece index must be valid, and the offset and size must be within bounds.
- **Postconditions**: The returned list contains all file slices that correspond to the requested block.
- **Thread Safety**: Thread-safe as long as the torrent_info object is not modified concurrently.
- **Complexity**: O(k) time complexity, where k is the number of file slices in the result.
- **See Also**: `torrent_info::map_block()`

## Function: get_next_announce

- **Signature**: `lt::time_point get_next_announce(announce_entry const& ae)`
- **Description**: Returns the next announce time for the given announce entry. This function is deprecated and should not be used.
- **Parameters**:
  - `ae` (announce_entry const&): The announce entry whose next announce time should be retrieved.
- **Return Value**:
  - `lt::time_point`: The next announce time, or a default-constructed time_point if no endpoints are available.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```cpp
// This function is deprecated and should not be used
lt::time_point next_announce = get_next_announce(entry);
```
- **Preconditions**: The `announce_entry` object must be valid and initialized.
- **Postconditions**: The returned time_point represents the next announce time.
- **Thread Safety**: Thread-safe as long as the announce_entry object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `get_min_announce()`, `can_announce()`, `is_working()`, `get_source()`, `get_verified()`, `get_message()`, `get_last_error()`, `get_scrape_incomplete()`, `get_scrape_complete()`, `get_scrape_downloaded()`, `next_announce_in()`, `min_announce_in()`, `get_send_stats()`

## Function: get_min_announce

- **Signature**: `lt::time_point get_min_announce(announce_entry const& ae)`
- **Description**: Returns the minimum announce time for the given announce entry. This function is deprecated and should not be used.
- **Parameters**:
  - `ae` (announce_entry const&): The announce entry whose minimum announce time should be retrieved.
- **Return Value**:
  - `lt::time_point`: The minimum announce time, or a default-constructed time_point if no endpoints are available.
- **Exceptions/Errors**:
  - None - this function does not throw exceptions.
- **Example**:
```cpp
// This function is deprecated and should not be used
lt::time_point min_announce = get_min_announce(entry);
```
- **Preconditions**: The `announce_entry` object must be valid and initialized.
- **Postconditions**: The returned time_point represents the minimum announce time.
- **Thread Safety**: Thread-safe as long as the announce_entry object is not modified concurrently.
- **Complexity**: O(1) time complexity.
- **See Also**: `get_next_announce()`, `can_announce()`, `is_working()`, `get_source()`, `get_verified()`, `get_message()`, `get_last_error()`, `get_scrape_incomplete()`, `get_scrape_complete()`, `get_scrape_downloaded()`, `next_announce_in()`, `min_announce_in()`, `get_send_stats()`

## Function: get_fails

- **Signature**: `int get_fails(announce_entry const& ae)`
- **Description**: Returns the number of failed announcements for the given announce entry. This function is deprecated and should not be used.
- **Parameters**:
  - `ae` (announce_entry const&): The announce entry whose failed count should be retrieved.
- **Return Value**:
  - `int`: The number of failed announcements, or 0 if no endpoints are