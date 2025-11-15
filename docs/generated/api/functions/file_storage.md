# libtorrent File Storage API Documentation

## file_entry

### Signature
```cpp
auto file_entry()
```

### Description
The `file_entry` struct represents a single file within a torrent's file storage. It contains metadata about a file, including its name, size, and location within the torrent's file structure. This struct is used internally by the `file_storage` class to represent individual files in a torrent.

### Return Value
- Returns an instance of the `file_entry` struct.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
// Creating a file_entry instance
file_entry entry;
```

### Preconditions
- None

### Postconditions
- A valid `file_entry` instance is created.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time and space complexity.

### See Also
- `file_storage`

## file_entry (copy constructor)

### Signature
```cpp
auto file_entry(file_entry const&) = default
```

### Description
Default copy constructor for the `file_entry` struct. This allows the creation of a copy of an existing `file_entry` instance.

### Parameters
- `other` (file_entry const&): The `file_entry` instance to copy.

### Return Value
- Returns a new `file_entry` instance with the same data as the source.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_entry original;
file_entry copy = original; // Uses the copy constructor
```

### Preconditions
- The source `file_entry` must be valid.

### Postconditions
- The copied `file_entry` has the same data as the original.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time and space complexity.

### See Also
- `file_entry`

## file_entry (move constructor)

### Signature
```cpp
auto file_entry(file_entry&&) noexcept = default
```

### Description
Default move constructor for the `file_entry` struct. This allows transferring ownership of resources from a temporary `file_entry` instance to a new one.

### Parameters
- `other` (file_entry&&): The temporary `file_entry` instance to move from.

### Return Value
- Returns a new `file_entry` instance with the moved resources.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_entry create_file_entry() {
    file_entry entry;
    return entry; // Move constructor is called here
}
```

### Preconditions
- The source `file_entry` must be in a valid state.

### Postconditions
- The moved-from `file_entry` is left in a valid but unspecified state.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time and space complexity.

### See Also
- `file_entry`

## file_storage

### Signature
```cpp
auto file_storage()
```

### Description
The `file_storage` class represents the complete file structure of a torrent. It contains information about all files in the torrent, including their names, sizes, and piece distribution. This class is used to manage the file layout of a torrent and is typically created during torrent creation or loading.

### Return Value
- Returns an instance of the `file_storage` class.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
// Creating a file_storage instance
file_storage storage;
```

### Preconditions
- None

### Postconditions
- A valid `file_storage` instance is created.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time and space complexity.

### See Also
- `file_entry`

## is_valid

### Signature
```cpp
auto is_valid() const
```

### Description
Checks if the `file_storage` instance is valid by verifying that the piece length is greater than zero. This is a simple validation check that ensures the storage has been properly initialized.

### Return Value
- Returns `true` if the piece length is greater than zero, `false` otherwise.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
if (storage.is_valid()) {
    // Storage is valid, proceed with operations
} else {
    // Storage is invalid, handle error
}
```

### Preconditions
- The `file_storage` instance must be initialized.

### Postconditions
- The validity state of the storage is determined.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `piece_length`

## begin

### Signature
```cpp
auto begin() const
```

### Description
Returns an iterator pointing to the first file in the storage. This method is deprecated and should be replaced with `begin_deprecated()`.

### Return Value
- Returns an iterator to the first file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.begin(); it != storage.end(); ++it) {
    // Process each file
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned iterator points to the first file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `end`, `begin_deprecated`

## end

### Signature
```cpp
auto end() const
```

### Description
Returns an iterator pointing to the position past the last file in the storage. This method is deprecated and should be replaced with `end_deprecated()`.

### Return Value
- Returns an iterator to the position past the last file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.begin(); it != storage.end(); ++it) {
    // Process each file
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned iterator points to the position past the last file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `begin`, `end_deprecated`

## rbegin

### Signature
```cpp
auto rbegin() const
```

### Description
Returns a reverse iterator pointing to the last file in the storage. This method is deprecated and should be replaced with `rbegin_deprecated()`.

### Return Value
- Returns a reverse iterator to the last file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.rbegin(); it != storage.rend(); ++it) {
    // Process files in reverse order
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned reverse iterator points to the last file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `rend`, `rbegin_deprecated`

## rend

### Signature
```cpp
auto rend() const
```

### Description
Returns a reverse iterator pointing to the position before the first file in the storage. This method is deprecated and should be replaced with `rend_deprecated()`.

### Return Value
- Returns a reverse iterator to the position before the first file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.rbegin(); it != storage.rend(); ++it) {
    // Process files in reverse order
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned reverse iterator points to the position before the first file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `rbegin`, `rend_deprecated`

## begin_deprecated

### Signature
```cpp
auto begin_deprecated() const
```

### Description
Returns an iterator pointing to the first file in the storage. This is the recommended method for iterating over files in a `file_storage` instance.

### Return Value
- Returns an iterator to the first file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.begin_deprecated(); it != storage.end_deprecated(); ++it) {
    // Process each file
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned iterator points to the first file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `end_deprecated`, `file_entry`

## end_deprecated

### Signature
```cpp
auto end_deprecated() const
```

### Description
Returns an iterator pointing to the position past the last file in the storage. This is the recommended method for iterating over files in a `file_storage` instance.

### Return Value
- Returns an iterator to the position past the last file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.begin_deprecated(); it != storage.end_deprecated(); ++it) {
    // Process each file
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned iterator points to the position past the last file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `begin_deprecated`, `file_entry`

## rbegin_deprecated

### Signature
```cpp
auto rbegin_deprecated() const
```

### Description
Returns a reverse iterator pointing to the last file in the storage. This is the recommended method for iterating over files in reverse order in a `file_storage` instance.

### Return Value
- Returns a reverse iterator to the last file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.rbegin_deprecated(); it != storage.rend_deprecated(); ++it) {
    // Process files in reverse order
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned reverse iterator points to the last file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `rend_deprecated`, `file_entry`

## rend_deprecated

### Signature
```cpp
auto rend_deprecated() const
```

### Description
Returns a reverse iterator pointing to the position before the first file in the storage. This is the recommended method for iterating over files in reverse order in a `file_storage` instance.

### Return Value
- Returns a reverse iterator to the position before the first file in the storage.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
for (auto it = storage.rbegin_deprecated(); it != storage.rend_deprecated(); ++it) {
    // Process files in reverse order
}
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The returned reverse iterator points to the position before the first file in the storage.

### Thread Safety
- Thread-safe for read-only operations.

### Complexity
- O(1) time complexity.

### See Also
- `rbegin_deprecated`, `file_entry`

## total_size

### Signature
```cpp
auto total_size() const
```

### Description
Returns the total size of all files in the torrent in bytes. This is the sum of the sizes of all individual files in the storage.

### Return Value
- Returns the total size of all files in the torrent in bytes.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
std::int64_t total = storage.total_size();
std::cout << "Total size: " << total << " bytes" << std::endl;
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The total size of all files is returned.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `file_entry::size`

## set_num_pieces

### Signature
```cpp
auto set_num_pieces(int n)
```

### Description
Sets the number of pieces in the torrent. This is used to determine how the files are divided into pieces for torrenting.

### Parameters
- `n` (int): The number of pieces to set. Must be a positive integer.

### Return Value
- None.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
storage.set_num_pieces(100); // Set 100 pieces
```

### Preconditions
- The value of `n` must be greater than 0.

### Postconditions
- The number of pieces in the storage is set to `n`.

### Thread Safety
- Thread-safe for write operations.

### Complexity
- O(1) time complexity.

### See Also
- `num_pieces`, `set_piece_length`

## num_pieces

### Signature
```cpp
auto num_pieces() const
```

### Description
Returns the number of pieces in the torrent. This is the number of pieces that the files have been divided into.

### Return Value
- Returns the number of pieces in the torrent.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
int numPieces = storage.num_pieces();
std::cout << "Number of pieces: " << numPieces << std::endl;
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The number of pieces is returned.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `set_num_pieces`, `end_piece`

## end_piece

### Signature
```cpp
auto end_piece() const
```

### Description
Returns a `piece_index_t` representing the position of the last piece plus one. This is used to iterate over pieces in the torrent.

### Return Value
- Returns a `piece_index_t` representing the position of the last piece plus one.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
piece_index_t end = storage.end_piece();
std::cout << "End piece index: " << end << std::endl;
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The end piece index is returned.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `last_piece`, `num_pieces`

## last_piece

### Signature
```cpp
auto last_piece() const
```

### Description
Returns a `piece_index_t` representing the index of the last piece in the torrent. This is used to iterate over pieces in the torrent.

### Return Value
- Returns a `piece_index_t` representing the index of the last piece in the torrent.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
piece_index_t last = storage.last_piece();
std::cout << "Last piece index: " << last << std::endl;
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The last piece index is returned.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `end_piece`, `num_pieces`

## set_piece_length

### Signature
```cpp
auto set_piece_length(int l)
```

### Description
Sets the length of each piece in the torrent. This determines how the files are divided into pieces for torrenting.

### Parameters
- `l` (int): The length of each piece in bytes. Must be a positive integer.

### Return Value
- None.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
storage.set_piece_length(1048576); // Set piece length to 1MB
```

### Preconditions
- The value of `l` must be greater than 0.

### Postconditions
- The piece length in the storage is set to `l`.

### Thread Safety
- Thread-safe for write operations.

### Complexity
- O(1) time complexity.

### See Also
- `piece_length`, `set_num_pieces`

## piece_length

### Signature
```cpp
auto piece_length() const
```

### Description
Returns the length of each piece in the torrent. This is the size of each piece in bytes.

### Return Value
- Returns the length of each piece in bytes.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
int pieceSize = storage.piece_length();
std::cout << "Piece length: " << pieceSize << " bytes" << std::endl;
```

### Preconditions
- The `file_storage` instance must be valid.

### Postconditions
- The piece length is returned.

### Thread Safety
- Thread-safe.

### Complexity
- O(1) time complexity.

### See Also
- `set_piece_length`, `is_valid`

## set_name

### Signature
```cpp
auto set_name(std::string const& n)
```

### Description
Sets the name of the torrent. This is the name that will be displayed to users and used in file naming.

### Parameters
- `n` (std::string const&): The name of the torrent. Must be a valid string.

### Return Value
- None.

### Exceptions/Errors
- No exceptions are thrown.

### Example
```cpp
file_storage storage;
storage.set_name("My Torrent");
```

### Preconditions
- The string `n` must be valid.

### Postconditions
- The name of the torrent is set to `n`.

### Thread Safety
- Thread-safe for write operations.

### Complexity
- O(1) time complexity.

### See Also
- `name`, `set_num_pieces`

## name

### Signature
```cpp
auto name() const
```

### Description
Returns the name of the torrent. This is the name that was set during torrent creation or loading.

### Return Value
- Returns the name of the torrent as a `std::string