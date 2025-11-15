# libtorrent Extensions API Documentation

This document provides comprehensive API documentation for the extension framework in libtorrent, covering session plugins, torrent plugins, peer plugins, and crypto plugins.

## Plugin Architecture Overview

The libtorrent extension system allows developers to extend the functionality of the library by implementing custom plugins. The architecture is built around several key interfaces:

1. **plugin**: Base class for session plugins
2. **torrent_plugin**: Base class for torrent-specific plugins
3. **peer_plugin**: Base class for peer-specific plugins
4. **crypto_plugin**: Base class for encryption plugins

These plugins can hook into various stages of the torrent lifecycle and network communication to add custom functionality.

## plugin

### Signature
`virtual ~plugin()`

### Description
Virtual destructor for the plugin base class. This ensures proper cleanup of derived plugin classes when they are destroyed.

### Parameters
- None

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
class MyPlugin : public plugin {
public:
    ~MyPlugin() override {
        // Cleanup code
    }
};
```

### Preconditions
- The plugin object must be properly constructed
- The plugin must be properly initialized before destruction

### Postconditions
- All resources owned by the plugin are released
- Any derived classes are properly destructed

### Thread Safety
- Thread-safe for destruction
- Not thread-safe for concurrent access

### Complexity
- O(1) time and space complexity

### See Also
- `torrent_plugin`
- `peer_plugin`
- `crypto_plugin`

## plugin

### Signature
`virtual feature_flags_t implemented_features() { return {}; }`

### Description
Returns the features implemented by this plugin. This method is called by the session to determine what capabilities the plugin provides. The returned flags indicate which features the plugin supports.

### Parameters
- None

### Return Value
- `feature_flags_t`: A bitset of implemented features. The default returns an empty set.

### Exceptions/Errors
- None

### Example
```cpp
feature_flags_t MyPlugin::implemented_features() {
    return feature_flags_t::has_dht_support |
           feature_flags_t::has_torrent_plugin;
}
```

### Preconditions
- The plugin must be properly initialized

### Postconditions
- The returned feature flags represent the plugin's capabilities

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `new_torrent()`

## plugin

### Signature
`virtual std::shared_ptr<torrent_plugin> new_torrent(torrent_handle const&, client_data_t) { return std::shared_ptr<torrent_plugin>(); }`

### Description
Creates a new torrent plugin instance for the specified torrent. This method is called when a new torrent is added to the session. The plugin can return a shared pointer to a torrent plugin that will be used for that specific torrent.

### Parameters
- `torrent_handle const&`: Handle to the torrent that was added
- `client_data_t`: Additional client-specific data

### Return Value
- `std::shared_ptr<torrent_plugin>`: Shared pointer to a new torrent plugin, or empty if no plugin should be created

### Exceptions/Errors
- None

### Example
```cpp
std::shared_ptr<torrent_plugin> MyPlugin::new_torrent(
    torrent_handle const& handle, client_data_t data) {
    
    auto plugin = std::make_shared<MyTorrentPlugin>();
    return plugin;
}
```

### Preconditions
- The plugin must be properly initialized
- The torrent handle must be valid

### Postconditions
- Returns a shared pointer to a torrent plugin, or an empty shared pointer

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `torrent_plugin`

## plugin

### Signature
`virtual void added(session_handle const&) {}`

### Description
Called when the plugin is added to the session. This method is invoked after the plugin is registered with the session. It can be used to perform initialization tasks.

### Parameters
- `session_handle const&`: Handle to the session that the plugin was added to

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::added(session_handle const& session) {
    // Initialize plugin with session
    m_session = session;
}
```

### Preconditions
- The plugin must be properly constructed
- The session handle must be valid

### Postconditions
- The plugin is ready to participate in session operations

### Thread Safety
- Thread-safe for initialization

### Complexity
- O(1) time complexity

### See Also
- `abort()`

## plugin

### Signature
`virtual void abort() {}`

### Description
Called when the plugin is being removed from the session. This method is invoked when the session is shutting down or the plugin is being destroyed. It provides an opportunity to clean up resources and perform final operations.

### Parameters
- None

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::abort() {
    // Clean up resources
    m_session = session_handle{};
}
```

### Preconditions
- The plugin must be properly initialized
- The plugin must be in a state where it can be safely destroyed

### Postconditions
- Resources are cleaned up
- The plugin can be safely destroyed

### Thread Safety
- Thread-safe for shutdown

### Complexity
- O(1) time complexity

### See Also
- `added()`

## plugin

### Signature
`virtual bool on_dht_request(string_view /* query */, udp::endpoint const& /* source */, bdecode_node const& /* message */, entry& /* response */) { return false; }`

### Description
Handles DHT (Distributed Hash Table) requests. This method is called when the session receives a DHT request. The plugin can process the request and modify the response.

### Parameters
- `string_view query`: The DHT query string
- `udp::endpoint const& source`: The source of the DHT request
- `bdecode_node const& message`: The DHT message content
- `entry& response`: Reference to the response entry to be modified

### Return Value
- `bool`: Returns `true` if the plugin handled the request, `false` otherwise

### Exceptions/Errors
- None

### Example
```cpp
bool MyPlugin::on_dht_request(string_view query,
    udp::endpoint const& source, bdecode_node const& message, entry& response) {
    
    if (query == "get_peers") {
        // Process get_peers request
        response["values"] = {"192.168.1.100:6881"};
        return true;
    }
    return false;
}
```

### Preconditions
- The plugin must be properly initialized
- The DHT request must be valid

### Postconditions
- The response is modified if the plugin handles the request
- Returns `true` if the request was handled

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `on_unknown_torrent()`

## plugin

### Signature
`virtual void on_alert(alert const*) {}`

### Description
Handles alerts from the session. This method is called when the session generates an alert. The plugin can process the alert and take appropriate action.

### Parameters
- `alert const*`: Pointer to the alert to be processed

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::on_alert(alert const* a) {
    if (alert_cast<status_changed_alert>(a)) {
        // Handle status change
    }
}
```

### Preconditions
- The plugin must be properly initialized
- The alert pointer must be valid

### Postconditions
- The plugin has processed the alert

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `on_unknown_torrent()`

## plugin

### Signature
`virtual bool on_unknown_torrent(info_hash_t const& /* info_hash */, peer_connection_handle const& /* pc */, add_torrent_params& /* p */) { return false; }`

### Description
Handles unknown torrents. This method is called when a new torrent is detected but not yet added to the session. The plugin can decide whether to add the torrent and modify the add_torrent_params.

### Parameters
- `info_hash_t const& info_hash`: The info hash of the unknown torrent
- `peer_connection_handle const& pc`: Handle to the peer connection that triggered this event
- `add_torrent_params& p`: Reference to the parameters that will be used to add the torrent

### Return Value
- `bool`: Returns `true` if the plugin wants to add the torrent, `false` otherwise

### Exceptions/Errors
- None

### Example
```cpp
bool MyPlugin::on_unknown_torrent(info_hash_t const& info_hash,
    peer_connection_handle const& pc, add_torrent_params& p) {
    
    if (shouldAddTorrent(info_hash)) {
        p.flags |= add_torrent_params::flag_auto_managed;
        return true;
    }
    return false;
}
```

### Preconditions
- The plugin must be properly initialized
- The info hash must be valid
- The peer connection handle must be valid

### Postconditions
- The add_torrent_params may be modified
- Returns `true` if the plugin wants to add the torrent

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `on_dht_request()`

## plugin

### Signature
`virtual void on_tick() {}`

### Description
Called periodically by the session. This method is called at regular intervals (typically every few seconds) to allow the plugin to perform periodic tasks.

### Parameters
- None

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::on_tick() {
    // Periodic cleanup or monitoring
    m_stats.update();
}
```

### Preconditions
- The plugin must be properly initialized
- The session must be running

### Postconditions
- The plugin has performed its periodic tasks

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `save_state()`

## plugin

### Signature
`virtual uint64_t get_unchoke_priority(peer_connection_handle const& /* peer */) { return (std::numeric_limits<uint64_t>::max)(); }`

### Description
Returns the unchoke priority for a peer connection. This method is called when the session decides which peers to unchoke. Higher priority peers are more likely to be unchoked.

### Parameters
- `peer_connection_handle const& peer`: Handle to the peer connection

### Return Value
- `uint64_t`: The unchoke priority, with higher values indicating higher priority. The default returns `std::numeric_limits<uint64_t>::max()` which means the peer has the lowest priority.

### Exceptions/Errors
- None

### Example
```cpp
uint64_t MyPlugin::get_unchoke_priority(peer_connection_handle const& peer) {
    // Return a priority based on peer's download speed
    return peer.get_download_rate() * 1000;
}
```

### Preconditions
- The plugin must be properly initialized
- The peer connection handle must be valid

### Postconditions
- Returns a priority value for the peer

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `on_tick()`

## plugin

### Signature
`virtual void save_state(entry&) {}`

### Description
Saves the plugin's state to the specified entry. This method is called when the session needs to save its state (e.g., during shutdown or configuration change). The plugin can store its persistent data in the entry.

### Parameters
- `entry&`: Reference to the entry where the state should be saved

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::save_state(entry& e) {
    // Save plugin-specific state
    e["my_plugin_version"] = 1;
    e["last_updated"] = time(nullptr);
}
```

### Preconditions
- The plugin must be properly initialized
- The entry must be valid

### Postconditions
- The plugin's state is saved in the entry

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `load_state()`

## plugin

### Signature
`virtual void load_state(bdecode_node const&) {}`

### Description
Loads the plugin's state from the specified bdecode_node. This method is called when the session needs to restore its state (e.g., after startup). The plugin can restore its persistent data from the node.

### Parameters
- `bdecode_node const&`: Reference to the bdecode_node containing the state data

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::load_state(bdecode_node const& node) {
    // Load plugin-specific state
    if (node.is_dict()) {
        if (auto v = node.dict_find_int("my_plugin_version")) {
            m_version = v;
        }
    }
}
```

### Preconditions
- The plugin must be properly initialized
- The bdecode_node must be valid

### Postconditions
- The plugin's state is restored from the node

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `save_state()`

## plugin

### Signature
`virtual std::map<std::string, std::string> save_state() const { return {}; }`

### Description
Saves the plugin's state to a map of strings. This method is called when the session needs to save its state (e.g., during shutdown or configuration change). The plugin can store its persistent data in the map.

### Parameters
- None

### Return Value
- `std::map<std::string, std::string>`: A map containing the plugin's state data. The default returns an empty map.

### Exceptions/Errors
- None

### Example
```cpp
std::map<std::string, std::string> MyPlugin::save_state() const {
    std::map<std::string, std::string> state;
    state["version"] = std::to_string(m_version);
    state["last_updated"] = std::to_string(m_last_updated);
    return state;
}
```

### Preconditions
- The plugin must be properly initialized

### Postconditions
- Returns a map containing the plugin's state data

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `load_state()`

## plugin

### Signature
`virtual void load_state(std::map<std::string, std::string> const&) {}`

### Description
Loads the plugin's state from a map of strings. This method is called when the session needs to restore its state (e.g., after startup). The plugin can restore its persistent data from the map.

### Parameters
- `std::map<std::string, std::string> const&`: Reference to the map containing the state data

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyPlugin::load_state(std::map<std::string, std::string> const& state) {
    // Load plugin-specific state
    for (auto const& [key, value] : state) {
        if (key == "version") {
            m_version = std::stoi(value);
        } else if (key == "last_updated") {
            m_last_updated = std::stoi(value);
        }
    }
}
```

### Preconditions
- The plugin must be properly initialized
- The map must be valid

### Postconditions
- The plugin's state is restored from the map

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `save_state()`

## torrent_plugin

### Signature
`virtual ~torrent_plugin() {}`

### Description
Virtual destructor for the torrent_plugin base class. This ensures proper cleanup of derived torrent plugin classes when they are destroyed.

### Parameters
- None

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
class MyTorrentPlugin : public torrent_plugin {
public:
    ~MyTorrentPlugin() override {
        // Cleanup code
    }
};
```

### Preconditions
- The plugin object must be properly constructed
- The plugin must be properly initialized before destruction

### Postconditions
- All resources owned by the plugin are released
- Any derived classes are properly destructed

### Thread Safety
- Thread-safe for destruction
- Not thread-safe for concurrent access

### Complexity
- O(1) time and space complexity

### See Also
- `peer_plugin`
- `crypto_plugin`

## torrent_plugin

### Signature
`virtual std::shared_ptr<peer_plugin> new_connection(peer_connection_handle const&) { return std::shared_ptr<peer_plugin>(); }`

### Description
Creates a new peer plugin instance for the specified peer connection. This method is called when a new peer connection is established with the torrent. The plugin can return a shared pointer to a peer plugin that will be used for that specific peer.

### Parameters
- `peer_connection_handle const&`: Handle to the peer connection

### Return Value
- `std::shared_ptr<peer_plugin>`: Shared pointer to a new peer plugin, or empty if no plugin should be created

### Exceptions/Errors
- None

### Example
```cpp
std::shared_ptr<peer_plugin> MyTorrentPlugin::new_connection(
    peer_connection_handle const& pc) {
    
    auto plugin = std::make_shared<MyPeerPlugin>();
    return plugin;
}
```

### Preconditions
- The plugin must be properly initialized
- The peer connection handle must be valid

### Postconditions
- Returns a shared pointer to a peer plugin, or an empty shared pointer

### Thread Safety
- Thread-safe

### Complexity
- O(1) time complexity

### See Also
- `peer_plugin`

## torrent_plugin

### Signature
`virtual void on_piece_pass(piece_index_t) {}`

### Description
Called when a piece is successfully downloaded and verified. This method is invoked when a piece passes all checks and is ready to be used.

### Parameters
- `piece_index_t piece`: The index of the piece that passed verification

### Return Value
- None

### Exceptions/Errors
- None

### Example
```cpp
void MyTorrentPlugin::on_piece_pass(piece_index_t piece) {
    // Log successful piece download
    std::cout <<