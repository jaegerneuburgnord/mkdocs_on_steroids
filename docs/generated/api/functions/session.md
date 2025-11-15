# libtorrent Python Bindings API Documentation

## Function: get_pointer

- **Signature**: `auto get_pointer()`
- **Description**: This function returns a pointer to an alert object. It's a simple wrapper that returns the input pointer unchanged.
- **Parameters**: 
  - `p` (lt::alert const volatile*): The alert pointer to be returned
- **Return Value**: 
  - Returns the same pointer passed as the argument
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
auto alert_ptr = get_pointer(my_alert);
```
- **Preconditions**: The input pointer must be valid
- **Postconditions**: Returns the same pointer that was passed in
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: listen_on

- **Signature**: `void listen_on(lt::session& s, int min_, int max_, char const* interface, int flags)`
- **Description**: Configures the session to listen on a range of ports for incoming connections.
- **Parameters**:
  - `s` (lt::session&): The session object to configure
  - `min_` (int): The minimum port number to listen on
  - `max_` (int): The maximum port number to listen on
  - `interface` (char const*): The network interface to bind to (e.g., "0.0.0.0")
  - `flags` (int): Additional flags for the listen operation
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - Throws std::system_error if the operation fails
- **Example**:
```cpp
listen_on(session, 6881, 6889, "0.0.0.0", lt::session::listen_ipv4);
```
- **Preconditions**: The session must be valid and not already listening
- **Postconditions**: The session will listen on the specified port range
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: outgoing_ports

- **Signature**: `void outgoing_ports(lt::session& s, int _min, int _max)`
- **Description**: Configures the range of outgoing ports to use for outgoing connections.
- **Parameters**:
  - `s` (lt::session&): The session object to configure
  - `_min` (int): The minimum outgoing port number
  - `_max` (int): The maximum outgoing port number
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
outgoing_ports(session, 50000, 50100);
```
- **Preconditions**: The session must be valid
- **Postconditions**: The session will use outgoing ports in the specified range
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: add_dht_node

- **Signature**: `void add_dht_node(lt::session& s, tuple n)`
- **Description**: Adds a DHT node to the DHT network.
- **Parameters**:
  - `s` (lt::session&): The session object to configure
  - `n` (tuple): A tuple containing the IP address and port of the DHT node
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
add_dht_node(session, make_tuple("192.168.1.1", 6881));
```
- **Preconditions**: The session must be valid and running
- **Postconditions**: The DHT node will be added to the network
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: add_dht_router

- **Signature**: `void add_dht_router(lt::session& s, std::string router_, int port_)`
- **Description**: Adds a DHT router to the DHT network.
- **Parameters**:
  - `s` (lt::session&): The session object to configure
  - `router_` (std::string): The hostname or IP address of the DHT router
  - `port_` (int): The port number of the DHT router
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
add_dht_router(session, "router.bitcoinstats.com", 80);
```
- **Preconditions**: The session must be valid and running
- **Postconditions**: The DHT router will be added to the network
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: add_extension

- **Signature**: `void add_extension(lt::session& s, object const& e)`
- **Description**: Adds an extension to the session, currently supporting the ut_metadata extension.
- **Parameters**:
  - `s` (lt::session&): The session object to configure
  - `e` (object const&): The extension name as a string
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
add_extension(session, "ut_metadata");
```
- **Preconditions**: The session must be valid and running
- **Postconditions**: The specified extension will be added to the session
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: make_settings_pack

- **Signature**: `void make_settings_pack(lt::settings_pack& p, dict const& sett_dict)`
- **Description**: Converts a Python dictionary to a libtorrent settings_pack object.
- **Parameters**:
  - `p` (lt::settings_pack&): The settings_pack object to populate
  - `sett_dict` (dict const&): The Python dictionary containing settings
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - Raises KeyError if a setting name is unknown
- **Example**:
```cpp
dict settings;
settings["peer_fingerprint"] = "MyClient/1.0";
make_settings_pack(settings_pack, settings);
```
- **Preconditions**: The settings_pack and dictionary must be valid
- **Postconditions**: The settings_pack will be populated with values from the dictionary
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of settings

## Function: make_dict

- **Signature**: `dict make_dict(lt::settings_pack const& sett)`
- **Description**: Converts a libtorrent settings_pack object to a Python dictionary.
- **Parameters**:
  - `sett` (lt::settings_pack const&): The settings_pack object to convert
- **Return Value**: 
  - dict: A Python dictionary containing the settings
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
dict settings = make_dict(session.get_settings());
```
- **Preconditions**: The settings_pack must be valid
- **Postconditions**: Returns a dictionary with all settings from the settings_pack
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of settings

## Function: make_session

- **Signature**: `std::shared_ptr<lt::session> make_session(boost::python::dict sett, session_flags_t const flags)`
- **Description**: Creates a new libtorrent session with the specified settings and flags.
- **Parameters**:
  - `sett` (boost::python::dict): The dictionary containing session settings
  - `flags` (session_flags_t const): Session flags to configure the session
- **Return Value**: 
  - std::shared_ptr<lt::session>: A shared pointer to the created session
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
auto session = make_session(settings_dict, lt::session::add_default_plugins);
```
- **Preconditions**: The settings dictionary must be valid
- **Postconditions**: Returns a shared pointer to a new session object
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: session_apply_settings

- **Signature**: `void session_apply_settings(lt::session& ses, dict const& sett_dict)`
- **Description**: Applies settings to an existing session from a dictionary.
- **Parameters**:
  - `ses` (lt::session&): The session object to configure
  - `sett_dict` (dict const&): The Python dictionary containing settings
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
session_apply_settings(session, settings_dict);
```
- **Preconditions**: The session and dictionary must be valid
- **Postconditions**: The session will have the specified settings applied
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of settings

## Function: session_get_settings

- **Signature**: `dict session_get_settings(lt::session const& ses)`
- **Description**: Retrieves the current settings of a session as a Python dictionary.
- **Parameters**:
  - `ses` (lt::session const&): The session object to query
- **Return Value**: 
  - dict: A Python dictionary containing the session's current settings
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
dict current_settings = session_get_settings(session);
```
- **Preconditions**: The session must be valid
- **Postconditions**: Returns a dictionary with the current settings
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of settings

## Function: min_memory_usage_wrapper

- **Signature**: `dict min_memory_usage_wrapper()`
- **Description**: Returns settings optimized for minimal memory usage.
- **Parameters**: 
  - None
- **Return Value**: 
  - dict: A Python dictionary containing minimal memory usage settings
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
dict minimal_settings = min_memory_usage_wrapper();
```
- **Preconditions**: None
- **Postconditions**: Returns a dictionary with minimal memory usage settings
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: default_settings_wrapper

- **Signature**: `dict default_settings_wrapper()`
- **Description**: Returns the default settings for a libtorrent session.
- **Parameters**: 
  - None
- **Return Value**: 
  - dict: A Python dictionary containing the default settings
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
dict default_settings = default_settings_wrapper();
```
- **Preconditions**: None
- **Postconditions**: Returns a dictionary with default settings
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: high_performance_seed_wrapper

- **Signature**: `dict high_performance_seed_wrapper()`
- **Description**: Returns settings optimized for high performance in seeding mode.
- **Parameters**: 
  - None
- **Return Value**: 
  - dict: A Python dictionary containing high performance seeding settings
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
dict high_perf_settings = high_performance_seed_wrapper();
```
- **Preconditions**: None
- **Postconditions**: Returns a dictionary with high performance seeding settings
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: add_torrent_depr

- **Signature**: `torrent_handle add_torrent_depr(lt::session& s, torrent_info const& ti, std::string const& save, entry const& resume, storage_mode_t storage_mode, bool paused)`
- **Description**: Adds a torrent to the session using deprecated parameters.
- **Parameters**:
  - `s` (lt::session&): The session object
  - `ti` (torrent_info const&): The torrent info object
  - `save` (std::string const&): The save path for the torrent
  - `resume` (entry const&): Resume data for the torrent
  - `storage_mode` (storage_mode_t): The storage mode for the torrent
  - `paused` (bool): Whether the torrent should start paused
- **Return Value**: 
  - torrent_handle: A handle to the added torrent
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
torrent_handle handle = add_torrent_depr(session, ti, "/downloads", resume_data, storage_mode_t::storage_mode_sparse, false);
```
- **Preconditions**: The session must be valid
- **Postconditions**: Returns a handle to the added torrent
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: dict_to_add_torrent_params

- **Signature**: `void dict_to_add_torrent_params(dict params, add_torrent_params& p)`
- **Description**: Converts a Python dictionary to an add_torrent_params object.
- **Parameters**:
  - `params` (dict): The Python dictionary containing torrent parameters
  - `p` (add_torrent_params&): The add_torrent_params object to populate
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - None
- **Example**:
```cpp
add_torrent_params params;
dict_to_add_torrent_params(torrent_dict, params);
```
- **Preconditions**: The dictionary and parameters must be valid
- **Postconditions**: The add_torrent_params object will be populated with values from the dictionary
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of parameters

## Function: add_torrent

- **Signature**: `torrent_handle add_torrent(lt::session& s, dict params)`
- **Description**: Adds a torrent to the session using a dictionary of parameters.
- **Parameters**:
  - `s` (lt::session&): The session object
  - `params` (dict): A dictionary containing torrent parameters
- **Return Value**: 
  - torrent_handle: A handle to the added torrent
- **Exceptions/Errors**: 
  - Raises KeyError if save_path is not set
- **Example**:
```cpp
dict torrent_params;
torrent_params["save_path"] = "/downloads";
torrent_params["info_hash"] = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p";
torrent_handle handle = add_torrent(session, torrent_params);
```
- **Preconditions**: The session must be valid
- **Postconditions**: Returns a handle to the added torrent
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of parameters

## Function: async_add_torrent

- **Signature**: `void async_add_torrent(lt::session& s, dict params)`
- **Description**: Asynchronously adds a torrent to the session.
- **Parameters**:
  - `s` (lt::session&): The session object
  - `params` (dict): A dictionary containing torrent parameters
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - Raises KeyError if save_path is not set
- **Example**:
```cpp
dict torrent_params;
torrent_params["save_path"] = "/downloads";
torrent_params["info_hash"] = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p";
async_add_torrent(session, torrent_params);
```
- **Preconditions**: The session must be valid
- **Postconditions**: The torrent will be added asynchronously
- **Thread Safety**: Thread-safe
- **Complexity**: O(n) time, O(1) space where n is the number of parameters

## Function: wrap_add_torrent

- **Signature**: `torrent_handle wrap_add_torrent(lt::session& s, lt::add_torrent_params const& p)`
- **Description**: Wraps add_torrent_params to add a torrent to the session.
- **Parameters**:
  - `s` (lt::session&): The session object
  - `p` (lt::add_torrent_params const&): The torrent parameters
- **Return Value**: 
  - torrent_handle: A handle to the added torrent
- **Exceptions/Errors**: 
  - Raises KeyError if save_path is not set
- **Example**:
```cpp
add_torrent_params params;
params.save_path = "/downloads";
params.info_hash = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p";
torrent_handle handle = wrap_add_torrent(session, params);
```
- **Preconditions**: The session must be valid
- **Postconditions**: Returns a handle to the added torrent
- **Thread Safety**: Thread-safe
- **Complexity**: O(1) time, O(1) space

## Function: wrap_async_add_torrent

- **Signature**: `void wrap_async_add_torrent(lt::session& s, lt::add_torrent_params const& p)`
- **Description**: Asynchronously wraps add_torrent_params to add a torrent to the session.
- **Parameters**:
  - `s` (lt::session&): The session object
  - `p` (lt::add_torrent_params const&): The torrent parameters
- **Return Value**: 
  - void
- **Exceptions/Errors**: 
  - Raises ValueError if save_path is not set
- **Example**:
```cpp
add_torrent_params params;
params.save_path = "/downloads";
params.info_hash = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p";
wrap_async_add_torrent(session, params);
```
- **Pre