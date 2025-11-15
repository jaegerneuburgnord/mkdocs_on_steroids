# API Documentation for create_torrent.cpp

## set_hash

- **Signature**: `void set_hash(create_torrent& c, piece_index_t p, bytes const& b)`
- **Description**: Sets the SHA-1 hash for a specific piece in the create_torrent object. This function is used to manually specify the hash of a piece in the torrent file.
- **Parameters**:
  - `c` (create_torrent&): Reference to the create_torrent object where the piece hash will be set.
  - `p` (piece_index_t): The index of the piece whose hash is being set.
  - `b` (bytes const&): The SHA-1 hash bytes for the piece, represented as a bytes object.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. However, the `create_torrent::set_hash` method might throw if the piece index is invalid.
- **Example**:
```cpp
create_torrent tor;
bytes hash = get_piece_hash(0); // Assume this function returns a valid hash
set_hash(tor, piece_index_t(0), hash);
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The piece at index `p` in the `create_torrent` object will have its hash set to the value provided.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `set_file_hash`, `create_torrent::set_hash`

## set_file_hash

- **Signature**: `void set_file_hash(create_torrent& c, file_index_t f, bytes const& b)`
- **Description**: Sets the SHA-1 hash for a specific file in the create_torrent object. This function allows manual specification of file hashes.
- **Parameters**:
  - `c` (create_torrent&): Reference to the create_torrent object where the file hash will be set.
  - `f` (file_index_t): The index of the file whose hash is being set.
  - `b` (bytes const&): The SHA-1 hash bytes for the file, represented as a bytes object.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. The `create_torrent::set_file_hash` method might throw if the file index is invalid.
- **Example**:
```cpp
create_torrent tor;
bytes hash = get_file_hash(0); // Assume this function returns a valid hash
set_file_hash(tor, file_index_t(0), hash);
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The file at index `f` in the `create_torrent` object will have its hash set to the value provided.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `set_hash`, `create_torrent::set_file_hash`

## set_piece_hashes_callback

- **Signature**: `void set_piece_hashes_callback(create_torrent& c, std::string const& p, boost::python::object cb)`
- **Description**: Sets piece hashes for a create_torrent object using a callback function. The callback is invoked for each piece during the hash calculation process.
- **Parameters**:
  - `c` (create_torrent&): Reference to the create_torrent object where piece hashes will be set.
  - `p` (std::string const&): The path to the directory containing the files for which hashes are being calculated.
  - `cb` (boost::python::object): A Python object that represents the callback function to be called for each piece.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. However, the callback function may throw exceptions.
- **Example**:
```cpp
create_torrent tor;
boost::python::object callback = boost::python::make_function([](piece_index_t i) {
    std::cout << "Processing piece " << i << std::endl;
});
set_piece_hashes_callback(tor, "/path/to/files", callback);
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The piece hashes for the files in the specified directory will be calculated and set in the `create_torrent` object.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(n) time complexity, where n is the number of pieces, O(1) space complexity.
- **See Also**: `set_piece_hashes`, `set_piece_hashes_callback`

## set_piece_hashes_callback (overloaded)

- **Signature**: `void set_piece_hashes_callback(create_torrent& c, std::string const& p, boost::python::object cb)`
- **Description**: Sets piece hashes for a create_torrent object using a callback function with error handling. The callback is invoked for each piece during the hash calculation process.
- **Parameters**:
  - `c` (create_torrent&): Reference to the create_torrent object where piece hashes will be set.
  - `p` (std::string const&): The path to the directory containing the files for which hashes are being calculated.
  - `cb` (boost::python::object): A Python object that represents the callback function to be called for each piece.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. However, the callback function may throw exceptions.
- **Example**:
```cpp
create_torrent tor;
boost::python::object callback = boost::python::make_function([](piece_index_t i) {
    std::cout << "Processing piece " << i << std::endl;
});
error_code ec;
set_piece_hashes_callback(tor, "/path/to/files", callback, ec);
if (ec) {
    std::cerr << "Error setting piece hashes: " << ec.message() << std::endl;
}
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The piece hashes for the files in the specified directory will be calculated and set in the `create_torrent` object.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(n) time complexity, where n is the number of pieces, O(1) space complexity.
- **See Also**: `set_piece_hashes`, `set_piece_hashes_callback`

## set_piece_hashes0

- **Signature**: `void set_piece_hashes0(create_torrent& c, std::string const & s)`
- **Description**: Sets piece hashes for a create_torrent object using a specified path. This function uses a default callback and error code.
- **Parameters**:
  - `c` (create_torrent&): Reference to the create_torrent object where piece hashes will be set.
  - `s` (std::string const&): The path to the directory containing the files for which hashes are being calculated.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. However, the underlying `set_piece_hashes` function may throw exceptions.
- **Example**:
```cpp
create_torrent tor;
set_piece_hashes0(tor, "/path/to/files");
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The piece hashes for the files in the specified directory will be calculated and set in the `create_torrent` object.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(n) time complexity, where n is the number of pieces, O(1) space complexity.
- **See Also**: `set_piece_hashes`, `set_piece_hashes_callback`

## add_node

- **Signature**: `void add_node(create_torrent& ct, std::string const& addr, int port)`
- **Description**: Adds a node to the create_torrent object's list of nodes. This function is used to specify additional nodes for the torrent.
- **Parameters**:
  - `ct` (create_torrent&): Reference to the create_torrent object where the node will be added.
  - `addr` (std::string const&): The IP address of the node.
  - `port` (int): The port number of the node.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function. However, the `create_torrent::add_node` method may throw exceptions if the address or port is invalid.
- **Example**:
```cpp
create_torrent tor;
add_node(tor, "192.168.1.1", 6881);
```
- **Preconditions**: The `create_torrent` object must be valid and initialized.
- **Postconditions**: The node with the specified address and port will be added to the `create_torrent` object's list of nodes.
- **Thread Safety**: Thread-safe if the `create_torrent` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `create_torrent::add_node`

## add_file_deprecated

- **Signature**: `void add_file_deprecated(file_storage& ct, file_entry const& fe)`
- **Description**: Adds a file entry to the file storage, but this overload is deprecated. Use `add_file` instead.
- **Parameters**:
  - `ct` (file_storage&): Reference to the file storage object where the file entry will be added.
  - `fe` (file_entry const&): The file entry to be added.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
file_storage fs;
file_entry fe;
// Initialize fe with appropriate values
add_file_deprecated(fs, fe);
```
- **Preconditions**: The `file_storage` object must be valid and initialized.
- **Postconditions**: The file entry will be added to the file storage object.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `add_file`, `file_storage::add_file`

## FileIter

- **Signature**: `FileIter(file_storage const& fs, file_index_t i)`
- **Description**: Constructor for the FileIter class. Creates an iterator for files in the file storage.
- **Parameters**:
  - `fs` (file_storage const&): Reference to the file storage object.
  - `i` (file_index_t): The index of the file to start iteration from.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
file_storage fs;
FileIter iter(fs, file_index_t(0));
```
- **Preconditions**: The `file_storage` object must be valid and initialized.
- **Postconditions**: A FileIter object is created that can be used to iterate over files in the file storage.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `begin_files`, `end_files`

## FileIter (copy constructor)

- **Signature**: `FileIter(FileIter const&) = default`
- **Description**: Copy constructor for the FileIter class. Creates a copy of an existing FileIter object.
- **Parameters**: 
  - `rhs` (FileIter const&): The FileIter object to be copied.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
FileIter iter1(fs, file_index_t(0));
FileIter iter2 = iter1;
```
- **Preconditions**: The `FileIter` object must be valid.
- **Postconditions**: A new FileIter object is created that is a copy of the original.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `FileIter`, `operator++`

## FileIter (default constructor)

- **Signature**: `FileIter()`
- **Description**: Default constructor for the FileIter class. Creates an empty FileIter object.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
FileIter iter;
```
- **Preconditions**: None.
- **Postconditions**: A FileIter object is created with default values.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `FileIter`, `begin_files`

## at

- **Signature**: `lt::file_entry operator*() const`
- **Description**: Dereferences the FileIter iterator to return the current file entry.
- **Parameters**: None.
- **Return Value**: Returns the file entry at the current iterator position.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
FileIter iter(fs, file_index_t(0));
lt::file_entry file = *iter;
```
- **Preconditions**: The iterator must not be at the end of the file storage.
- **Postconditions**: The file entry at the current iterator position is returned.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `begin_files`, `end_files`

## FileIter (post-increment)

- **Signature**: `FileIter operator++(int)`
- **Description**: Post-increment operator for the FileIter class. Advances the iterator to the next file.
- **Parameters**: 
  - `int`: Dummy parameter to distinguish from pre-increment.
- **Return Value**: Returns a copy of the iterator before incrementing.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
FileIter iter(fs, file_index_t(0));
FileIter iter2 = iter++;
```
- **Preconditions**: The iterator must not be at the end of the file storage.
- **Postconditions**: The iterator is advanced to the next file, and a copy of the original iterator is returned.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `at`, `operator-`

## assert

- **Signature**: `int operator-(FileIter const& rhs) const`
- **Description**: Subtraction operator for FileIter objects. Returns the difference in file indices between two iterators.
- **Parameters**: 
  - `rhs` (FileIter const&): The right-hand side iterator.
- **Return Value**: Returns the difference in file indices between the current iterator and the right-hand side iterator.
- **Exceptions/Errors**: Throws an assertion error if the file storage objects are different.
- **Example**:
```cpp
FileIter iter1(fs, file_index_t(0));
FileIter iter2(fs, file_index_t(5));
int diff = iter1 - iter2; // Returns -5
```
- **Preconditions**: Both iterators must point to the same file storage object.
- **Postconditions**: The difference in file indices is returned.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `FileIter`, `operator*`

## begin_files

- **Signature**: `FileIter begin_files(file_storage const& self)`
- **Description**: Returns an iterator pointing to the first file in the file storage. This function is deprecated.
- **Parameters**:
  - `self` (file_storage const&): Reference to the file storage object.
- **Return Value**: Returns a FileIter object pointing to the first file.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
file_storage fs;
FileIter iter = begin_files(fs);
```
- **Preconditions**: The `file_storage` object must be valid and initialized.
- **Postconditions**: A FileIter object is returned pointing to the first file.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `end_files`, `__iter__`

## end_files

- **Signature**: `FileIter end_files(file_storage const& self)`
- **Description**: Returns an iterator pointing to one past the last file in the file storage.
- **Parameters**:
  - `self` (file_storage const&): Reference to the file storage object.
- **Return Value**: Returns a FileIter object pointing to one past the last file.
- **Exceptions/Errors**: No exceptions are thrown by this function.
- **Example**:
```cpp
file_storage fs;
FileIter iter = end_files(fs);
```
- **Preconditions**: The `file_storage` object must be valid and initialized.
- **Postconditions**: A FileIter object is returned pointing to one past the last file.
- **Thread Safety**: Thread-safe if the `file_storage` object is not accessed by other threads simultaneously.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `begin_files`, `__iter__`

## add_files_callback

- **Signature**: `void add_files_callback(file_storage& fs, std::string const& file, boost::python::object cb, create_flags_t const flags)`
- **Description**: Adds files to a file storage object using a callback function. The callback is invoked for each file during the addition process.
- **Parameters**:
  - `fs` (file_storage&): Reference to the file storage