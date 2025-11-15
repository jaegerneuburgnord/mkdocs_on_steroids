# libtorrent UTP Stream API Documentation

## Function Reference

### T

- **Signature**: `operator T() const`
- **Description**: Converts the underlying data storage to the specified type T using type-specific reading logic. This is a type conversion operator that extracts data from the internal storage buffer.
- **Parameters**: None
- **Return Value**: The converted value of type T extracted from the internal storage.
- **Exceptions/Errors**: No exceptions thrown, but may return invalid data if the internal storage doesn't contain valid data of the requested type.
- **Example**:
```cpp
int value = stream.T<int>();
```
- **Preconditions**: The internal storage must contain valid data that can be converted to type T.
- **Postconditions**: Returns the converted value of type T.
- **Thread Safety**: Thread-safe if the underlying data is not modified during conversion.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_type()`, `get_version()`

### get_type

- **Signature**: `int get_type() const`
- **Description**: Retrieves the type of the UTP stream message by extracting the upper 4 bits from the type_version field.
- **Parameters**: None
- **Return Value**: An integer representing the UTP message type (bits 7-4 of the type_version field).
- **Exceptions/Errors**: None
- **Example**:
```cpp
int stream_type = stream.get_type();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns the UTP message type.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_version()`, `get_executor()`

### get_version

- **Signature**: `int get_version() const`
- **Description**: Retrieves the version of the UTP stream message by extracting the lower 4 bits from the type_version field.
- **Parameters**: None
- **Return Value**: An integer representing the UTP message version (bits 3-0 of the type_version field).
- **Exceptions/Errors**: None
- **Example**:
```cpp
int stream_version = stream.get_version();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns the UTP message version.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_type()`, `get_executor()`

### get_executor

- **Signature**: `executor_type get_executor()`
- **Description**: Returns the executor associated with the UTP stream, which is used for asynchronous operations and event handling.
- **Parameters**: None
- **Return Value**: The executor type associated with the stream's I/O service.
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto executor = stream.get_executor();
```
- **Preconditions**: The stream must be properly initialized.
- **Postconditions**: Returns a valid executor object.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `lowest_layer()`, `async_connect()`

### utp_stream

- **Signature**: `utp_stream(utp_stream const&) = delete`
- **Description**: Deleted copy constructor to prevent copying of UTP stream objects, ensuring that each stream object maintains its own unique state and resources.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**: Not applicable - this constructor is deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Not applicable (constructor cannot be called).
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `lowest_layer()`, `get_executor()`

### lowest_layer

- **Signature**: `lowest_layer_type& lowest_layer()`
- **Description**: Returns a reference to the lowest layer of the stream, which is the stream itself. This is used to access the underlying stream functionality.
- **Parameters**: None
- **Return Value**: A reference to the lowest layer type of the stream.
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto& lowest_layer = stream.lowest_layer();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns a reference to the lowest layer.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_executor()`, `async_connect()`

### lowest_layer

- **Signature**: `lowest_layer_type const& lowest_layer() const`
- **Description**: Returns a const reference to the lowest layer of the stream, which is the stream itself. This is used to access the underlying stream functionality in a read-only manner.
- **Parameters**: None
- **Return Value**: A const reference to the lowest layer type of the stream.
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto const& lowest_layer = stream.lowest_layer();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns a const reference to the lowest layer.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `lowest_layer()`, `get_executor()`

### io_control

- **Signature**: `void io_control(IO_Control_Command&)`
- **Description**: Performs an I/O control operation on the stream. This function is a no-op in the current implementation.
- **Parameters**:
  - `command` (IO_Control_Command&): The I/O control command to execute.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
IO_Control_Command command;
stream.io_control(command);
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The I/O control command is executed (though no-op in current implementation).
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `async_connect()`, `read_some()`

### io_control

- **Signature**: `void io_control(IO_Control_Command&, error_code&)`
- **Description**: Performs an I/O control operation on the stream with error handling. This function is a no-op in the current implementation.
- **Parameters**:
  - `command` (IO_Control_Command&): The I/O control command to execute.
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
IO_Control_Command command;
error_code ec;
stream.io_control(command, ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The I/O control command is executed (though no-op in current implementation).
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `io_control()`, `async_connect()`

### non_blocking

- **Signature**: `void non_blocking(bool)`
- **Description**: Sets the non-blocking mode of the stream. This function is a no-op in the current implementation.
- **Parameters**:
  - `value` (bool): True to enable non-blocking mode, false to disable it.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
stream.non_blocking(true);
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The non-blocking mode is set to the specified value.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `non_blocking()`, `async_connect()`

### non_blocking

- **Signature**: `void non_blocking(bool, error_code&)`
- **Description**: Sets the non-blocking mode of the stream with error handling. This function is a no-op in the current implementation.
- **Parameters**:
  - `value` (bool): True to enable non-blocking mode, false to disable it.
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
bool value = true;
error_code ec;
stream.non_blocking(value, ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The non-blocking mode is set to the specified value.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `non_blocking()`, `async_connect()`

### bind

- **Signature**: `void bind(endpoint_type const& endpoint)`
- **Description**: Binds the stream to a specific endpoint. This function is a no-op in the current implementation.
- **Parameters**:
  - `endpoint` (endpoint_type const&): The endpoint to bind to.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
tcp::endpoint endpoint(ip::address::from_string("127.0.0.1"), 12345);
stream.bind(endpoint);
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The stream is bound to the specified endpoint.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `async_connect()`, `open()`

### set_option

- **Signature**: `void set_option(SettableSocketOption const&)`
- **Description**: Sets a socket option on the stream. This function is a no-op in the current implementation.
- **Parameters**:
  - `option` (SettableSocketOption const&): The socket option to set.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
tcp::no_delay option(true);
stream.set_option(option);
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The socket option is set to the specified value.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `set_option()`, `get_option()`

### set_option

- **Signature**: `void set_option(SettableSocketOption const&, error_code&)`
- **Description**: Sets a socket option on the stream with error handling. This function is a no-op in the current implementation.
- **Parameters**:
  - `option` (SettableSocketOption const&): The socket option to set.
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
tcp::no_delay option(true);
error_code ec;
stream.set_option(option, ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The socket option is set to the specified value.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `set_option()`, `get_option()`

### get_option

- **Signature**: `void get_option(GettableSocketOption&)`
- **Description**: Gets a socket option from the stream. This function is a no-op in the current implementation.
- **Parameters**:
  - `option` (GettableSocketOption&): The socket option to get.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
tcp::no_delay option;
stream.get_option(option);
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The socket option is retrieved.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_option()`, `set_option()`

### get_option

- **Signature**: `void get_option(GettableSocketOption&, error_code&)`
- **Description**: Gets a socket option from the stream with error handling. This function is a no-op in the current implementation.
- **Parameters**:
  - `option` (GettableSocketOption&): The socket option to get.
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
tcp::no_delay option;
error_code ec;
stream.get_option(option, ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The socket option is retrieved.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `get_option()`, `set_option()`

### cancel

- **Signature**: `void cancel(error_code&)`
- **Description**: Cancels all pending operations on the stream and notifies all handlers with the specified error code. This function is used to gracefully terminate ongoing operations.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
error_code ec;
stream.cancel(ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: All pending operations are canceled and handlers are notified.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `close()`, `async_connect()`

### close

- **Signature**: `void close(error_code const&)`
- **Description**: Closes the stream and performs cleanup operations. This function is a wrapper around the actual close operation.
- **Parameters**:
  - `ec` (error_code const&): Error code to store any error that occurs during the operation.
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
error_code ec;
stream.close(ec);
if (ec) {
    // Handle error
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: The stream is closed.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `cancel()`, `is_open()`

### is_open

- **Signature**: `bool is_open() const`
- **Description**: Checks whether the stream is currently open and connected.
- **Parameters**: None
- **Return Value**: True if the stream is open, false otherwise.
- **Exceptions/Errors**: None
- **Example**:
```cpp
if (stream.is_open()) {
    // Stream is open, perform operations
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns true if the stream is open.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `close()`, `open()`

### local_endpoint

- **Signature**: `endpoint_type local_endpoint() const`
- **Description**: Returns the local endpoint of the stream, which is the address and port the stream is bound to.
- **Parameters**: None
- **Return Value**: The local endpoint of the stream.
- **Exceptions/Errors**: No exceptions thrown, but may return an invalid endpoint if the stream is not bound.
- **Example**:
```cpp
auto endpoint = stream.local_endpoint();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns the local endpoint of the stream.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `remote_endpoint()`, `bind()`

### remote_endpoint

- **Signature**: `endpoint_type remote_endpoint() const`
- **Description**: Returns the remote endpoint of the stream, which is the address and port of the remote peer.
- **Parameters**: None
- **Return Value**: The remote endpoint of the stream.
- **Exceptions/Errors**: No exceptions thrown, but may return an invalid endpoint if the stream is not connected.
- **Example**:
```cpp
auto endpoint = stream.remote_endpoint();
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns the remote endpoint of the stream.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `local_endpoint()`, `async_connect()`

### available

- **Signature**: `std::size_t available(error_code& ec) const`
- **Description**: Returns the number of bytes that can be read from the stream without blocking. This function is used to check the availability of data for reading.
- **Parameters**:
  - `ec` (error_code&): Error code to store any error that occurs during the operation.
- **Return Value**: The number of bytes available for reading.
- **Exceptions/Errors**: No exceptions thrown, but error code may be set if the operation fails.
- **Example**:
```cpp
error_code ec;
std::size_t available_bytes = stream.available(ec);
if (ec) {
    // Handle error
} else {
    // Process available data
}
```
- **Preconditions**: The stream must be in a valid state.
- **Postconditions**: Returns the number of bytes available for reading.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) - Constant time operation.
- **See Also**: `read_some()`, `async_read_some()`

### async_connect

- **Signature**: `void async_connect(endpoint_type const& endpoint, Handler handler)`
- **Description**: Initiates an