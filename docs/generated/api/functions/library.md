# libtorrent C++ Bindings API Documentation

## find_handle

- **Signature**: `int find_handle(lt::torrent_handle h)`
- **Description**: Searches for a torrent handle in the global handles vector and returns its index. This function is used internally to map between a handle index and the actual torrent handle object.
- **Parameters**:
  - `h` (lt::torrent_handle): The torrent handle to search for in the global handles vector. This handle must have been previously added using `add_handle`.
- **Return Value**:
  - Returns the index of the handle in the handles vector if found
  - Returns -1 if the handle is not found in the vector
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 when the handle is not found (valid return value, not an error)
- **Example**:
```cpp
int index = find_handle(my_handle);
if (index != -1) {
    // Handle found at index
    lt::torrent_handle found_handle = get_handle(index);
}
```
- **Preconditions**: The handle must have been previously added to the handles vector using `add_handle`
- **Postconditions**: Returns the index of the handle if found, otherwise returns -1
- **Thread Safety**: Not thread-safe - concurrent access to the handles vector requires synchronization
- **Complexity**: O(n) where n is the number of handles in the vector
- **See Also**: `get_handle()`, `add_handle()`

## get_handle

- **Signature**: `lt::torrent_handle get_handle(int i)`
- **Description**: Retrieves a torrent handle from the global handles vector by index. This function is used to convert a handle index back into a valid torrent handle object.
- **Parameters**:
  - `i` (int): The index of the handle in the handles vector. Must be between 0 and handles.size() - 1.
- **Return Value**:
  - Returns the torrent handle at the specified index if valid
  - Returns a default-constructed lt::torrent_handle if the index is invalid
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns a default-constructed handle if index is out of bounds
- **Example**:
```cpp
lt::torrent_handle handle = get_handle(5);
if (handle.is_valid()) {
    // Handle is valid, can use it
    handle.pause();
}
```
- **Preconditions**: The handle at index i must have been previously added to the handles vector
- **Postconditions**: Returns a valid handle if index is valid, otherwise returns a default-constructed handle
- **Thread Safety**: Not thread-safe - concurrent access to the handles vector requires synchronization
- **Complexity**: O(1) - direct access to vector element
- **See Also**: `find_handle()`, `add_handle()`

## add_handle

- **Signature**: `int add_handle(lt::torrent_handle const& h)`
- **Description**: Adds a torrent handle to the global handles vector. This function searches for an unused slot (marked by an invalid handle) and replaces it with the new handle. If no unused slots are found, the handle is added to the end of the vector.
- **Parameters**:
  - `h` (lt::torrent_handle const&): The torrent handle to add to the handles vector. This handle must be valid.
- **Return Value**:
  - Returns the index where the handle was added if successful
  - Returns -1 if there's an error (though no explicit error condition is shown in the code)
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if there's an error (though the code shows incomplete return)
- **Example**:
```cpp
int index = add_handle(new_handle);
if (index != -1) {
    // Handle added successfully at index
    // Can now use get_handle(index) to retrieve it
}
```
- **Preconditions**: The handle must be valid and the handles vector must be accessible
- **Postconditions**: The handle is added to the handles vector at the specified index, and the function returns that index
- **Thread Safety**: Not thread-safe - concurrent access to the handles vector requires synchronization
- **Complexity**: O(n) where n is the number of handles in the vector (due to the find_if operation)
- **See Also**: `find_handle()`, `get_handle()`

## set_int_value

- **Signature**: `int set_int_value(void* dst, int* size, int val)`
- **Description**: Copies an integer value to a destination buffer, ensuring the buffer is large enough. This function is used to safely copy integer values to user-provided buffers.
- **Parameters**:
  - `dst` (void*): Pointer to the destination buffer where the integer will be copied
  - `size` (int*): Pointer to the size of the destination buffer. On input, this should contain the available size. On output, it will contain the actual size written
  - `val` (int): The integer value to copy to the destination buffer
- **Return Value**:
  - Returns 0 on success
  - Returns -2 if the destination buffer is too small to hold the integer
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -2 if the destination buffer is too small
- **Example**:
```cpp
int result;
int buffer[1];
int buffer_size = sizeof(buffer);
int error = set_int_value(buffer, &buffer_size, 42);
if (error == 0) {
    // Successfully wrote 42 to buffer
    // buffer_size now contains the actual size written (4 bytes)
}
```
- **Preconditions**: `dst` must point to a valid memory location, `size` must point to a valid integer, and `size` must be at least the size of an int
- **Postconditions**: The integer value is copied to the destination buffer if there's enough space, and `size` is updated to reflect the actual size written
- **Thread Safety**: Thread-safe - no shared state modified
- **Complexity**: O(1) - simple memory copy operation
- **See Also**: `copy_proxy_setting()`

## copy_proxy_setting

- **Signature**: `void copy_proxy_setting(lt::proxy_settings* s, proxy_setting const* ps)`
- **Description**: Copies proxy settings from a C-style structure to a libtorrent proxy_settings structure. This function handles the conversion of string fields and enum values between the two structures.
- **Parameters**:
  - `s` (lt::proxy_settings*): Pointer to the destination libtorrent proxy_settings structure
  - `ps` (proxy_setting const*): Pointer to the source C-style proxy_setting structure
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions thrown
  - No error codes returned
- **Example**:
```cpp
lt::proxy_settings target;
proxy_setting source;
// Fill source with proxy configuration
copy_proxy_setting(&target, &source);
// target now contains the same proxy settings as source
```
- **Preconditions**: Both pointers must be valid and point to properly initialized structures
- **Postconditions**: The destination proxy_settings structure contains the same settings as the source proxy_setting structure
- **Thread Safety**: Thread-safe - no shared state modified
- **Complexity**: O(1) - simple field-by-field copy
- **See Also**: `set_int_value()`

## session_create

- **Signature**: `TORRENT_EXPORT void* session_create(int tag, ...)`
- **Description**: Creates a new libtorrent session with the specified configuration parameters. This function initializes a libtorrent session with the given settings and returns a handle to it.
- **Parameters**:
  - `tag` (int): The first tag in a variable argument list. The function uses this to determine the type of subsequent parameters
  - `...`: Variable arguments following the tag, which specify the session configuration parameters
- **Return Value**:
  - Returns a pointer to the newly created session if successful
  - Returns nullptr if session creation fails
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns nullptr if session creation fails
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, SET_NUM_CONNECTIONS, 100, TAG_END);
if (session) {
    // Session created successfully
    // Use the session handle for other operations
}
```
- **Preconditions**: Valid tag values must be provided, and the variable arguments must be appropriate for the given tags
- **Postconditions**: A new session is created and initialized with the specified parameters
- **Thread Safety**: Not thread-safe - concurrent session creation requires synchronization
- **Complexity**: O(1) - simple initialization operations
- **See Also**: `session_close()`, `session_add_torrent()`

## session_close

- **Signature**: `TORRENT_EXPORT void session_close(void* ses)`
- **Description**: Closes and destroys a libtorrent session. This function frees all resources associated with the session and invalidates the session handle.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle to close
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions thrown
  - The function does not check for null pointers, so passing a null pointer may result in undefined behavior
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
// ... use session ...
session_close(session);
// Session is now closed and cannot be used again
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The session is destroyed and all associated resources are freed
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple deletion operation
- **See Also**: `session_create()`, `session_add_torrent()`

## session_add_torrent

- **Signature**: `TORRENT_EXPORT int session_add_torrent(void* ses, int tag, ...)`
- **Description**: Adds a torrent to the session. This function takes various parameters to configure the torrent and adds it to the session for download.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle
  - `tag` (int): The first tag in a variable argument list. The function uses this to determine the type of subsequent parameters
  - `...`: Variable arguments following the tag, which specify the torrent configuration parameters
- **Return Value**:
  - Returns 0 on success
  - Returns -1 if there's an error
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if there's an error adding the torrent
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
int result = session_add_torrent(session, ADD_TORRENT, "torrent_file_path", 100, TAG_END);
if (result == 0) {
    // Torrent added successfully
}
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The torrent is added to the session and can be downloaded
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple addition to the session
- **See Also**: `session_remove_torrent()`, `session_get_status()`

## session_remove_torrent

- **Signature**: `TORRENT_EXPORT void session_remove_torrent(void* ses, int tor, int flags)`
- **Description**: Removes a torrent from the session. This function takes a torrent handle and removes it from the session, optionally with flags to control the removal behavior.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle
  - `tor` (int): The torrent handle index to remove
  - `flags` (int): Flags to control the removal behavior (e.g., whether to remove the torrent completely or just stop it)
- **Return Value**: None
- **Exceptions/Errors**:
  - No exceptions thrown
  - The function does not check for null pointers, so passing invalid parameters may result in undefined behavior
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
// ... add torrents ...
session_remove_torrent(session, 0, 0); // Remove first torrent
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The torrent is removed from the session
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple removal operation
- **See Also**: `session_add_torrent()`, `session_pop_alert()`

## session_pop_alert

- **Signature**: `TORRENT_EXPORT int session_pop_alert(void* ses, char* dest, int len, int* category)`
- **Description**: Retrieves the next alert from the session's alert queue. This function removes the alert from the queue and copies its message to the provided buffer.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle
  - `dest` (char*): Pointer to the destination buffer for the alert message
  - `len` (int): Size of the destination buffer
  - `category` (int*): Pointer to store the alert category
- **Return Value**:
  - Returns 0 on success
  - Returns -1 if there are no alerts in the queue
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if there are no alerts in the queue
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
char buffer[256];
int category;
int result = session_pop_alert(session, buffer, sizeof(buffer), &category);
if (result == 0) {
    // Alert retrieved successfully
    printf("Alert: %s, Category: %d\n", buffer, category);
}
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The alert is removed from the queue and its message is copied to the destination buffer
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple queue operation
- **See Also**: `session_create()`, `session_get_status()`

## session_set_settings

- **Signature**: `TORRENT_EXPORT int session_set_settings(void* ses, int tag, ...)`
- **Description**: Sets session-wide settings. This function takes various parameters to configure the session's behavior.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle
  - `tag` (int): The first tag in a variable argument list. The function uses this to determine the type of subsequent parameters
  - `...`: Variable arguments following the tag, which specify the session configuration parameters
- **Return Value**:
  - Returns 0 on success
  - Returns -1 if there's an error
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if there's an error setting the settings
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
int result = session_set_settings(session, SET_UPLOAD_RATE_LIMIT, 1000, SET_DOWNLOAD_RATE_LIMIT, 2000, TAG_END);
if (result == 0) {
    // Settings applied successfully
}
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The session settings are updated with the specified values
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple setting operations
- **See Also**: `session_get_setting()`, `session_get_status()`

## session_get_setting

- **Signature**: `TORRENT_EXPORT int session_get_setting(void* ses, int tag, void* value, int* value_size)`
- **Description**: Retrieves session-wide settings. This function gets the current value of various session settings.
- **Parameters**:
  - `ses` (void*): Pointer to the session handle
  - `tag` (int): The setting to retrieve (e.g., upload rate limit)
  - `value` (void*): Pointer to the destination buffer for the setting value
  - `value_size` (int*): Pointer to the size of the destination buffer
- **Return Value**:
  - Returns 0 on success
  - Returns -1 if there's an error
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if there's an error retrieving the setting
- **Example**:
```cpp
void* session = session_create(SET_LISTEN_PORT, 6881, TAG_END);
int upload_limit;
int buffer_size = sizeof(upload_limit);
int result = session_get_setting(session, SET_UPLOAD_RATE_LIMIT, &upload_limit, &buffer_size);
if (result == 0) {
    // Successfully retrieved upload limit
    printf("Upload limit: %d\n", upload_limit);
}
```
- **Preconditions**: The session pointer must be valid and created by `session_create`
- **Postconditions**: The setting value is copied to the destination buffer
- **Thread Safety**: Not thread-safe - concurrent access to the same session requires synchronization
- **Complexity**: O(1) - simple retrieval operation
- **See Also**: `session_set_settings()`, `session_get_status()`

## session_get_status

- **Signature**: `TORRENT_EXPORT int session_get_status(void* sesptr, struct session_status* s, int struct_size)`
- **Description**: Retrieves the current status of the session. This function returns various statistics about the session's current state.
- **Parameters**:
  - `sesptr` (void*): Pointer to the session handle
  - `s` (struct session_status*): Pointer to the destination structure to fill with status information
  - `struct_size` (int): Size of the destination structure
- **Return Value**:
  - Returns 0 on success
  - Returns -1 if the structure size doesn't match
- **Exceptions/Errors**:
  - No exceptions thrown
  - Returns -1 if the structure size doesn't match
- **Example**