# libtorrent Hash Picker API Documentation

## set_block_hash_result (Constructor 1)

- **Signature**: `set_block_hash_result(result s)`
- **Description**: Constructs a `set_block_hash_result` object with the specified result status. This constructor initializes the result with success status and default values for verified blocks.
- **Parameters**:
  - `s` (result): The result status to set. Valid values include `result::success`, `result::unknown`, `result::block_hash_failed`, and `result::piece_hash_failed`.
- **Return Value**:
  - Returns a `set_block_hash_result` object initialized with the given status and default values.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result(result::success);
```
- **Preconditions**: The `result` enum must be valid.
- **Postconditions**: The `set_block_hash_result` object is initialized with the specified status and default values for verified blocks.
- **Thread Safety**: Thread-safe if the result enum is properly defined.
- **Complexity**: O(1)
- **See Also**: `set_block_hash_result(result, int, int)`

## set_block_hash_result (Constructor 2)

- **Signature**: `set_block_hash_result(result st, int first_block, int num)`
- **Description**: Constructs a `set_block_hash_result` object with the specified result status and verified block information. This constructor allows setting specific block ranges that were successfully verified.
- **Parameters**:
  - `st` (result): The result status to set. Valid values include `result::success`, `result::unknown`, `result::block_hash_failed`, and `result::piece_hash_failed`.
  - `first_block` (int): The index of the first verified block.
  - `num` (int): The number of consecutive verified blocks.
- **Return Value**:
  - Returns a `set_block_hash_result` object initialized with the specified status and verified block information.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result(result::success, 10, 5);
```
- **Preconditions**: The `result` enum must be valid, and `first_block` and `num` must be non-negative.
- **Postconditions**: The `set_block_hash_result` object is initialized with the specified status and verified block information.
- **Thread Safety**: Thread-safe if the result enum is properly defined.
- **Complexity**: O(1)
- **See Also**: `set_block_hash_result(result)`

## piece_range

- **Signature**: `index_range<piece_index_t> piece_range(piece_index_t const piece, int const blocks_per_piece) const`
- **Description**: Calculates the piece range for a given piece and blocks per piece count. This function computes the range of pieces that correspond to the verified blocks.
- **Parameters**:
  - `piece` (piece_index_t const): The piece index for which to calculate the range.
  - `blocks_per_piece` (int const): The number of blocks per piece.
- **Return Value**:
  - Returns an `index_range<piece_index_t>` object representing the range of pieces corresponding to the verified blocks.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto range = piece_range(piece_index_t(0), 16);
```
- **Preconditions**: `blocks_per_piece` must be positive.
- **Postconditions**: Returns the piece range corresponding to the verified blocks.
- **Thread Safety**: Thread-safe if the `piece` and `blocks_per_piece` parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: `set_block_hash_result`

## success

- **Signature**: `static set_block_hash_result success(int first_block, int num)`
- **Description**: Creates a `set_block_hash_result` object indicating success with the specified first verified block and number of verified blocks. This is a static factory method for creating success results.
- **Parameters**:
  - `first_block` (int): The index of the first verified block.
  - `num` (int): The number of consecutive verified blocks.
- **Return Value**:
  - Returns a `set_block_hash_result` object with the success status and specified verified block information.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result::success(10, 5);
```
- **Preconditions**: `first_block` and `num` must be non-negative.
- **Postconditions**: Returns a `set_block_hash_result` object with success status and verified block information.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: `unknown`, `block_hash_failed`, `piece_hash_failed`

## unknown

- **Signature**: `static set_block_hash_result unknown()`
- **Description**: Creates a `set_block_hash_result` object indicating an unknown result status. This is a static factory method for creating unknown results.
- **Parameters**: None
- **Return Value**:
  - Returns a `set_block_hash_result` object with the unknown status.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result::unknown();
```
- **Preconditions**: None
- **Postconditions**: Returns a `set_block_hash_result` object with unknown status.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `success`, `block_hash_failed`, `piece_hash_failed`

## block_hash_failed

- **Signature**: `static set_block_hash_result block_hash_failed()`
- **Description**: Creates a `set_block_hash_result` object indicating a block hash failure. This is a static factory method for creating block hash failure results.
- **Parameters**: None
- **Return Value**:
  - Returns a `set_block_hash_result` object with the block hash failure status.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result::block_hash_failed();
```
- **Preconditions**: None
- **Postconditions**: Returns a `set_block_hash_result` object with block hash failure status.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `success`, `unknown`, `piece_hash_failed`

## piece_hash_failed

- **Signature**: `static set_block_hash_result piece_hash_failed(int first_block, int num)`
- **Description**: Creates a `set_block_hash_result` object indicating a piece hash failure with the specified first verified block and number of verified blocks. This is a static factory method for creating piece hash failure results.
- **Parameters**:
  - `first_block` (int): The index of the first verified block.
  - `num` (int): The number of consecutive verified blocks.
- **Return Value**:
  - Returns a `set_block_hash_result` object with the piece hash failure status and specified verified block information.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = set_block_hash_result::piece_hash_failed(10, 5);
```
- **Preconditions**: `first_block` and `num` must be non-negative.
- **Postconditions**: Returns a `set_block_hash_result` object with piece hash failure status and verified block information.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: `success`, `unknown`, `block_hash_failed`

## add_hashes_result

- **Signature**: `explicit add_hashes_result(bool const v)`
- **Description**: Constructs an `add_hashes_result` object indicating whether the hashes were successfully added. This constructor initializes the result with a boolean value.
- **Parameters**:
  - `v` (bool const): The success status of adding hashes.
- **Return Value**:
  - Returns an `add_hashes_result` object initialized with the specified success status.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto result = add_hashes_result(true);
```
- **Preconditions**: None
- **Postconditions**: The `add_hashes_result` object is initialized with the specified success status.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: None

## node_index

- **Signature**: `node_index(file_index_t f, std::int32_t n)`
- **Description**: Constructs a `node_index` object representing a node in the file storage. This constructor initializes the node index with the specified file index and node index.
- **Parameters**:
  - `f` (file_index_t): The file index to which the node belongs.
  - `n` (std::int32_t): The node index within the file.
- **Return Value**:
  - Returns a `node_index` object initialized with the specified file and node indices.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto index = node_index(file_index_t(0), 10);
```
- **Preconditions**: The `file_index_t` must be valid.
- **Postconditions**: The `node_index` object is initialized with the specified file and node indices.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: None

## hash_request (Default Constructor)

- **Signature**: `hash_request() = default;`
- **Description**: Default constructor for the `hash_request` class. This constructor initializes a `hash_request` object with default values.
- **Parameters**: None
- **Return Value**:
  - Returns a `hash_request` object with default values.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto request = hash_request();
```
- **Preconditions**: None
- **Postconditions**: The `hash_request` object is initialized with default values.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `hash_request(file_index_t, int, int, int, int)`

## hash_request (Parameterized Constructor)

- **Signature**: `hash_request(file_index_t const f, int const b, int const i, int const c, int const p)`
- **Description**: Constructs a `hash_request` object with the specified file index, base, index, count, and proof layers. This constructor initializes the hash request with the given parameters.
- **Parameters**:
  - `f` (file_index_t const): The file index to which the hash request belongs.
  - `b` (int const): The base value for the hash request.
  - `i` (int const): The index value for the hash request.
  - `c` (int const): The count value for the hash request.
  - `p` (int const): The number of proof layers for the hash request.
- **Return Value**:
  - Returns a `hash_request` object initialized with the specified parameters.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto request = hash_request(file_index_t(0), 10, 5, 3, 2);
```
- **Preconditions**: The `file_index_t` must be valid, and `b`, `i`, `c`, and `p` must be non-negative.
- **Postconditions**: The `hash_request` object is initialized with the specified parameters.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: `hash_request()`

## hash_request (Copy Constructor)

- **Signature**: `hash_request(hash_request const&) = default;`
- **Description**: Copy constructor for the `hash_request` class. This constructor creates a copy of the specified `hash_request` object.
- **Parameters**:
  - `other` (hash_request const&): The `hash_request` object to copy.
- **Return Value**:
  - Returns a `hash_request` object that is a copy of the specified object.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto request1 = hash_request(file_index_t(0), 10, 5, 3, 2);
auto request2 = request1;
```
- **Preconditions**: The `hash_request` object must be valid.
- **Postconditions**: The `hash_request` object is a copy of the specified object.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: `hash_request()`, `hash_request(file_index_t, int, int, int, int)`

## hash_picker

- **Signature**: `hash_picker(file_storage const& files, aux::vector<aux::merkle_tree, file_index_t>& trees)`
- **Description**: Constructs a `hash_picker` object with the specified file storage and merkle trees. This constructor initializes the hash picker with the provided file storage and merkle trees.
- **Parameters**:
  - `files` (file_storage const&): The file storage to use for the hash picker.
  - `trees` (aux::vector<aux::merkle_tree, file_index_t>&): The merkle trees to use for the hash picker.
- **Return Value**:
  - Returns a `hash_picker` object initialized with the specified file storage and merkle trees.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto hash_picker = hash_picker(file_storage(), aux::vector<aux::merkle_tree, file_index_t>());
```
- **Preconditions**: The `file_storage` must be valid, and the `aux::vector` must be properly initialized.
- **Postconditions**: The `hash_picker` object is initialized with the specified file storage and merkle trees.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(n) where n is the number of files
- **See Also**: `pick_hashes`, `add_hashes`

## piece_layer

- **Signature**: `int piece_layer() const`
- **Description**: Returns the current piece layer of the hash picker. This function retrieves the piece layer information.
- **Parameters**: None
- **Return Value**:
  - Returns the piece layer as an integer.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto layer = hash_picker.piece_layer();
```
- **Preconditions**: The `hash_picker` object must be properly initialized.
- **Postconditions**: Returns the piece layer of the hash picker.
- **Thread Safety**: Thread-safe if the `hash_picker` object is properly initialized.
- **Complexity**: O(1)
- **See Also**: `hash_picker`

## priority_block_request

- **Signature**: `priority_block_request(file_index_t const f, int const b)`
- **Description**: Constructs a `priority_block_request` object with the specified file index and block index. This constructor initializes the priority block request with the given parameters.
- **Parameters**:
  - `f` (file_index_t const): The file index to which the block request belongs.
  - `b` (int const): The block index for the priority block request.
- **Return Value**:
  - Returns a `priority_block_request` object initialized with the specified parameters.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto request = priority_block_request(file_index_t(0), 10);
```
- **Preconditions**: The `file_index_t` must be valid, and `b` must be non-negative.
- **Postconditions**: The `priority_block_request` object is initialized with the specified parameters.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: None

## piece_block_request

- **Signature**: `piece_block_request(file_index_t const f, piece_index_t::diff_type const p)`
- **Description**: Constructs a `piece_block_request` object with the specified file index and piece index. This constructor initializes the piece block request with the given parameters.
- **Parameters**:
  - `f` (file_index_t const): The file index to which the block request belongs.
  - `p` (piece_index_t::diff_type const): The piece index for the piece block request.
- **Return Value**:
  - Returns a `piece_block_request` object initialized with the specified parameters.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
auto request = piece_block_request(file_index_t(0), 10);
```
- **Preconditions**: The `file_index_t` must be valid, and `p` must be non-negative.
- **Postconditions**: The `piece_block_request` object is initialized with the specified parameters.
- **Thread Safety**: Thread-safe if the parameters are properly defined.
- **Complexity**: O(1)
- **See Also**: None

## Usage Examples

### Basic Usage
```cpp
// Initialize file storage and merkle trees
file_storage files;
aux::vector<aux::merkle_tree, file_index_t> trees;

// Create hash picker
hash_picker hp(files, trees);

// Pick hashes for pieces
typed_bitfield<piece_index_t> pieces;
hash_request request = hp.pick_hashes(pieces);

// Add hashes to the hash picker
add_hashes_result result = hp.add_hashes(request, span<sha256_hash>());
```

### Error Handling
```cpp
// Check if hashes were successfully added
add_hashes_result result = hp.add_hashes(request, span<sha256_hash>());
if (result.valid) {
    // Hashes were successfully added
    std::cout << "Hashes added successfully" << std::endl;
} else {
    // Handle error case
    std::cerr << "Failed to add hashes" << std::endl;
}
```

### Edge Cases
```cpp
// Handle empty file storage
file_storage empty_files;
aux::vector<aux::merkle_tree, file_index_t> empty_trees;
hash_picker hp(empty_files, empty_trees);

// Pick hashes for empty pieces
typed_bitfield<piece_index_t> empty_pieces;
hash_request empty_request = hp.pick_hashes(empty_pieces);

// Add hashes to empty request
add_hashes_result empty_result = hp.add_hashes(empty_request, span<sha256_hash>());
```

## Best Practices

1. **Use const references**: When passing large objects, use const references to avoid copying.
2. **Check return values**: Always check the return values of functions