```markdown
# API Documentation for Custom Storage Implementation

## temp_storage

- **Signature**: `temp_storage(lt::file_storage const& fs)`
- **Description**: Constructor for the temporary storage implementation. Initializes the storage with the given file storage metadata.
- **Parameters**:
  - `fs` (lt::file_storage const&): The file storage object containing metadata about the torrent files. This must be valid and cannot be null.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::file_storage fs;
// populate fs with torrent file metadata
auto storage = temp_storage(fs);
```
- **Preconditions**: The `fs` parameter must be a valid lt::file_storage object.
- **Postconditions**: The storage object is initialized with the provided file storage metadata.
- **Thread Safety**: Not thread-safe (constructor).
- **Complexity**: O(1) time and space complexity.
- **See Also**: `lt::file_storage`

## readv

- **Signature**: `lt::span<char const> readv(lt::peer_request const r, lt::storage_error& ec) const`
- **Description**: Reads data from the specified piece and offset into a span of characters. This function is used by libtorrent to read data from the storage.
- **Parameters**:
  - `r` (lt::peer_request const): The request specifying which piece and offset to read from.
  - `ec` (lt::storage_error&): Error code reference that will be set if an error occurs.
- **Return Value**: Returns a span of characters containing the requested data. Returns an empty span if an error occurs.
- **Exceptions/Errors**: 
  - `ec.operation = lt::operation_t::file_read` if there's an error reading the file.
  - `ec.ec = boost::asio::error::eof` if the requested piece doesn't exist.
- **Example**:
```cpp
lt::peer_request req;
lt::storage_error ec;
auto data = storage.readv(req, ec);
if (ec.ec) {
    // handle error
}
```
- **Preconditions**: The storage must be initialized and the requested piece must exist.
- **Postconditions**: The returned span contains the requested data or is empty if an error occurred.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity for finding the piece, O(n) for copying data where n is the amount of data copied.
- **See Also**: `lt::peer_request`, `lt::storage_error`

## writev

- **Signature**: `void writev(lt::span<char const> const b, lt::piece_index_t const piece, int const offset)`
- **Description**: Writes data from a span of characters to the specified piece and offset. This function is used by libtorrent to write data to the storage.
- **Parameters**:
  - `b` (lt::span<char const> const): The data to write, as a span of characters.
  - `piece` (lt::piece_index_t const): The piece index where the data should be written.
  - `offset` (int const): The offset within the piece where the data should be written.
- **Return Value**: None
- **Exceptions/Errors**: None (assumes all operations succeed)
- **Example**:
```cpp
lt::span<char const> data("Hello, World!", 13);
storage.writev(data, 0, 0);
```
- **Preconditions**: The storage must be initialized and the piece must exist.
- **Postconditions**: The specified data is written to the given piece and offset.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity for finding the piece, O(n) for copying data where n is the amount of data copied.
- **See Also**: `lt::span`, `lt::piece_index_t`

## hash

- **Signature**: `lt::sha1_hash hash(lt::piece_index_t const piece, lt::span<lt::sha256_hash> const block_hashes, lt::storage_error& ec) const`
- **Description**: Computes the SHA-1 hash of a specified piece using the provided block hashes. This is used by libtorrent to verify piece integrity.
- **Parameters**:
  - `piece` (lt::piece_index_t const): The piece index to hash.
  - `block_hashes` (lt::span<lt::sha256_hash> const): The block hashes to use in the computation.
  - `ec` (lt::storage_error&): Error code reference that will be set if an error occurs.
- **Return Value**: Returns the SHA-1 hash of the piece. Returns an empty hash if an error occurs.
- **Exceptions/Errors**:
  - `ec.operation = lt::operation_t::file_read` if there's an error reading the file.
  - `ec.ec = boost::asio::error::eof` if the requested piece doesn't exist.
- **Example**:
```cpp
lt::span<lt::sha256_hash> block_hashes;
lt::storage_error ec;
auto hash = storage.hash(0, block_hashes, ec);
if (ec.ec) {
    // handle error
}
```
- **Preconditions**: The storage must be initialized and the piece must exist.
- **Postconditions**: The hash of the piece is computed and returned, or an empty hash is returned if an error occurred.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the size of the piece.
- **See Also**: `lt::sha1_hash`, `lt::span`, `lt::storage_error`

## hash2

- **Signature**: `lt::sha256_hash hash2(lt::piece_index_t const piece, int const offset, lt::storage_error& ec)`
- **Description**: Computes the SHA-256 hash of a specified piece starting from a given offset. This is used by libtorrent to verify piece integrity.
- **Parameters**:
  - `piece` (lt::piece_index_t const): The piece index to hash.
  - `offset` (int const): The offset within the piece to start hashing from.
  - `ec` (lt::storage_error&): Error code reference that will be set if an error occurs.
- **Return Value**: Returns the SHA-256 hash of the specified region. Returns an empty hash if an error occurs.
- **Exceptions/Errors**:
  - `ec.operation = lt::operation_t::file_read` if there's an error reading the file.
  - `ec.ec = boost::asio::error::eof` if the requested piece doesn't exist.
- **Example**:
```cpp
lt::storage_error ec;
auto hash = storage.hash2(0, 0, ec);
if (ec.ec) {
    // handle error
}
```
- **Preconditions**: The storage must be initialized and the piece must exist.
- **Postconditions**: The hash of the specified region is computed and returned, or an empty hash is returned if an error occurred.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the size of the region being hashed.
- **See Also**: `lt::sha256_hash`, `lt::storage_error`

## piece_size

- **Signature**: `int piece_size(lt::piece_index_t piece) const`
- **Description**: Returns the size of a specified piece in bytes. This is used by libtorrent to determine the size of pieces during file operations.
- **Parameters**:
  - `piece` (lt::piece_index_t const): The piece index to query.
- **Return Value**: Returns the size of the piece in bytes. Returns the remainder of the total size when it's the last piece.
- **Exceptions/Errors**: None
- **Example**:
```cpp
int size = storage.piece_size(0);
std::cout << "Piece size: " << size << " bytes" << std::endl;
```
- **Preconditions**: The storage must be initialized and the piece index must be valid.
- **Postconditions**: The returned value is the size of the specified piece in bytes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `lt::piece_index_t`

## pop

- **Signature**: `lt::storage_index_t pop(std::vector<lt::storage_index_t>& q)`
- **Description**: Removes and returns the last element from a vector of storage indices. This is used to manage free slots in the storage system.
- **Parameters**:
  - `q` (std::vector<lt::storage_index_t>&): The vector of storage indices to pop from.
- **Return Value**: Returns the removed storage index.
- **Exceptions/Errors**: Throws an assertion error if the vector is empty.
- **Example**:
```cpp
std::vector<lt::storage_index_t> slots;
slots.push_back(1);
auto index = pop(slots);
```
- **Preconditions**: The vector must not be empty.
- **Postconditions**: The last element is removed from the vector and returned.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `std::vector`, `lt::storage_index_t`

## temp_disk_io

- **Signature**: `temp_disk_io(lt::io_context& ioc)`
- **Description**: Constructor for the temporary disk I/O implementation. Initializes the disk I/O with the given io_context.
- **Parameters**:
  - `ioc` (lt::io_context&): The io_context object used for asynchronous operations.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::io_context io_ctx;
auto disk_io = temp_disk_io(io_ctx);
```
- **Preconditions**: The io_context must be valid.
- **Postconditions**: The disk I/O object is initialized with the provided io_context.
- **Thread Safety**: Not thread-safe (constructor).
- **Complexity**: O(1) time and space complexity.
- **See Also**: `lt::io_context`

## settings_updated

- **Signature**: `void settings_updated() override`
- **Description**: Overrides the settings_updated method from the base class. This function is called when settings are updated in the disk I/O system.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
disk_io.settings_updated();
```
- **Preconditions**: The disk I/O object must be initialized.
- **Postconditions**: The settings are updated (no effect in this implementation).
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `lt::disk_interface`

## new_torrent

- **Signature**: `lt::storage_holder new_torrent(lt::storage_params const& params, std::shared_ptr<void> const&) override`
- **Description**: Creates a new storage object for a torrent. This is called by libtorrent when a new torrent is added.
- **Parameters**:
  - `params` (lt::storage_params const&): The storage parameters for the new torrent.
  - `shared_ptr` (std::shared_ptr<void> const&): A shared pointer to additional data (not used in this implementation).
- **Return Value**: Returns a storage holder containing the new storage object.
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::storage_params params;
auto storage = new_torrent(params, nullptr);
```
- **Preconditions**: The storage parameters must be valid and the disk I/O object must be initialized.
- **Postconditions**: A new storage object is created and returned.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity for finding free slots, O(n) for creating the storage object where n is the number of files.
- **See Also**: `lt::storage_params`, `lt::storage_holder`

## remove_torrent

- **Signature**: `void remove_torrent(lt::storage_index_t const idx) override`
- **Description**: Removes a torrent from the storage system. This is called by libtorrent when a torrent is removed.
- **Parameters**:
  - `idx` (lt::storage_index_t const): The index of the torrent to remove.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
remove_torrent(1);
```
- **Preconditions**: The torrent index must be valid.
- **Postconditions**: The torrent at the specified index is removed from the storage system.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `lt::storage_index_t`

## abort

- **Signature**: `void abort(bool) override`
- **Description**: Overrides the abort method from the base class. This function is called when a torrent is being aborted.
- **Parameters**:
  - `bool`: A flag indicating whether the abort is immediate (not used in this implementation).
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
disk_io.abort(true);
```
- **Preconditions**: The disk I/O object must be initialized.
- **Postconditions**: The abort operation is processed (no effect in this implementation).
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `lt::disk_interface`

## async_read

- **Signature**: `void async_read(lt::storage_index_t storage, lt::peer_request const& r, std::function<void(lt::disk_buffer_holder block, lt::storage_error const& se)> handler, lt::disk_job_flags_t)`
- **Description**: Asynchronously reads data from the specified piece and offset. This is called by libtorrent to read data from storage.
- **Parameters**:
  - `storage` (lt::storage_index_t): The storage index where the data is located.
  - `r` (lt::peer_request const&): The request specifying which piece and offset to read from.
  - `handler` (std::function<void(lt::disk_buffer_holder block, lt::storage_error const& se)>): The callback function to call when the read operation completes.
  - `flags` (lt::disk_job_flags_t): Flags for the disk job (not used in this implementation).
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::storage_index_t storage = 0;
lt::peer_request req;
auto handler = [](lt::disk_buffer_holder block, lt::storage_error const& se) {
    // handle result
};
async_read(storage, req, handler, lt::disk_job_flags_t::none);
```
- **Preconditions**: The storage index must be valid and the storage object must be initialized.
- **Postconditions**: The read operation is queued and the handler will be called when it completes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity for queuing the operation.
- **See Also**: `lt::disk_buffer_holder`, `lt::storage_error`

## async_write

- **Signature**: `bool async_write(lt::storage_index_t storage, lt::peer_request const& r, char const* buf, std::shared_ptr<lt::disk_observer>, std::function<void(lt::storage_error const&)> handler, lt::disk_job_flags_t)`
- **Description**: Asynchronously writes data to the specified piece and offset. This is called by libtorrent to write data to storage.
- **Parameters**:
  - `storage` (lt::storage_index_t): The storage index where the data should be written.
  - `r` (lt::peer_request const&): The request specifying which piece and offset to write to.
  - `buf` (char const*): The data to write.
  - `observer` (std::shared_ptr<lt::disk_observer>): A shared pointer to a disk observer (not used in this implementation).
  - `handler` (std::function<void(lt::storage_error const&)>): The callback function to call when the write operation completes.
  - `flags` (lt::disk_job_flags_t): Flags for the disk job (not used in this implementation).
- **Return Value**: Returns true if the write operation was queued successfully, false otherwise.
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::storage_index_t storage = 0;
lt::peer_request req;
auto handler = [](lt::storage_error const& se) {
    // handle result
};
async_write(storage, req, "data", nullptr, handler, lt::disk_job_flags_t::none);
```
- **Preconditions**: The storage index must be valid and the storage object must be initialized.
- **Postconditions**: The write operation is queued and the handler will be called when it completes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time complexity for queuing the operation.
- **See Also**: `lt::disk_observer`, `lt::storage_error`

## async_hash

- **Signature**: `void async_hash(lt::storage_index_t storage, lt::piece_index_t const piece, lt::span<lt::sha256_hash> block_hashes, lt::disk_job_flags_t, std::function<void(lt::piece_index_t, lt::sha1_hash const&, lt::storage_error const&)> handler)`
- **Description**: Asynchronously computes the SHA-1 hash of a specified piece. This is called by libtorrent to verify piece integrity.
- **Parameters**:
  - `storage` (lt::storage_index_t): The storage index where the piece is located.
  - `piece` (lt::piece_index_t const): The piece index to hash.
  - `block_hashes` (lt::span<lt::sha256_hash>): The block hashes to use in the computation.
  - `flags` (lt::disk_job_flags_t): Flags for the disk job (not used in this implementation).
  - `handler` (std::function<void(lt::piece_index_t, lt::sha1_hash const&, lt::storage_error const&)>): The callback function to call when the hash operation completes.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
lt::storage_index_t storage = 0;
lt::piece_index_t piece = 0;
lt::span<lt::sha256_hash> block_hashes;
auto handler = [](lt::piece_index_t piece, lt::sha1_hash const& hash