# C++ API Documentation

## get_buffer

- **Signature**: `bytes get_buffer(read_piece_alert const& rpa)`
- **Description**: Retrieves the buffer data from a read_piece_alert. Returns a bytes object containing the data from the alert's buffer if it exists, otherwise returns an empty bytes object.
- **Parameters**:
  - `rpa` (read_piece_alert const&): The alert from which to extract the buffer data. This must be a valid read_piece_alert object.
- **Return Value**:
  - `bytes`: A bytes object containing the buffer data. If the alert has no buffer (buffer is null), an empty bytes object is returned.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of get_buffer
auto buffer = get_buffer(alert);
if (buffer.size() > 0) {
    // Process the buffer data
}
```
- **Preconditions**: The `rpa` parameter must be a valid read_piece_alert object.
- **Postconditions**: The returned bytes object contains the buffer data or is empty if no buffer exists.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `read_piece_alert`, `bytes`

## stats_alert_transferred

- **Signature**: `list stats_alert_transferred(stats_alert const& alert)`
- **Description**: Extracts the transferred data from a stats_alert and returns it as a list.
- **Parameters**:
  - `alert` (stats_alert const&): The stats_alert object containing the transferred data.
- **Return Value**:
  - `list`: A list containing the transferred data from each channel.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of stats_alert_transferred
auto transferred = stats_alert_transferred(alert);
for (auto item : transferred) {
    // Process each transferred value
}
```
- **Preconditions**: The `alert` parameter must be a valid stats_alert object.
- **Postconditions**: The returned list contains all transferred data from the alert.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of channels.
- **See Also**: `stats_alert`, `list`

## get_status_from_update_alert

- **Signature**: `list get_status_from_update_alert(state_update_alert const& alert)`
- **Description**: Retrieves the torrent status updates from a state_update_alert and returns them as a list.
- **Parameters**:
  - `alert` (state_update_alert const&): The state_update_alert object containing the status updates.
- **Return Value**:
  - `list`: A list of torrent_status objects representing the current status of torrents.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of get_status_from_update_alert
auto statuses = get_status_from_update_alert(alert);
for (auto status : statuses) {
    // Process each torrent status
}
```
- **Preconditions**: The `alert` parameter must be a valid state_update_alert object.
- **Postconditions**: The returned list contains all torrent status updates.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of torrents.
- **See Also**: `state_update_alert`, `list`, `torrent_status`

## dht_stats_active_requests

- **Signature**: `list dht_stats_active_requests(dht_stats_alert const& a)`
- **Description**: Extracts active DHT requests from a dht_stats_alert and returns them as a list of dictionaries.
- **Parameters**:
  - `a` (dht_stats_alert const&): The dht_stats_alert object containing DHT statistics.
- **Return Value**:
  - `list`: A list of dictionaries, each containing information about an active DHT request.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_stats_active_requests
auto active_requests = dht_stats_active_requests(alert);
for (auto request : active_requests) {
    // Process each active DHT request
}
```
- **Preconditions**: The `a` parameter must be a valid dht_stats_alert object.
- **Postconditions**: The returned list contains all active DHT requests.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of active requests.
- **See Also**: `dht_stats_alert`, `list`, `dht_lookup`

## dht_stats_routing_table

- **Signature**: `list dht_stats_routing_table(dht_stats_alert const& a)`
- **Description**: Extracts DHT routing table information from a dht_stats_alert and returns it as a list of dictionaries.
- **Parameters**:
  - `a` (dht_stats_alert const&): The dht_stats_alert object containing DHT statistics.
- **Return Value**:
  - `list`: A list of dictionaries, each containing routing table information.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_stats_routing_table
auto routing_table = dht_stats_routing_table(alert);
for (auto entry : routing_table) {
    // Process each routing table entry
}
```
- **Preconditions**: The `a` parameter must be a valid dht_stats_alert object.
- **Postconditions**: The returned list contains all routing table entries.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of routing table entries.
- **See Also**: `dht_stats_alert`, `list`, `dht_routing_bucket`

## dht_immutable_item

- **Signature**: `dict dht_immutable_item(dht_immutable_item_alert const& alert)`
- **Description**: Extracts immutable DHT item data from a dht_immutable_item_alert and returns it as a dictionary.
- **Parameters**:
  - `alert` (dht_immutable_item_alert const&): The dht_immutable_item_alert object containing the item data.
- **Return Value**:
  - `dict`: A dictionary containing the key and value of the immutable item.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_immutable_item
auto item = dht_immutable_item(alert);
auto key = item["key"];
auto value = item["value"];
// Process the key and value
```
- **Preconditions**: The `alert` parameter must be a valid dht_immutable_item_alert object.
- **Postconditions**: The returned dictionary contains the key and value of the immutable item.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `dht_immutable_item_alert`, `dict`

## dht_mutable_item

- **Signature**: `dict dht_mutable_item(dht_mutable_item_alert const& alert)`
- **Description**: Extracts mutable DHT item data from a dht_mutable_item_alert and returns it as a dictionary.
- **Parameters**:
  - `alert` (dht_mutable_item_alert const&): The dht_mutable_item_alert object containing the item data.
- **Return Value**:
  - `dict`: A dictionary containing the key, value, signature, sequence number, and salt of the mutable item.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_mutable_item
auto item = dht_mutable_item(alert);
auto key = item["key"];
auto value = item["value"];
auto signature = item["signature"];
auto seq = item["seq"];
auto salt = item["salt"];
// Process the key, value, signature, sequence number, and salt
```
- **Preconditions**: The `alert` parameter must be a valid dht_mutable_item_alert object.
- **Postconditions**: The returned dictionary contains all fields of the mutable item.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `dht_mutable_item_alert`, `dict`

## dht_put_item

- **Signature**: `dict dht_put_item(dht_put_alert const& alert)`
- **Description**: Extracts DHT put item data from a dht_put_alert and returns it as a dictionary.
- **Parameters**:
  - `alert` (dht_put_alert const&): The dht_put_alert object containing the put item data.
- **Return Value**:
  - `dict`: A dictionary containing the public key, signature, and sequence number if the target is not all zeros.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_put_item
auto put_item = dht_put_item(alert);
auto publicKey = put_item["public_key"];
auto signature = put_item["signature"];
auto seq = put_item["seq"];
// Process the public key, signature, and sequence number
```
- **Preconditions**: The `alert` parameter must be a valid dht_put_alert object.
- **Postconditions**: The returned dictionary contains the relevant fields of the put item.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `dht_put_alert`, `dict`

## session_stats_values

- **Signature**: `dict session_stats_values(session_stats_alert const& alert)`
- **Description**: Extracts session statistics values from a session_stats_alert and returns them as a dictionary.
- **Parameters**:
  - `alert` (session_stats_alert const&): The session_stats_alert object containing the statistics.
- **Return Value**:
  - `dict`: A dictionary containing the session statistics values.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of session_stats_values
auto stats = session_stats_values(alert);
for (auto& [key, value] : stats) {
    // Process each statistic
}
```
- **Preconditions**: The `alert` parameter must be a valid session_stats_alert object.
- **Postconditions**: The returned dictionary contains all session statistics values.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of statistics metrics.
- **See Also**: `session_stats_alert`, `dict`

## dht_live_nodes_nodes

- **Signature**: `list dht_live_nodes_nodes(dht_live_nodes_alert const& alert)`
- **Description**: Extracts live DHT nodes from a dht_live_nodes_alert and returns them as a list of dictionaries.
- **Parameters**:
  - `alert` (dht_live_nodes_alert const&): The dht_live_nodes_alert object containing the nodes.
- **Return Value**:
  - `list`: A list of dictionaries, each containing information about a live DHT node.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_live_nodes_nodes
auto nodes = dht_live_nodes_nodes(alert);
for (auto node : nodes) {
    auto nid = node["nid"];
    auto endpoint = node["endpoint"];
    // Process each live DHT node
}
```
- **Preconditions**: The `alert` parameter must be a valid dht_live_nodes_alert object.
- **Postconditions**: The returned list contains all live DHT nodes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of live nodes.
- **See Also**: `dht_live_nodes_alert`, `list`, `dict`

## dht_sample_infohashes_nodes

- **Signature**: `list dht_sample_infohashes_nodes(dht_sample_infohashes_alert const& alert)`
- **Description**: Extracts sample infohashes nodes from a dht_sample_infohashes_alert and returns them as a list of dictionaries.
- **Parameters**:
  - `alert` (dht_sample_infohashes_alert const&): The dht_sample_infohashes_alert object containing the nodes.
- **Return Value**:
  - `list`: A list of dictionaries, each containing information about a sample infohashes node.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of dht_sample_infohashes_nodes
auto nodes = dht_sample_infohashes_nodes(alert);
for (auto node : nodes) {
    auto nid = node["nid"];
    auto endpoint = node["endpoint"];
    // Process each sample infohashes node
}
```
- **Preconditions**: The `alert` parameter must be a valid dht_sample_infohashes_alert object.
- **Postconditions**: The returned list contains all sample infohashes nodes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of sample infohashes nodes.
- **See Also**: `dht_sample_infohashes_alert`, `list`, `dict`

## get_resume_data_entry

- **Signature**: `entry const& get_resume_data_entry(save_resume_data_alert const& self)`
- **Description**: Retrieves the resume data entry from a save_resume_data_alert. This function is deprecated and should not be used.
- **Parameters**:
  - `self` (save_resume_data_alert const&): The save_resume_data_alert object containing the resume data.
- **Return Value**:
  - `entry const&`: A reference to the resume data entry.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of get_resume_data_entry (deprecated)
auto resumeData = get_resume_data_entry(alert);
// Note: This function is deprecated and should not be used
```
- **Preconditions**: The `self` parameter must be a valid save_resume_data_alert object.
- **Postconditions**: The returned reference points to the resume data entry.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `save_resume_data_alert`, `entry`

## get_pkt_buf

- **Signature**: `bytes get_pkt_buf(dht_pkt_alert const& alert)`
- **Description**: Extracts the packet buffer from a dht_pkt_alert and returns it as a bytes object.
- **Parameters**:
  - `alert` (dht_pkt_alert const&): The dht_pkt_alert object containing the packet buffer.
- **Return Value**:
  - `bytes`: A bytes object containing the packet buffer data.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of get_pkt_buf
auto pktBuf = get_pkt_buf(alert);
// Process the packet buffer data
```
- **Preconditions**: The `alert` parameter must be a valid dht_pkt_alert object.
- **Postconditions**: The returned bytes object contains the packet buffer data.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `dht_pkt_alert`, `bytes`

## get_dropped_alerts

- **Signature**: `list get_dropped_alerts(alerts_dropped_alert const& alert)`
- **Description**: Extracts information about dropped alerts from an alerts_dropped_alert and returns it as a list of boolean values.
- **Parameters**:
  - `alert` (alerts_dropped_alert const&): The alerts_dropped_alert object containing information about dropped alerts.
- **Return Value**:
  - `list`: A list of boolean values indicating whether each alert was dropped.
- **Exceptions/Errors**:
  - No exceptions are thrown.
- **Example**:
```cpp
// Example usage of get_dropped_alerts
auto droppedAlerts = get_dropped_alerts(alert);
for (auto dropped : droppedAlerts) {
    if (dropped) {
        // Handle dropped alert
    }
}
```
- **Preconditions**: The `alert` parameter must be a valid alerts_dropped_alert object.
- **Postconditions**: The returned list contains the drop status for each alert.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) time complexity where n is the number of dropped alerts.
- **See Also**: `alerts_dropped_alert`, `list`

# Usage Examples

## Basic Usage

```cpp
// Example: Extracting and processing various alert data
#include <iostream>
#include <vector>

// Assume we have various alert objects
// auto alert = ...; // Initialize alert object

// Extracting buffer data
auto buffer = get_buffer(read_piece_alert);
std::cout << "Buffer size: " << buffer.size() << std::endl;

// Extracting transferred data
auto transferred = stats_alert_transferred(stats_alert);
for (auto value : transferred) {
    std::cout << "Transferred: " << value << std::endl;
}

// Extracting torrent status
auto statuses = get_status_from_update_alert(state_update_alert);
for (auto status : statuses) {
    std::cout << "Torrent status: " << status << std::endl;
}
```

## Error Handling

```cpp
// Example: Safe usage with error handling
#include <iostream>
#include <stdexcept>

// Function to safely extract data from alerts
template<typename Alert>
std::optional<typename Alert::result_type> extractData(const Alert& alert) {
    try {
        return Alert::func(alert);
    } catch (const std::exception& e) {
        std::cerr << "Error extracting data: " << e.what() << std::endl;
        return std::nullopt;
    }
}

// Example usage
auto buffer = extractData<get_buffer>(read_piece_alert);
if (buffer) {
    std::cout << "Buffer size: " << buffer->size() << std::endl;
} else {
    std::cout << "Failed to extract buffer data" << std::endl;
}
```

## Edge Cases

```cpp
// Example: Handling edge cases
#include <iostream>

// Example with null buffer
auto buffer = get_buffer(read_piece_alert);
if (buffer.size() == 0) {
    std::cout << "No buffer data available" << std::endl;
} else {
    std::cout << "Buffer size: " << buffer.size() << std::endl;
}

// Example with empty stats
auto transferred = stats_alert_transferred(stats_alert);
if (transferred.empty()) {
    std::cout << "No transferred data available" << std::endl;
} else {
    for (auto value : transferred) {
        std::cout << "Transferred: " << value << std::endl;
    }
}
