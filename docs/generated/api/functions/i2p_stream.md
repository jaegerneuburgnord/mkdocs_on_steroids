# libtorrent I2P Stream API Documentation

## Function Reference

### get_i2p_category
- **Signature**: `auto get_i2p_category()`
- **Description**: Returns a reference to the I2P error category, which is used to provide error messages specific to the I2P protocol. This function is deprecated and should not be used in new code.
- **Parameters**: None
- **Return Value**: `boost::system::error_category&` - Reference to the I2P error category
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto& category = get_i2p_category();
```
- **Preconditions**: None
- **Postconditions**: Returns a valid reference to the I2P error category
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `i2p_category()`

### i2p_stream
- **Signature**: `auto i2p_stream()`
- **Description**: Default move constructor for the `i2p_stream` class. This allows the stream to be moved from one object to another efficiently.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream1;
i2p_stream stream2 = std::move(stream1);
```
- **Preconditions**: None
- **Postconditions**: The source stream is in a valid but unspecified state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `i2p_stream(const i2p_stream&)`, `~i2p_stream()`

### set_command
- **Signature**: `auto set_command(command_t c)`
- **Description**: Sets the command type for the I2P stream operation. This is used to specify what type of operation (e.g., connect, accept, create session) should be performed.
- **Parameters**:
  - `c` (command_t): The command type to set. Valid values are defined in the `command_t` enum.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
stream.set_command(command_t::connect);
```
- **Preconditions**: None
- **Postconditions**: The command type is set to the specified value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `command_t`

### set_session_options
- **Signature**: `auto set_session_options(i2p_session_options const& session_options)`
- **Description**: Sets the session options for the I2P stream. These options control the behavior of the I2P session, such as encryption settings and lease sets.
- **Parameters**:
  - `session_options` (i2p_session_options const&): The session options to set
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
i2p_session_options options;
options.encryption_type = i2p_session_options::encryption_type::aes128;
stream.set_session_options(options);
```
- **Preconditions**: None
- **Postconditions**: The session options are set to the specified values
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `i2p_session_options`

### set_session_id
- **Signature**: `auto set_session_id(char const* id)`
- **Description**: Sets the session ID for the I2P stream. The session ID is used to identify the session in I2P communications.
- **Parameters**:
  - `id` (char const*): The session ID to set. Must be a null-terminated string.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
stream.set_session_id("session123");
```
- **Preconditions**: `id` must not be null
- **Postconditions**: The session ID is set to the specified value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `session_id()`

### set_local_i2p_endpoint
- **Signature**: `auto set_local_i2p_endpoint(string_view d)`
- **Description**: Sets the local I2P endpoint for the stream. This is used to specify the local I2P address when connecting to a remote peer.
- **Parameters**:
  - `d` (string_view): The local I2P endpoint to set. Must be a valid string_view.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
stream.set_local_i2p_endpoint("mylocal.i2p");
```
- **Preconditions**: `d` must be valid and non-empty
- **Postconditions**: The local I2P endpoint is set to the specified value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `local_i2p_endpoint()`

### local_i2p_endpoint
- **Signature**: `auto local_i2p_endpoint()`
- **Description**: Returns the local I2P endpoint for the stream. This is the I2P address that the stream is using for local communication.
- **Parameters**: None
- **Return Value**: `std::string const&` - The local I2P endpoint
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
std::string endpoint = stream.local_i2p_endpoint();
```
- **Preconditions**: None
- **Postconditions**: Returns the current local I2P endpoint
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `set_local_i2p_endpoint()`

### set_destination
- **Signature**: `auto set_destination(string_view d)`
- **Description**: Sets the destination for the I2P stream. This is the I2P address of the remote peer that the stream will connect to.
- **Parameters**:
  - `d` (string_view): The destination to set. Must be a valid string_view.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
stream.set_destination("remotepeer.i2p");
```
- **Preconditions**: `d` must be valid and non-empty
- **Postconditions**: The destination is set to the specified value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `destination()`

### destination
- **Signature**: `auto destination()`
- **Description**: Returns the destination for the I2P stream. This is the I2P address of the remote peer that the stream is connected to.
- **Parameters**: None
- **Return Value**: `std::string const&` - The destination
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
std::string dest = stream.destination();
```
- **Preconditions**: None
- **Postconditions**: Returns the current destination
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `set_destination()`

### async_connect
- **Signature**: `auto async_connect(endpoint_type const&, Handler h)`
- **Description**: Initiates an asynchronous connection to a remote I2P peer. The function uses the SAM bridge to establish the connection.
- **Parameters**:
  - `endpoint` (endpoint_type const&): The endpoint to connect to. This is ignored as the connection uses the destination set in the stream.
  - `h` (Handler): The handler to call when the connection is established or fails.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (ec) {
        // handle error
    } else {
        // connection successful
    }
};
stream.async_connect(endpoint_type(), handler);
```
- **Preconditions**: The stream must be in a valid state
- **Postconditions**: The connection process is initiated
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `do_connect()`, `connected()`

### name_lookup
- **Signature**: `auto name_lookup()`
- **Description**: Returns the current name lookup value for the I2P stream. This is used for naming lookup operations.
- **Parameters**: None
- **Return Value**: `std::string` - The current name lookup value
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
std::string name = stream.name_lookup();
```
- **Preconditions**: None
- **Postconditions**: Returns the current name lookup value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `set_name_lookup()`

### set_name_lookup
- **Signature**: `auto set_name_lookup(char const* name)`
- **Description**: Sets the name lookup value for the I2P stream. This is used for naming lookup operations.
- **Parameters**:
  - `name` (char const*): The name lookup value to set. Must be a null-terminated string.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
stream.set_name_lookup("myname");
```
- **Preconditions**: `name` must not be null
- **Postconditions**: The name lookup value is set to the specified value
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `name_lookup()`

### send_name_lookup
- **Signature**: `auto send_name_lookup(Handler h)`
- **Description**: Sends a name lookup command to the SAM bridge to resolve a name. This is used to resolve I2P names to addresses.
- **Parameters**:
  - `h` (Handler): The handler to call when the name lookup is complete.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec, char const* dst) {
    if (!ec) {
        // name lookup successful
    }
};
stream.send_name_lookup(handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The name lookup command is sent to the SAM bridge
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `do_name_lookup()`, `on_name_lookup()`

### do_connect
- **Signature**: `auto do_connect(error_code const& e, tcp::resolver::results_type ips, Handler h)`
- **Description**: Completes the connection process by connecting to the resolved IP addresses. This function is called after the name resolution is complete.
- **Parameters**:
  - `e` (error_code const&): The error code from the previous operation. If non-zero, the connection fails.
  - `ips` (tcp::resolver::results_type): The resolved IP addresses to connect to.
  - `h` (Handler): The handler to call when the connection is complete.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // connection successful
    }
};
// Assuming e and ips are obtained from a previous operation
stream.do_connect(e, ips, handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The connection process is completed
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `async_connect()`, `connected()`

### connected
- **Signature**: `auto connected(error_code const& e, Handler h)`
- **Description**: Handles the connection result and sends the hello command to the remote peer. This function is called after the connection is established.
- **Parameters**:
  - `e` (error_code const&): The error code from the connection attempt.
  - `h` (Handler): The handler to call when the operation is complete.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // connection successful
    }
};
// Assuming e is obtained from a previous operation
stream.connected(e, handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The hello command is sent to the remote peer
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `do_connect()`, `start_read_line()`

### start_read_line
- **Signature**: `auto start_read_line(error_code const& e, Handler h)`
- **Description**: Begins reading a line from the I2P stream. This function is used to read responses from the SAM bridge.
- **Parameters**:
  - `e` (error_code const&): The error code from the previous operation.
  - `h` (Handler): The handler to call when the read operation is complete.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // read successful
    }
};
// Assuming e is obtained from a previous operation
stream.start_read_line(e, handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The read operation is initiated
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `read_line()`, `async_read()`

### read_line
- **Signature**: `auto read_line(error_code const& e, Handler h)`
- **Description**: Reads a line from the I2P stream and processes it. This function is used to process responses from the SAM bridge.
- **Parameters**:
  - `e` (error_code const&): The error code from the previous operation.
  - `h` (Handler): The handler to call when the read operation is complete.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // read successful
    }
};
// Assuming e is obtained from a previous operation
stream.read_line(e, handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The line is read and processed
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `start_read_line()`, `async_read()`

### send_connect
- **Signature**: `auto send_connect(Handler h)`
- **Description**: Sends a connect command to the SAM bridge to establish a connection to a remote I2P peer.
- **Parameters**:
  - `h` (Handler): The handler to call when the command is sent.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // connect command sent successfully
    }
};
stream.send_connect(handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The connect command is sent to the SAM bridge
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `send_accept()`, `send_session_create()`

### send_accept
- **Signature**: `auto send_accept(Handler h)`
- **Description**: Sends an accept command to the SAM bridge to accept an incoming connection.
- **Parameters**:
  - `h` (Handler): The handler to call when the command is sent.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // accept command sent successfully
    }
};
stream.send_accept(handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The accept command is sent to the SAM bridge
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `send_connect()`, `send_session_create()`

### send_session_create
- **Signature**: `auto send_session_create(Handler h)`
- **Description**: Sends a session create command to the SAM bridge to create a new I2P session.
- **Parameters**:
  - `h` (Handler): The handler to call when the command is sent.
- **Return Value**: None
- **Exceptions/Errors**: None
- **Example**:
```cpp
i2p_stream stream;
auto handler = [](error_code const& ec) {
    if (!ec) {
        // session create command sent successfully
    }
};
stream.send_session_create(handler);
```
- **Preconditions**: The stream must be in a valid state and `m_magic` must be 0x1337
- **Postconditions**: The session create command is sent to the SAM bridge
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `send_connect()`, `send_accept()`

### is_open
- **Signature**: `auto is_open() const`
- **Description**: Checks if the I2P stream is open and connected to the SAM bridge.
- **Parameters**: None
- **Return Value**: `bool` - True if the stream is open, false otherwise
- **Exceptions/Errors**: None
- **Example**:
```