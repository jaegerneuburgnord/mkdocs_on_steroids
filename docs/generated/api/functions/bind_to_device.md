# API Documentation: bind_to_device

## bind_to_device (Constructor)

- **Signature**: `explicit bind_to_device(char const* device)`
- **Description**: Constructs a `bind_to_device` option object that can be used to bind a socket to a specific network interface by its name. This option is typically used with `boost::asio::socket` or similar socket types.
- **Parameters**:
  - `device` (char const*): A null-terminated string representing the name of the network interface (e.g., "eth0", "wlan0"). The string must remain valid for the lifetime of the option object. Must not be null.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device device_option("eth0");
// Use device_option with a socket
```
- **Preconditions**: `device` must be a valid null-terminated string.
- **Postconditions**: The option object is initialized with the specified device name.
- **Thread Safety**: Thread-safe as it's a constructor.
- **Complexity**: O(1)
- **See Also**: `bind_device`, `bind_to_device` (overload with unsigned int)

## level

- **Signature**: `int level(Protocol const&) const`
- **Description**: Returns the socket level at which the option should be applied. This is typically `SOL_SOCKET` for socket-level options or `IPPROTO_IP` for IP-level options.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns the socket level (either `SOL_SOCKET` or `IPPROTO_IP` depending on the specific overload).
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
int level_value = option.level(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct socket level for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `name`, `data`, `size`

## name

- **Signature**: `int name(Protocol const&) const`
- **Description**: Returns the option name (SO_BINDTODEVICE or IP_BOUND_IF) that should be used with the socket's `set_option` method.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns the option name (SO_BINDTODEVICE or IP_BOUND_IF) depending on the specific overload.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
int option_name = option.name(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct option name for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `data`, `size`

## data

- **Signature**: `char const* data(Protocol const&) const`
- **Description**: Returns a pointer to the data associated with the option. For string-based options, this returns the device name string.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns a pointer to the device name string.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
char const* device_name = option.data(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns a pointer to the device name string.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `size`

## size

- **Signature**: `size_t size(Protocol const&) const`
- **Description**: Returns the size of the data associated with the option in bytes. This is used by the socket system to know how much data to pass to the underlying system call.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns the size of the device name string in bytes, including the null terminator.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
size_t data_size = option.size(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct size of the device name string.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `data`

## bind_device

- **Signature**: `void bind_device(T& sock, char const* device, error_code& ec)`
- **Description**: Binds a socket to a specific network interface by its name using the `bind_to_device` option.
- **Parameters**:
  - `sock` (T&): A reference to the socket object (e.g., `boost::asio::ip::tcp::socket`) that should be bound to the specified device.
  - `device` (char const*): A null-terminated string representing the name of the network interface (e.g., "eth0", "wlan0"). Must not be null.
  - `ec` (error_code&): An error code object that will be set to indicate any errors that occur during the operation.
- **Return Value**: None
- **Exceptions/Errors**: 
  - If the device name is invalid or not found, `ec` will be set to the corresponding error code (typically `ENOENT` or similar).
  - If the socket operation fails, `ec` will be set to the appropriate error code.
- **Example**:
```cpp
boost::asio::ip::tcp::socket socket(io_context);
error_code ec;
bind_device(socket, "eth0", ec);
if (ec) {
    std::cerr << "Failed to bind to device: " << ec.message() << std::endl;
}
```
- **Preconditions**: 
  - `sock` must be a valid socket object.
  - `device` must be a valid null-terminated string.
  - `ec` must be a valid error_code object.
- **Postconditions**: 
  - If successful, the socket is bound to the specified device.
  - If failed, `ec` contains the error code describing the failure.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bind_to_device` (constructor), `bind_to_device` (overload with unsigned int)

## bind_to_device (Constructor)

- **Signature**: `explicit bind_to_device(unsigned int idx)`
- **Description**: Constructs a `bind_to_device` option object that can be used to bind a socket to a specific network interface by its interface index.
- **Parameters**:
  - `idx` (unsigned int): The interface index of the network interface (e.g., the value returned by `if_nametoindex`).
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device device_option(3);
// Use device_option with a socket
```
- **Preconditions**: `idx` must be a valid interface index.
- **Postconditions**: The option object is initialized with the specified interface index.
- **Thread Safety**: Thread-safe as it's a constructor.
- **Complexity**: O(1)
- **See Also**: `bind_device`, `bind_to_device` (overload with char const*)

## level

- **Signature**: `int level(Protocol const&) const`
- **Description**: Returns the socket level at which the option should be applied. For this overload, it returns `IPPROTO_IP`.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns `IPPROTO_IP`.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option(3);
int level_value = option.level(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct socket level for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `name`, `data`, `size`

## name

- **Signature**: `int name(Protocol const&) const`
- **Description**: Returns the option name (IP_BOUND_IF) that should be used with the socket's `set_option` method.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns `IP_BOUND_IF`.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option(3);
int option_name = option.name(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct option name for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `data`, `size`

## data

- **Signature**: `char const* data(Protocol const&) const`
- **Description**: Returns a pointer to the data associated with the option. For interface index-based options, this returns a pointer to the interface index.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns a pointer to the interface index.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option(3);
char const* interface_index = option.data(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns a pointer to the interface index.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `size`

## size

- **Signature**: `size_t size(Protocol const&) const`
- **Description**: Returns the size of the data associated with the option in bytes. This is used by the socket system to know how much data to pass to the underlying system call.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns the size of the interface index in bytes.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option(3);
size_t data_size = option.size(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct size of the interface index.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `data`

## bind_device

- **Signature**: `void bind_device(T& sock, char const* device, error_code& ec)`
- **Description**: Binds a socket to a specific network interface by its name using the `bind_to_device` option with interface index resolution.
- **Parameters**:
  - `sock` (T&): A reference to the socket object (e.g., `boost::asio::ip::tcp::socket`) that should be bound to the specified device.
  - `device` (char const*): A null-terminated string representing the name of the network interface (e.g., "eth0", "wlan0"). Must not be null.
  - `ec` (error_code&): An error code object that will be set to indicate any errors that occur during the operation.
- **Return Value**: None
- **Exceptions/Errors**: 
  - If the device name is invalid or not found, `ec` will be set to the corresponding error code (typically `ENOENT` or similar).
  - If the socket operation fails, `ec` will be set to the appropriate error code.
- **Example**:
```cpp
boost::asio::ip::tcp::socket socket(io_context);
error_code ec;
bind_device(socket, "eth0", ec);
if (ec) {
    std::cerr << "Failed to bind to device: " << ec.message() << std::endl;
}
```
- **Preconditions**: 
  - `sock` must be a valid socket object.
  - `device` must be a valid null-terminated string.
  - `ec` must be a valid error_code object.
- **Postconditions**: 
  - If successful, the socket is bound to the specified device.
  - If failed, `ec` contains the error code describing the failure.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `bind_to_device` (constructor), `bind_to_device` (overload with unsigned int)

## bind_to_device (Constructor)

- **Signature**: `explicit bind_to_device(char const* device)`
- **Description**: Constructs a `bind_to_device` option object that can be used to bind a socket to a specific network interface by its name. This option is typically used with `boost::asio::socket` or similar socket types.
- **Parameters**:
  - `device` (char const*): A null-terminated string representing the name of the network interface (e.g., "eth0", "wlan0"). The string must remain valid for the lifetime of the option object. Must not be null.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device device_option("eth0");
// Use device_option with a socket
```
- **Preconditions**: `device` must be a valid null-terminated string.
- **Postconditions**: The option object is initialized with the specified device name.
- **Thread Safety**: Thread-safe as it's a constructor.
- **Complexity**: O(1)
- **See Also**: `bind_device`, `bind_to_device` (overload with unsigned int)

## level

- **Signature**: `int level(Protocol const&) const`
- **Description**: Returns the socket level at which the option should be applied. This is typically `SOL_SOCKET` for socket-level options.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns `SOL_SOCKET`.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
int level_value = option.level(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct socket level for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `name`, `data`, `size`

## name

- **Signature**: `int name(Protocol const&) const`
- **Description**: Returns the option name (IP_FORCE_OUT_IFP) that should be used with the socket's `set_option` method.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns `IP_FORCE_OUT_IFP`.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
int option_name = option.name(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct option name for the option.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `data`, `size`

## data

- **Signature**: `char const* data(Protocol const&) const`
- **Description**: Returns a pointer to the data associated with the option. For string-based options, this returns the device name string.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns a pointer to the device name string.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
char const* device_name = option.data(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns a pointer to the device name string.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `size`

## size

- **Signature**: `size_t size(Protocol const&) const`
- **Description**: Returns the size of the data associated with the option in bytes. This is used by the socket system to know how much data to pass to the underlying system call.
- **Parameters**:
  - `Protocol` (Protocol const&): A protocol parameter that is part of the template instantiation. This parameter is not used in the implementation but serves as a type constraint.
- **Return Value**: Returns the size of the device name string in bytes, including the null terminator.
- **Exceptions/Errors**: None
- **Example**:
```cpp
bind_to_device option("eth0");
size_t data_size = option.size(Protocol());
```
- **Preconditions**: None
- **Postconditions**: Returns the correct size of the device name string.
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `level`, `name`, `data`

## bind_device

- **Signature**: `void bind_device(T& sock, char const* device, error_code& ec)`
- **Description**: Binds a socket to a specific network interface by its name using the `bind_to_device` option.
- **Parameters**:
  - `sock` (T&): A reference to the socket object (e.g., `boost::asio::ip::tcp::socket`) that should be bound to the specified device.
  - `device` (char const*): A null-terminated string representing the name of the network interface (e.g., "eth0", "wlan0"). Must not be null.
