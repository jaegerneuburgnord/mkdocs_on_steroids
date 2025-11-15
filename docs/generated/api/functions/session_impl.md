# libtorrent Session Implementation API Documentation

## operator (std::unique_ptr<T> const&, std::unique_ptr<T> const&)

- **Signature**: `bool operator()(std::unique_ptr<T> const& lhs, std::unique_ptr<T> const& rhs) const`
- **Description**: Compares two unique pointers by comparing their underlying raw pointers. This is used as a comparison functor for sorting or ordering unique pointers.
- **Parameters**:
  - `lhs` (std::unique_ptr<T> const&): Left-hand side unique pointer to compare
  - `rhs` (std::unique_ptr<T> const&): Right-hand side unique pointer to compare
- **Return Value**: Returns `true` if the raw pointer of `lhs` is less than the raw pointer of `rhs`, `false` otherwise.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
std::vector<std::unique_ptr<int>> vec;
// ... populate vector
std::sort(vec.begin(), vec.end(), [](const std::unique_ptr<int>& a, const std::unique_ptr<int>& b) {
    return a < b;
});
```
- **Preconditions**: Both parameters must be valid unique pointers.
- **Postconditions**: Returns the result of comparing the raw pointers.
- **Thread Safety**: Thread-safe if the underlying pointers are not modified.
- **Complexity**: O(1)
- **See Also**: `operator()(std::unique_ptr<T> const&, T*)`, `operator()(T*, std::unique_ptr<T> const&)`

## operator (std::unique_ptr<T> const&, T*)

- **Signature**: `bool operator()(std::unique_ptr<T> const& lhs, T* rhs) const`
- **Description**: Compares a unique pointer with a raw pointer by comparing their underlying addresses. This allows comparison between different pointer types.
- **Parameters**:
  - `lhs` (std::unique_ptr<T> const&): Unique pointer to compare
  - `rhs` (T*): Raw pointer to compare
- **Return Value**: Returns `true` if the raw pointer of `lhs` is less than `rhs`, `false` otherwise.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
auto ptr1 = std::make_unique<int>(42);
int val = 100;
bool result = operator()(ptr1, &val);
```
- **Preconditions**: The raw pointer `rhs` should be valid.
- **Postconditions**: Returns the result of comparing the raw pointers.
- **Thread Safety**: Thread-safe if the underlying pointers are not modified.
- **Complexity**: O(1)
- **See Also**: `operator()(std::unique_ptr<T> const&, std::unique_ptr<T> const&)`, `operator()(T*, std::unique_ptr<T> const&)`

## operator (T*, std::unique_ptr<T> const&)

- **Signature**: `bool operator()(T* lhs, std::unique_ptr<T> const& rhs) const`
- **Description**: Compares a raw pointer with a unique pointer by comparing their underlying addresses. This allows comparison between different pointer types.
- **Parameters**:
  - `lhs` (T*): Raw pointer to compare
  - `rhs` (std::unique_ptr<T> const&): Unique pointer to compare
- **Return Value**: Returns `true` if `lhs` is less than the raw pointer of `rhs`, `false` otherwise.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
int val = 42;
auto ptr2 = std::make_unique<int>(100);
bool result = operator(&(val), ptr2);
```
- **Preconditions**: The raw pointer `lhs` should be valid.
- **Postconditions**: Returns the result of comparing the raw pointers.
- **Thread Safety**: Thread-safe if the underlying pointers are not modified.
- **Complexity**: O(1)
- **See Also**: `operator()(std::unique_ptr<T> const&, T*)`, `operator()(std::unique_ptr<T> const&, std::unique_ptr<T> const&)`

## listen_socket_t()

- **Signature**: `listen_socket_t() = default;`
- **Description**: Default constructor for the listen_socket_t class. Initializes a new listen socket object.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
listen_socket_t socket;
```
- **Preconditions**: None
- **Postconditions**: A valid listen_socket_t object is created.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `listen_socket_t(listen_socket_t const&)`, `listen_socket_t(listen_socket_t&&)`

## listen_socket_t (copy constructor)

- **Signature**: `listen_socket_t(listen_socket_t const&) = delete;`
- **Description**: Deleted copy constructor to prevent copying of listen_socket_t objects. This is because listen sockets manage resources that cannot be safely duplicated.
- **Parameters**:
  - `other` (listen_socket_t const&): The listen socket to copy from
- **Return Value**: None
- **Exceptions/Errors**: Compilation error if attempted to copy.
- **Example**: Not applicable - this function is deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Not applicable
- **Complexity**: N/A
- **See Also**: `listen_socket_t()`, `listen_socket_t(listen_socket_t&&)`

## listen_socket_t (move constructor)

- **Signature**: `listen_socket_t(listen_socket_t&&) = delete;`
- **Description**: Deleted move constructor to prevent moving of listen_socket_t objects. This is because listen sockets manage resources that cannot be safely moved.
- **Parameters**:
  - `other` (listen_socket_t&&): The listen socket to move from
- **Return Value**: None
- **Exceptions/Errors**: Compilation error if attempted to move.
- **Example**: Not applicable - this function is deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Not applicable
- **Complexity**: N/A
- **See Also**: `listen_socket_t()`, `listen_socket_t(listen_socket_t const&)`

## get_local_endpoint()

- **Signature**: `udp::endpoint get_local_endpoint() override`
- **Description**: Returns the local endpoint of the UDP socket. If the UDP socket is not initialized, returns the local endpoint from the session configuration.
- **Parameters**: None
- **Return Value**: The local endpoint as a udp::endpoint object.
- **Exceptions/Errors**: If the local endpoint operation fails, an error_code is returned with the error.
- **Example**:
```cpp
auto endpoint = get_local_endpoint();
std::cout << "Local endpoint: " << endpoint.address() << ":" << endpoint.port() << std::endl;
```
- **Preconditions**: The session must be running and the UDP socket must be initialized.
- **Postconditions**: Returns the local endpoint information.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `tcp_external_port()`, `udp_external_port()`

## tcp_external_port()

- **Signature**: `int tcp_external_port()`
- **Description**: Returns the external TCP port number. If a port mapping is available, returns the mapped port; otherwise, returns the local port.
- **Parameters**: None
- **Return Value**: The external TCP port number as an integer.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
int port = tcp_external_port();
if (port != 0) {
    std::cout << "TCP external port: " << port << std::endl;
}
```
- **Preconditions**: The session must be running and port mapping must be configured.
- **Postconditions**: Returns the external TCP port number.
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) where n is the number of port mappings.
- **See Also**: `udp_external_port()`, `get_local_endpoint()`

## udp_external_port()

- **Signature**: `int udp_external_port()`
- **Description**: Returns the external UDP port number. If a port mapping is available, returns the mapped port; otherwise, returns the local port or 0 if not available.
- **Parameters**: None
- **Return Value**: The external UDP port number as an integer.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
int port = udp_external_port();
if (port != 0) {
    std::cout << "UDP external port: " << port << std::endl;
}
```
- **Preconditions**: The session must be running and port mapping must be configured.
- **Postconditions**: Returns the external UDP port number.
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) where n is the number of port mappings.
- **See Also**: `tcp_external_port()`, `get_local_endpoint()`

## listen_endpoint_t (constructor)

- **Signature**: `listen_endpoint_t(address const& adr, int p, std::string dev, transport s, listen_socket_flags_t f, address const& nmask = address{})`
- **Description**: Constructor for the listen_endpoint_t struct. Initializes a new listen endpoint with the specified parameters.
- **Parameters**:
  - `adr` (address const&): The IP address for the endpoint
  - `p` (int): The port number for the endpoint
  - `dev` (std::string): The device name for the endpoint
  - `s` (transport): The transport type for the endpoint
  - `f` (listen_socket_flags_t): The flags for the endpoint
  - `nmask` (address const&, default): The netmask for the endpoint
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
listen_endpoint_t endpoint(address::from_string("192.168.1.1"), 6881, "eth0", transport::tcp, listen_socket_flags_t::none);
```
- **Preconditions**: The address and port must be valid.
- **Postconditions**: A valid listen_endpoint_t object is created.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `listen_endpoint_t(address const& adr, int p, std::string dev, transport s, listen_socket_flags_t f, address const& nmask = address{})`

## session_impl (copy constructor)

- **Signature**: `session_impl(session_impl const&) = delete;`
- **Description**: Deleted copy constructor to prevent copying of session_impl objects. This is because sessions manage resources that cannot be safely duplicated.
- **Parameters**:
  - `other` (session_impl const&): The session to copy from
- **Return Value**: None
- **Exceptions/Errors**: Compilation error if attempted to copy.
- **Example**: Not applicable - this function is deleted.
- **Preconditions**: None
- **Postconditions**: None
- **Thread Safety**: Not applicable
- **Complexity**: N/A
- **See Also**: `session_impl()`, `session_impl(session_impl&&)`

## call_abort()

- **Signature**: `void call_abort()`
- **Description**: Initiates the abort process for the session. This function dispatches an abort operation to the IO context.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
call_abort();
```
- **Preconditions**: The session must be running.
- **Postconditions**: The abort process is initiated.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `is_aborted()`, `abort()`

## session_plugin_wrapper (constructor)

- **Signature**: `explicit session_plugin_wrapper(ext_function_t f) : m_f(std::move(f)) {}`
- **Description**: Constructor for session_plugin_wrapper. Initializes the plugin wrapper with the specified external function.
- **Parameters**:
  - `f` (ext_function_t): The external function to wrap
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
session_plugin_wrapper wrapper([](torrent_handle const& t, client_data_t const user) {
    return std::make_shared<my_torrent_plugin>();
});
```
- **Preconditions**: The function must be valid.
- **Postconditions**: A valid session_plugin_wrapper object is created.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `new_torrent()`, `is_single_thread()`

## new_torrent()

- **Signature**: `std::shared_ptr<torrent_plugin> new_torrent(torrent_handle const& t, client_data_t const user) override`
- **Description**: Creates a new torrent plugin for the specified torrent handle and user data.
- **Parameters**:
  - `t` (torrent_handle const&): The torrent handle for which to create a plugin
  - `user` (client_data_t const&): The user data to pass to the plugin
- **Return Value**: A shared pointer to the created torrent plugin.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
auto plugin = new_torrent(torrent_handle, client_data_t());
```
- **Preconditions**: The torrent handle must be valid.
- **Postconditions**: A new torrent plugin is created and returned.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `session_plugin_wrapper()`, `is_single_thread()`

## is_single_thread()

- **Signature**: `bool is_single_thread() const override`
- **Description**: Checks if the session is running in single-threaded mode.
- **Parameters**: None
- **Return Value**: `true` if the session is running in single-threaded mode, `false` otherwise.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
if (is_single_thread()) {
    std::cout << "Session is running in single-threaded mode" << std::endl;
}
```
- **Preconditions**: The session must be running.
- **Postconditions**: Returns the single-threaded status of the session.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `is_posting_torrent_updates()`, `get_peer_allocator()`

## is_posting_torrent_updates()

- **Signature**: `bool is_posting_torrent_updates() const override`
- **Description**: Checks if the session is currently posting torrent updates.
- **Parameters**: None
- **Return Value**: `true` if the session is posting torrent updates, `false` otherwise.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
if (is_posting_torrent_updates()) {
    std::cout << "Session is posting torrent updates" << std::endl;
}
```
- **Preconditions**: The session must be running.
- **Postconditions**: Returns the current status of torrent update posting.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `is_single_thread()`, `get_peer_allocator()`

## get_peer_allocator()

- **Signature**: `torrent_peer_allocator_interface& get_peer_allocator() override`
- **Description**: Returns a reference to the peer allocator interface used by the session.
- **Parameters**: None
- **Return Value**: A reference to the peer allocator interface.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
auto& allocator = get_peer_allocator();
```
- **Preconditions**: The session must be running.
- **Postconditions**: Returns a reference to the peer allocator interface.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `is_single_thread()`, `get_context()`

## get_context()

- **Signature**: `io_context& get_context() override`
- **Description**: Returns a reference to the IO context used by the session.
- **Parameters**: None
- **Return Value**: A reference to the IO context.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
auto& context = get_context();
```
- **Preconditions**: The session must be running.
- **Postconditions**: Returns a reference to the IO context.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `get_resolver()`, `torrent_list()`

## get_resolver()

- **Signature**: `resolver_interface& get_resolver() override`
- **Description**: Returns a reference to the resolver interface used by the session.
- **Parameters**: None
- **Return Value**: A reference to the resolver interface.
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
auto& resolver = get_resolver();
```
- **Preconditions**: The session must be running.
- **Postconditions**: Returns a reference to the resolver interface.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `get_context()`, `torrent_list()`

## torrent_list()

- **Signature**: `aux::vector<torrent*>& torrent_list(torrent_list_index_t i) override`
- **Description**: Returns a reference to the vector of torrents at the specified index.
- **Parameters**:
  - `i` (torrent_list_index_t): The index of the torrent list to return
- **Return Value**: A reference to the vector of torrents.
- **Exceptions/Errors**: Throws an assertion if the index is out of bounds.
- **Example**:
```cpp
auto& torrents = torrent_list(torrent_list_index_t(0));
```
- **Preconditions**: The index must be valid.
- **Postconditions**: Returns a reference to the vector of torrents.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `set_load_function()`, `num_torrents()`

## set_load_function()

- **Signature**: `TORRENT_DEPRECATED void set_load_function(user_load_function_t fun)`
- **Description**: Sets the user load function for the session. This function is deprecated and should not be used in new code.
- **Parameters**:
  - `fun` (user_load_function_t): The user load function to set
- **Return Value**: None
- **Exceptions/Errors**: No exceptions thrown.
- **Example**:
```cpp
set_load_function([](torrent_handle const& t, client_data_t const user) {
    return std::make_shared<my_torrent_plugin>();
