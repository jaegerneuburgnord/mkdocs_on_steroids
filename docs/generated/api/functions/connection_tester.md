# Connection Tester API Documentation

## generate_block

- **Signature**: `void generate_block(span<std::uint32_t> buffer, piece_index_t const piece, int const offset)`
- **Description**: Fills a buffer with a pattern based on piece and offset values. This function is used to generate test data blocks for torrent verification and testing purposes. The pattern is a 32-bit value constructed from the piece index and offset.
- **Parameters**:
  - `buffer` (span<std::uint32_t>): The buffer to fill with the generated pattern. This must be a valid span of 32-bit unsigned integers.
  - `piece` (piece_index_t const): The piece index used to generate the pattern. This determines the high 8 bits of the pattern.
  - `offset` (int const): The offset within the piece used to generate the pattern. This determines the middle 8 bits of the pattern.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown, but the function assumes valid input parameters.
- **Example**:
```cpp
std::vector<std::uint32_t> buffer(1024);
piece_index_t piece = 42;
int offset = 8192;
generate_block(buffer, piece, offset);
```
- **Preconditions**: `buffer` must be a valid span of 32-bit unsigned integers.
- **Postconditions**: The buffer is filled with the generated pattern based on the piece and offset.
- **Thread Safety**: This function is thread-safe as it only reads input parameters and writes to the buffer.
- **Complexity**: O(n) where n is the size of the buffer.
- **See Also**: `verify_piece()`

## leaf_path

- **Signature**: `std::string leaf_path(std::string f)`
- **Description**: Extracts the leaf path from a file path string. This function returns the last component of the path, handling both forward and back slashes on different platforms.
- **Parameters**:
  - `f` (std::string): The file path from which to extract the leaf path.
- **Return Value**:
  - `std::string`: The leaf path (last component) of the input path.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::string path = "/home/user/documents/file.txt";
std::string leaf = leaf_path(path);
// leaf will be "file.txt"
```
- **Preconditions**: `f` must be a valid string representing a file path.
- **Postconditions**: Returns the last component of the path.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) where n is the length of the input string.
- **See Also**: `peer_conn()`

## peer_conn

- **Signature**: `peer_conn(io_context& ios, int piece_count, int blocks_pp, tcp::endpoint const& ep, char const* ih, bool seed_, int churn_, bool corrupt_)`
- **Description**: Constructor for the peer_conn class. Initializes a peer connection with the given parameters. This class manages a single peer connection in the torrent testing framework.
- **Parameters**:
  - `ios` (io_context&): The io_context for the connection.
  - `piece_count` (int): The number of pieces in the torrent.
  - `blocks_pp` (int): The number of blocks per piece.
  - `ep` (tcp::endpoint const&): The endpoint to connect to.
  - `ih` (char const*): The info hash of the torrent.
  - `seed_` (bool): Whether this peer is a seed.
  - `churn_` (int): The churn rate for the connection.
  - `corrupt_` (bool): Whether to generate corrupt data.
- **Return Value**:
  - None (constructor)
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
io_context ios;
tcp::endpoint ep(address_v4::loopback(), 6881);
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
```
- **Preconditions**: The io_context must be valid and the endpoint must be valid.
- **Postconditions**: The peer_conn object is initialized with the given parameters.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `start_conn()`, `on_connect()`

## start_conn

- **Signature**: `void start_conn()`
- **Description**: Initiates the connection process by binding to a local address and attempting to connect to the remote endpoint. This function is typically called after the peer_conn object is constructed.
- **Parameters**: None
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown, but the function may return if the connection fails.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
conn.start_conn();
```
- **Preconditions**: The peer_conn object must be properly constructed.
- **Postconditions**: The connection attempt is initiated.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_connect()`

## on_connect

- **Signature**: `void on_connect(error_code const& ec)`
- **Description**: Handles the connect callback. If the connection is successful, it sends the handshake message. This function is called when the connection attempt completes.
- **Parameters**:
  - `ec` (error_code const&): The error code from the connection attempt.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_connect(error_code());
```
- **Preconditions**: The connection attempt must have been initiated.
- **Postconditions**: If the connection is successful, the handshake is sent.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_handshake()`

## on_handshake

- **Signature**: `void on_handshake(char* h, error_code const& ec, size_t)`
- **Description**: Handles the handshake callback. It reads the handshake from the peer and initiates the next step in the connection process. This function is called when the handshake message is received.
- **Parameters**:
  - `h` (char*): The handshake message.
  - `ec` (error_code const&): The error code from the handshake operation.
  - `size_t`: Unused parameter.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_handshake(handshake_message, error_code());
```
- **Preconditions**: The handshake message must be valid.
- **Postconditions**: The handshake is processed and the next step is initiated.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_handshake2()`

## on_handshake2

- **Signature**: `void on_handshake2(error_code const& ec, size_t)`
- **Description**: Handles the second handshake callback. It reads the complete handshake and sets up the connection based on the extension bits. This function is called when the full handshake is received.
- **Parameters**:
  - `ec` (error_code const&): The error code from the handshake operation.
  - `size_t`: Unused parameter.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_handshake2(error_code(), 0);
```
- **Preconditions**: The handshake must be complete and valid.
- **Postconditions**: The connection is set up and ready for communication.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `write_have_all()`

## write_have_all

- **Signature**: `void write_have_all()`
- **Description**: Writes a have_all message and an unchoke message to the peer. This function is used to inform the peer that this client has all pieces and to unchoke the peer.
- **Parameters**: None
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
conn.write_have_all();
```
- **Preconditions**: The connection must be established.
- **Postconditions**: The have_all and unchoke messages are sent to the peer.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `write_have()`

## on_sent

- **Signature**: `void on_sent(error_code const& ec, size_t, char const* msg)`
- **Description**: Handles the send callback. If the message is sent successfully, it reads the next message from the peer. This function is called when a message is sent.
- **Parameters**:
  - `ec` (error_code const&): The error code from the send operation.
  - `size_t`: Unused parameter.
  - `msg` (char const*): The message that was sent.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_sent(error_code(), 0, "have_all");
```
- **Preconditions**: The message must be valid.
- **Postconditions**: If the send is successful, the next message is read.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_msg_length()`

## write_request

- **Signature**: `bool write_request()`
- **Description**: Writes a request message to the peer if the conditions are met. This function checks if the peer is not choked and if there are pieces to request.
- **Parameters**: None
- **Return Value**:
  - `bool`: True if a request was sent, false otherwise.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
if (conn.write_request()) {
    // Request was sent
}
```
- **Preconditions**: The connection must be established and the peer must not be choked.
- **Postconditions**: If a request was sent, the request message is sent to the peer.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_req_sent()`

## on_req_sent

- **Signature**: `void on_req_sent(char* m, error_code const& ec, size_t)`
- **Description**: Handles the request send callback. It frees the request message and starts the download process if the send was successful. This function is called when a request message is sent.
- **Parameters**:
  - `m` (char*): The request message.
  - `ec` (error_code const&): The error code from the send operation.
  - `size_t`: Unused parameter.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_req_sent(request_message, error_code(), 0);
```
- **Preconditions**: The request message must be valid.
- **Postconditions**: If the send is successful, the download process starts.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `work_download()`

## close

- **Signature**: `void close(char const* msg, error_code const& ec)`
- **Description**: Closes the connection and prints a message. This function is called when the connection is closed, either normally or due to an error.
- **Parameters**:
  - `msg` (char const*): The message to print.
  - `ec` (error_code const&): The error code from the connection closure.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
conn.close("Connection closed", error_code());
```
- **Preconditions**: The connection must be established.
- **Postconditions**: The connection is closed and a message is printed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `main()`

## work_download

- **Signature**: `void work_download()`
- **Description**: Processes the download by sending requests and handling received data. This function is called when data needs to be downloaded.
- **Parameters**: None
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false);
conn.work_download();
```
- **Preconditions**: The connection must be established.
- **Postconditions**: Data is downloaded and processed.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) where n is the amount of data to download.
- **See Also**: `on_message()`

## on_msg_length

- **Signature**: `void on_msg_length(error_code const& ec, size_t)`
- **Description**: Handles the message length callback. It reads the message length and initiates the next step in the message processing. This function is called when the message length is received.
- **Parameters**:
  - `ec` (error_code const&): The error code from the message length operation.
  - `size_t`: Unused parameter.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_msg_length(error_code(), 0);
```
- **Preconditions**: The message length must be valid.
- **Postconditions**: The message length is processed and the next step is initiated.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `on_message()`

## on_message

- **Signature**: `void on_message(error_code const& ec, size_t bytes_transferred)`
- **Description**: Handles the message callback. It processes the received message and initiates the next step in the message processing. This function is called when a message is received.
- **Parameters**:
  - `ec` (error_code const&): The error code from the message operation.
  - `bytes_transferred` (size_t): The number of bytes transferred.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// This function is called automatically by the system
on_message(error_code(), 1024);
```
- **Preconditions**: The message must be valid.
- **Postconditions**: The message is processed and the next step is initiated.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1)
- **See Also**: `verify_piece()`

## verify_piece

- **Signature**: `bool verify_piece(piece_index_t const piece, int start, char const* ptr, int size)`
- **Description**: Verifies that a piece of data matches the expected pattern. This function compares the received data with the expected pattern generated by generate_block.
- **Parameters**:
  - `piece` (piece_index_t const): The piece index to verify.
  - `start` (int): The start offset of the data to verify.
  - `ptr` (char const*): The pointer to the data to verify.
  - `size` (int): The size of the data to verify.
- **Return Value**:
  - `bool`: True if the piece matches the expected pattern, false otherwise.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
bool valid = verify_piece(42, 0, received_data, 1024);
if (valid) {
    // Data is valid
}
```
- **Preconditions**: The data must be valid and the size must be correct.
- **Postconditions**: Returns true if the data matches the expected pattern.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) where n is the size of the data to verify.
- **See Also**: `generate_block()`

## write_piece

- **Signature**: `void write_piece(piece_index_t const piece, int start, int length)`
- **Description**: Writes a piece of data to the write buffer. This function generates the data using generate_block and optionally corrupts it. This function is used to generate test data for torrent verification.
- **Parameters**:
  - `piece` (piece_index_t const): The piece index to write.
  - `start` (int): The start offset of the piece.
  - `length` (int): The length of the piece to write.
- **Return Value**:
  - void: This function does not return a value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
peer_conn conn(ios, 100, 16, ep, "info_hash", true, 10, false