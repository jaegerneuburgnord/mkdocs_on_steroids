# API Documentation for libtorrent Client Test Functions

## sleep_and_input

- **Signature**: `bool sleep_and_input(int* c, lt::time_duration const sleep)`
- **Description**: Checks for keyboard input within a specified time duration. Returns true if a key was pressed, false otherwise. The function attempts to check for input multiple times within the specified duration.
- **Parameters**:
  - `c` (int*): Pointer to an integer where the pressed key will be stored. The function modifies this value if a key is pressed.
  - `sleep` (lt::time_duration const): The total duration to wait for input, divided into multiple checks.
- **Return Value**:
  - `true`: A key was pressed during the check period
  - `false`: No key was pressed within the specified time
- **Exceptions/Errors**:
  - No exceptions are thrown, but the function relies on platform-specific functions (_kbhit and _getch) that may not be available on all platforms.
- **Example**:
```cpp
int key = 0;
if (sleep_and_input(&key, lt::seconds(1))) {
    std::printf("Key pressed: %d\n", key);
} else {
    std::printf("No key pressed\n");
}
```
- **Preconditions**: The function assumes that the system supports keyboard input detection.
- **Postconditions**: If a key is pressed, the value of `c` will be set to the ASCII value of the pressed key.
- **Thread Safety**: This function is not thread-safe due to the use of global state in the keyboard input functions.
- **Complexity**: O(1) time complexity, as it performs a fixed number of checks.
- **See Also**: `set_keypress`, `print_alert`

## set_keypress (constructor)

- **Signature**: `set_keypress(std::uint8_t const mode = 0)`
- **Description**: Constructor for the `set_keypress` class that sets the terminal to non-canonical mode, allowing immediate character input without requiring the Enter key to be pressed. This is typically used to enable real-time keyboard input in a console application.
- **Parameters**:
  - `mode` (std::uint8_t const): Configuration mode flags, which can include `echo` to enable character echoing.
- **Return Value**: None (constructor).
- **Exceptions/Errors**:
  - May throw an exception if the terminal settings cannot be changed (e.g., on some platforms or with insufficient permissions).
- **Example**:
```cpp
set_keypress s_;
// The terminal is now in non-canonical mode
// When s_ is destroyed, the terminal settings are restored
```
- **Preconditions**: The function must be called from a terminal that supports terminal attribute manipulation.
- **Postconditions**: The terminal is set to non-canonical mode with the specified configuration until the object is destroyed.
- **Thread Safety**: This function is not thread-safe due to the global state modification of terminal settings.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_keypress` (destructor), `sleep_and_input`

## set_keypress (destructor)

- **Signature**: `~set_keypress()`
- **Description**: Destructor for the `set_keypress` class that restores the original terminal settings when the object is destroyed. This ensures that the terminal returns to its previous state even if the program exits unexpectedly.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**:
  - May throw an exception if the terminal settings cannot be restored.
- **Example**:
```cpp
{
    set_keypress s_;
    // Terminal is in non-canonical mode
    // When s_ goes out of scope, terminal settings are restored
}
// Terminal is back to normal
```
- **Preconditions**: The function assumes that the object was properly constructed and that terminal settings were modified.
- **Postconditions**: The terminal settings are restored to their original state.
- **Thread Safety**: This function is not thread-safe due to the global state modification of terminal settings.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_keypress` (constructor), `sleep_and_input`

## sleep_and_input

- **Signature**: `bool sleep_and_input(int* c, lt::time_duration const sleep)`
- **Description**: Checks for keyboard input within a specified time duration using file descriptor monitoring. Returns true if a key was pressed, false otherwise.
- **Parameters**:
  - `c` (int*): Pointer to an integer where the pressed key will be stored.
  - `sleep` (lt::time_duration const): The total duration to wait for input.
- **Return Value**:
  - `true`: A key was pressed during the check period
  - `false`: No key was pressed within the specified time
- **Exceptions/Errors**:
  - No exceptions are thrown, but the function relies on platform-specific functions for file descriptor monitoring.
- **Example**:
```cpp
int key = 0;
if (sleep_and_input(&key, lt::seconds(1))) {
    std::printf("Key pressed: %d\n", key);
} else {
    std::printf("No key pressed\n");
}
```
- **Preconditions**: The function assumes that the system supports file descriptor monitoring.
- **Postconditions**: If a key is pressed, the value of `c` will be set to the ASCII value of the pressed key.
- **Thread Safety**: This function is not thread-safe due to the use of global state in the file descriptor monitoring functions.
- **Complexity**: O(1) time complexity.
- **See Also**: `set_keypress`, `print_alert`

## to_hex

- **Signature**: `std::string to_hex(lt::sha1_hash const& s)`
- **Description**: Converts a SHA-1 hash to its hexadecimal string representation.
- **Parameters**:
  - `s` (lt::sha1_hash const&): The SHA-1 hash to convert.
- **Return Value**: A string containing the hexadecimal representation of the hash.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
lt::sha1_hash hash("some data");
std::string hex = to_hex(hash);
std::printf("SHA-1 hash: %s\n", hex.c_str());
```
- **Preconditions**: The input hash must be valid.
- **Postconditions**: The returned string is a valid hexadecimal representation of the hash.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `resume_file`, `is_resume_file`

## load_file

- **Signature**: `bool load_file(std::string const& filename, std::vector<char>& v, int limit = 8000000)`
- **Description**: Loads the contents of a file into a vector. The function checks the file size against a limit to prevent loading excessively large files.
- **Parameters**:
  - `filename` (std::string const&): The path to the file to load.
  - `v` (std::vector<char>&): The vector to store the file contents.
  - `limit` (int, default 8000000): The maximum file size allowed.
- **Return Value**:
  - `true`: File was successfully loaded
  - `false`: File loading failed (e.g., due to size limit, permission issues, or file not found)
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::vector<char> data;
if (load_file("example.txt", data)) {
    std::printf("File loaded successfully\n");
} else {
    std::printf("Failed to load file\n");
}
```
- **Preconditions**: The file must exist and be accessible, and the limit must be a positive value.
- **Postconditions**: If successful, the vector contains the file contents; otherwise, it remains unchanged.
- **Thread Safety**: This function is not thread-safe due to file I/O operations.
- **Complexity**: O(n) time complexity, where n is the file size.
- **See Also**: `save_file`, `resume_file`

## is_absolute_path

- **Signature**: `bool is_absolute_path(std::string const& f)`
- **Description**: Determines whether a given file path is absolute (i.e., starts with a drive letter on Windows or a root directory on Unix-like systems).
- **Parameters**:
  - `f` (std::string const&): The file path to check.
- **Return Value**:
  - `true`: The path is absolute
  - `false`: The path is relative
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
if (is_absolute_path("C:\\Windows\\System32")) {
    std::printf("Path is absolute\n");
} else {
    std::printf("Path is relative\n");
}
```
- **Preconditions**: The input string must be a valid file path.
- **Postconditions**: The function returns the result of the absolute path check.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) time complexity, where n is the length of the path string.
- **See Also**: `make_absolute_path`, `path_append`

## path_append

- **Signature**: `std::string path_append(std::string const& lhs, std::string const& rhs)`
- **Description**: Appends two path components, ensuring the correct separator is used based on the platform. Handles edge cases like empty strings and the current directory marker.
- **Parameters**:
  - `lhs` (std::string const&): The left path component.
  - `rhs` (std::string const&): The right path component.
- **Return Value**: A new string representing the combined path.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::string path = path_append("C:\\Users", "Documents");
std::printf("Path: %s\n", path.c_str());
```
- **Preconditions**: The input strings must be valid path components.
- **Postconditions**: The returned string is a properly formatted path.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) time complexity, where n is the total length of the input paths.
- **See Also**: `make_absolute_path`, `is_absolute_path`

## make_absolute_path

- **Signature**: `std::string make_absolute_path(std::string const& p)`
- **Description**: Converts a relative path to an absolute path by prepending the current working directory. The function handles both Windows and Unix-like systems.
- **Parameters**:
  - `p` (std::string const&): The path to convert to absolute.
- **Return Value**: A string representing the absolute path.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::string absolute = make_absolute_path("Documents\\example.txt");
std::printf("Absolute path: %s\n", absolute.c_str());
```
- **Preconditions**: The current working directory must be valid.
- **Postconditions**: The returned string is an absolute path.
- **Thread Safety**: This function is not thread-safe due to file system calls.
- **Complexity**: O(n) time complexity, where n is the length of the path.
- **See Also**: `path_append`, `is_absolute_path`

## print_endpoint

- **Signature**: `std::string print_endpoint(lt::tcp::endpoint const& ep)`
- **Description**: Converts a TCP endpoint to a human-readable string format, including IP address and port. Handles IPv6 addresses appropriately.
- **Parameters**:
  - `ep` (lt::tcp::endpoint const&): The TCP endpoint to convert.
- **Return Value**: A string representation of the endpoint.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
lt::tcp::endpoint ep(lt::address_v4::from_string("192.168.1.1"), 8080);
std::string endpoint_str = print_endpoint(ep);
std::printf("Endpoint: %s\n", endpoint_str.c_str());
```
- **Preconditions**: The endpoint must be valid.
- **Postconditions**: The returned string is a valid representation of the endpoint.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `peer_index`, `print_peer_info`

## peer_index

- **Signature**: `int peer_index(lt::tcp::endpoint addr, std::vector<lt::peer_info> const& peers)`
- **Description**: Finds the index of a peer with the specified endpoint in a vector of peer information.
- **Parameters**:
  - `addr` (lt::tcp::endpoint): The endpoint of the peer to find.
  - `peers` (std::vector<lt::peer_info> const&): The vector of peer information.
- **Return Value**:
  - `>= 0`: The index of the peer in the vector
  - `-1`: Peer not found
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
lt::tcp::endpoint peer_addr(lt::address_v4::from_string("192.168.1.1"), 6881);
int index = peer_index(peer_addr, peers);
if (index >= 0) {
    std::printf("Peer found at index %d\n", index);
} else {
    std::printf("Peer not found\n");
}
```
- **Preconditions**: The vector of peers must be valid and contain peer information.
- **Postconditions**: The function returns the index of the peer or -1 if not found.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) time complexity, where n is the number of peers.
- **See Also**: `print_peer_info`, `print_endpoint`

## base32encode_i2p

- **Signature**: `void base32encode_i2p(lt::sha256_hash const& s, std::string& out, int limit)`
- **Description**: Encodes a SHA-256 hash into a base32 string format, typically used for I2P addresses. The function ensures the output is limited to a specified length.
- **Parameters**:
  - `s` (lt::sha256_hash const&): The hash to encode.
  - `out` (std::string&): The output string where the encoded result will be stored.
  - `limit` (int): The maximum length of the output string.
- **Return Value**: None (modifies the output string).
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
lt::sha256_hash hash("some data");
std::string encoded;
base32encode_i2p(hash, encoded, 32);
std::printf("Encoded: %s\n", encoded.c_str());
```
- **Preconditions**: The hash must be valid, and the limit must be a positive value.
- **Postconditions**: The output string contains the base32-encoded hash.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) time complexity, where n is the length of the hash.
- **See Also**: `to_hex`, `is_resume_file`

## print_peer_info

- **Signature**: `int print_peer_info(std::string& out, std::vector<lt::peer_info> const& peers, int max_lines)`
- **Description**: Generates a formatted string containing information about peers, including IP addresses, download progress, and other statistics. The function limits the output to a specified number of lines.
- **Parameters**:
  - `out` (std::string&): The output string where the formatted peer information will be appended.
  - `peers` (std::vector<lt::peer_info> const&): The vector of peer information.
  - `max_lines` (int): The maximum number of lines to output.
- **Return Value**: The number of lines actually printed.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::string output;
int lines_printed = print_peer_info(output, peers, 10);
std::printf("Printed %d lines\n", lines_printed);
std::printf("%s\n", output.c_str());
```
- **Preconditions**: The vector of peers must be valid.
- **Postconditions**: The output string contains the formatted peer information.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(n) time complexity, where n is the number of peers.
- **See Also**: `peer_index`, `print_peer_legend`

## print_peer_legend

- **Signature**: `int print_peer_legend(std::string& out, int max_lines)`
- **Description**: Prints a legend for the peer information output, explaining the meaning of different columns and symbols. The function limits the output to a specified number of lines.
- **Parameters**:
  - `out` (std::string&): The output string where the legend will be appended.
  - `max_lines` (int): The maximum number of lines to output.
- **Return Value**: The number of lines actually printed.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
std::string output;
int lines_printed = print_peer_legend(output, 5);
std::printf("Printed %d lines\n", lines_printed);
std::printf("%s\n", output.c_str());
```
- **Preconditions**: None.
- **Postconditions**: The output string contains the legend.
- **Thread Safety**: This function is thread-safe.
- **Complexity**: O(1) time complexity.
- **See Also**: `print_peer_info`, `print_usage`

## signal_handler

- **Signature**: `void signal_handler(int)`
- **Description**: Signal handler function that sets a global flag (`quit`) to true when a signal is received, typically to terminate the program gracefully.
- **Parameters**:
  - `int`: The signal number (unused in this implementation).
- **Return Value**: None.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
signal(SIGINT, signal_handler);
// When Ctrl+C is pressed, quit will be set to true
```
- **Preconditions**: The signal must be valid and the function must be registered as a handler.
- **Postconditions**: The `quit`