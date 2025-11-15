# polymorphic_socket API Documentation

## Overview
The `polymorphic_socket` class provides a polymorphic interface for network sockets, allowing different socket implementations to be used interchangeably. It leverages `boost::variant` to store different socket types and uses the `TORRENT_FWD_CALL` macro to forward calls to the underlying socket implementation.

## Class: polymorphic_socket

### Constructor: polymorphic_socket(S s)
- **Signature**: `explicit polymorphic_socket(S s)`
- **Description**: Constructs a `polymorphic_socket` from a socket of type `S`. This constructor is explicit to prevent unintended implicit conversions.
- **Parameters**:
  - `s` (S): The socket object to wrap. Must be move-constructible and nothrow move-constructible.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: 
  - Throws if the socket type is not nothrow move-constructible (asserted at compile time)
  - May throw if the underlying socket construction fails
- **Example**:
```cpp
tcp::socket socket(io_context);
polymorphic_socket sock(std::move(socket));
```
- **Preconditions**: The socket `s` must be in a valid state.
- **Postconditions**: The `polymorphic_socket` object is constructed and contains a valid socket.
- **Thread Safety**: Not thread-safe during construction.
- **Complexity**: O(1) - constant time.
- **See Also**: `polymorphic_socket(polymorphic_socket&&)`, `~polymorphic_socket()`

### Constructor: polymorphic_socket(polymorphic_socket&&)
- **Signature**: `polymorphic_socket(polymorphic_socket&&) = default`
- **Description**: Default move constructor for `polymorphic_socket`. Allows efficient transfer of ownership of the socket.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
polymorphic_socket sock1 = create_socket();
polymorphic_socket sock2 = std::move(sock1); // Efficient move
```
- **Preconditions**: `sock1` must be in a valid state.
- **Postconditions**: `sock1` is in a valid but unspecified state, `sock2` contains the moved socket.
- **Thread Safety**: Not thread-safe during move.
- **Complexity**: O(1) - constant time.
- **See Also**: `polymorphic_socket(S s)`, `~polymorphic_socket()`

### Destructor: ~polymorphic_socket()
- **Signature**: `~polymorphic_socket() = default`
- **Description**: Default destructor for `polymorphic_socket`. Properly cleans up the underlying socket.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
{
    polymorphic_socket sock;
    // Use socket
} // Automatic cleanup when sock goes out of scope
```
- **Preconditions**: None
- **Postconditions**: The socket is properly closed and resources are released.
- **Thread Safety**: Not thread-safe during destruction.
- **Complexity**: O(1) - constant time.
- **See Also**: `polymorphic_socket(polymorphic_socket&&)`, `polymorphic_socket(S s)`

## Socket Operations

### is_open
- **Signature**: `bool is_open() const`
- **Description**: Checks if the socket is open and connected.
- **Parameters**: None
- **Return Value**: `true` if the socket is open, `false` otherwise.
- **Exceptions/Errors**: None
- **Example**:
```cpp
if (sock.is_open()) {
    std::cout << "Socket is open" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: Returns the open status of the socket.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `open()`, `close()`

### open(protocol_type const& p, error_code& ec)
- **Signature**: `void open(protocol_type const& p, error_code& ec)`
- **Description**: Opens the socket with the specified protocol. The error code is set if an error occurs.
- **Parameters**:
  - `p` (protocol_type): The protocol to use for the connection.
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: None
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
sock.open(protocol_type(), ec);
if (ec) {
    std::cerr << "Failed to open socket: " << ec.message() << std::endl;
}
```
- **Preconditions**: The socket must not be already open.
- **Postconditions**: The socket is open and ready for use, or an error is set in `ec`.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `open(protocol_type const& p)`, `close()`

### open(protocol_type const& p)
- **Signature**: `void open(protocol_type const& p)`
- **Description**: Opens the socket with the specified protocol. Throws an exception if an error occurs.
- **Parameters**:
  - `p` (protocol_type): The protocol to use for the connection.
- **Return Value**: None
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be opened
- **Example**:
```cpp
try {
    sock.open(protocol_type());
    std::cout << "Socket opened successfully" << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to open socket: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must not be already open.
- **Postconditions**: The socket is open and ready for use.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `open(protocol_type const& p, error_code& ec)`, `close()`

### close(error_code& ec)
- **Signature**: `void close(error_code& ec)`
- **Description**: Closes the socket. The error code is set if an error occurs.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: None
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
sock.close(ec);
if (ec) {
    std::cerr << "Failed to close socket: " << ec.message() << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: The socket is closed and resources are released, or an error is set in `ec`.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `close()`, `is_open()`

### close()
- **Signature**: `void close()`
- **Description**: Closes the socket. Throws an exception if an error occurs.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be closed
- **Example**:
```cpp
try {
    sock.close();
    std::cout << "Socket closed successfully" << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to close socket: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: The socket is closed and resources are released.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `close(error_code& ec)`, `is_open()`

### local_endpoint(error_code& ec) const
- **Signature**: `endpoint_type local_endpoint(error_code& ec) const`
- **Description**: Returns the local endpoint of the socket. The error code is set if an error occurs.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: The local endpoint as an `endpoint_type` object.
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
auto endpoint = sock.local_endpoint(ec);
if (ec) {
    std::cerr << "Failed to get local endpoint: " << ec.message() << std::endl;
} else {
    std::cout << "Local endpoint: " << endpoint << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: Returns the local endpoint, or `ec` is set if an error occurs.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `local_endpoint()`, `remote_endpoint()`

### local_endpoint() const
- **Signature**: `endpoint_type local_endpoint() const`
- **Description**: Returns the local endpoint of the socket. Throws an exception if an error occurs.
- **Parameters**: None
- **Return Value**: The local endpoint as an `endpoint_type` object.
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be queried
- **Example**:
```cpp
try {
    auto endpoint = sock.local_endpoint();
    std::cout << "Local endpoint: " << endpoint << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to get local endpoint: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: Returns the local endpoint.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `local_endpoint(error_code& ec)`, `remote_endpoint()`

### remote_endpoint(error_code& ec) const
- **Signature**: `endpoint_type remote_endpoint(error_code& ec) const`
- **Description**: Returns the remote endpoint of the socket. The error code is set if an error occurs.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: The remote endpoint as an `endpoint_type` object.
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
auto endpoint = sock.remote_endpoint(ec);
if (ec) {
    std::cerr << "Failed to get remote endpoint: " << ec.message() << std::endl;
} else {
    std::cout << "Remote endpoint: " << endpoint << std::endl;
}
```
- **Preconditions**: The socket must be open and connected.
- **Postconditions**: Returns the remote endpoint, or `ec` is set if an error occurs.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `remote_endpoint()`, `local_endpoint()`

### remote_endpoint() const
- **Signature**: `endpoint_type remote_endpoint() const`
- **Description**: Returns the remote endpoint of the socket. Throws an exception if an error occurs.
- **Parameters**: None
- **Return Value**: The remote endpoint as an `endpoint_type` object.
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be queried
- **Example**:
```cpp
try {
    auto endpoint = sock.remote_endpoint();
    std::cout << "Remote endpoint: " << endpoint << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to get remote endpoint: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must be open and connected.
- **Postconditions**: Returns the remote endpoint.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `remote_endpoint(error_code& ec)`, `local_endpoint()`

### bind(endpoint_type const& endpoint, error_code& ec)
- **Signature**: `void bind(endpoint_type const& endpoint, error_code& ec)`
- **Description**: Binds the socket to the specified endpoint. The error code is set if an error occurs.
- **Parameters**:
  - `endpoint` (endpoint_type const&): The endpoint to bind to.
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: None
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
sock.bind(endpoint_type(), ec);
if (ec) {
    std::cerr << "Failed to bind socket: " << ec.message() << std::endl;
}
```
- **Preconditions**: The socket must be open and not bound.
- **Postconditions**: The socket is bound to the specified endpoint, or an error is set in `ec`.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `bind(endpoint_type const& endpoint)`, `open()`

### bind(endpoint_type const& endpoint)
- **Signature**: `void bind(endpoint_type const& endpoint)`
- **Description**: Binds the socket to the specified endpoint. Throws an exception if an error occurs.
- **Parameters**:
  - `endpoint` (endpoint_type const&): The endpoint to bind to.
- **Return Value**: None
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be bound
- **Example**:
```cpp
try {
    sock.bind(endpoint_type());
    std::cout << "Socket bound successfully" << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to bind socket: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must be open and not bound.
- **Postconditions**: The socket is bound to the specified endpoint.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `bind(endpoint_type const& endpoint, error_code& ec)`, `open()`

### available(error_code& ec) const
- **Signature**: `std::size_t available(error_code& ec) const`
- **Description**: Returns the number of bytes available for reading. The error code is set if an error occurs.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: The number of bytes available for reading.
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
std::size_t bytes = sock.available(ec);
if (ec) {
    std::cerr << "Failed to check available bytes: " << ec.message() << std::endl;
} else {
    std::cout << "Available bytes: " << bytes << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: Returns the number of available bytes, or `ec` is set if an error occurs.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `available()`, `read_some()`

### available() const
- **Signature**: `std::size_t available() const`
- **Description**: Returns the number of bytes available for reading. Throws an exception if an error occurs.
- **Parameters**: None
- **Return Value**: The number of bytes available for reading.
- **Exceptions/Errors**: 
  - Throws `std::system_error` if the socket cannot be queried
- **Example**:
```cpp
try {
    std::size_t bytes = sock.available();
    std::cout << "Available bytes: " << bytes << std::endl;
} catch (const std::system_error& e) {
    std::cerr << "Failed to check available bytes: " << e.what() << std::endl;
}
```
- **Preconditions**: The socket must be open.
- **Postconditions**: Returns the number of available bytes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - constant time.
- **See Also**: `available(error_code& ec)`, `read_some()`

## Data Transfer Operations

### read_some(Mutable_Buffers const& buffers, error_code& ec)
- **Signature**: `std::size_t read_some(Mutable_Buffers const& buffers, error_code& ec)`
- **Description**: Reads data from the socket into the specified buffers. The error code is set if an error occurs.
- **Parameters**:
  - `buffers` (Mutable_Buffers const&): The buffers to read into.
  - `ec` (error_code&): Error code to store any error that occurs.
- **Return Value**: The number of bytes read.
- **Exceptions/Errors**: 
  - Sets `ec` if an error occurs
  - May throw if the underlying socket operation fails
- **Example**:
```cpp
error_code ec;
std::size_t bytes = sock.read_some(buffer, ec);
if (ec) {
    std::cerr << "Failed to read from socket: " << ec.message() << std::endl;
} else {
    std::cout << "Read " << bytes << " bytes" << std::endl;
}
```
- **Preconditions**: The socket must be open and connected.
- **Postconditions**: Returns the number of bytes read, or `ec` is set if an error occurs.
- **Thread Safety**: Not thread-safe.
- **Complexity**: O(n) - linear in the number of bytes read.
- **See Also**: `read_some(Mutable_Buffers const& buffers)`, `write_some()`

### read_some(Mutable_Buffers const& buffers)
- **Signature**: `std::size_t read_some(Mutable_Buffers const& buffers)`
- **Description**: Reads data from the socket into