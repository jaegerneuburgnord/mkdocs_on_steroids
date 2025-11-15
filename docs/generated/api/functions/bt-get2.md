# API Documentation

## state

- **Signature**: `char const* state(lt::torrent_status::state_t s)`
- **Description**: Converts a libtorrent torrent status enum value to a human-readable string representation. This function maps internal torrent state values to descriptive strings for logging, debugging, or user interface display purposes.
- **Parameters**:
  - `s` (lt::torrent_status::state_t): The torrent status enum value to convert. Valid values include all states defined in lt::torrent_status::state_t enumeration such as checking_files, downloading_metadata, downloading, seeding, etc.
- **Return Value**:
  - Returns a null-terminated C string representing the state name.
  - The returned string is a static string literal and remains valid for the duration of the program.
  - The function returns a string corresponding to the state, such as "checking", "dl", etc.
  - The function does not return nullptr under normal conditions, but may return an undefined string if given an invalid enum value.
- **Exceptions/Errors**:
  - No exceptions are thrown.
  - The function assumes the input is a valid lt::torrent_status::state_t value.
  - If an invalid state is passed (which should not happen in proper usage), the behavior is undefined.
- **Example**:
```cpp
auto status = lt::torrent_status::downloading_metadata;
const char* state_str = state(status);
std::cout << "Current state: " << state_str << std::endl;
```
- **Preconditions**: The input parameter `s` must be a valid lt::torrent_status::state_t enum value.
- **Postconditions**: The function returns a valid string pointer that can be safely used for display purposes.
- **Thread Safety**: The function is thread-safe as it only reads from a switch statement and returns a static string.
- **Complexity**: O(1) time complexity, O(1) space complexity.
- **See Also**: `lt::torrent_status`, `lt::torrent_status::state_t`

## main

- **Signature**: `int main(int argc, char const* argv[])`
- **Description**: The main entry point of the bt-get2 application. This function initializes the libtorrent library, processes command-line arguments, sets up the torrent session with appropriate settings, and manages the download process from a magnet link.
- **Parameters**:
  - `argc` (int): The number of command-line arguments passed to the program.
  - `argv` (char const*): An array of C-style strings containing the command-line arguments.
- **Return Value**:
  - Returns 0 on successful completion.
  - Returns 1 if the usage is incorrect (incorrect number of arguments).
  - Returns other values if initialization or download failures occur.
- **Exceptions/Errors**:
  - Throws exceptions from the libtorrent library if initialization fails.
  - The function uses a try-catch block to handle exceptions from the libtorrent library.
  - The function returns 1 if the user provides incorrect command-line arguments.
- **Example**:
```cpp
int main(int argc, char const* argv[]) try {
    if (argc != 2) {
        std::cerr << "usage: " << argv[0] << " <magnet-url>" << std::endl;
        return 1;
    }
    
    lt::settings_pack pack;
    pack.set_int(lt::settings_pack::alert_mask
        , lt::alert_category::error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::performance_warning
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::alert_category::peer_error
        | lt::alert_category::cache
        | lt::alert_category::file_progress
        | lt::alert_category::performance_warning
        | lt::alert_category::file_error
        | lt::alert_category::storage
        | lt::alert_category::progress
        | lt::alert_category::status
        | lt::alert_category::tracker_warning
        | lt::alert_category::tracker_error
        | lt::alert_category::peer
        | lt::alert_category::dht
        | lt::alert_category::scrape
        | lt::alert_category::fastresume
        | lt::alert_category::port_mapping
        | lt::alert_category::file_error
        | lt::alert_category::listen
        | lt::alert_category::udp_error
        | lt::alert_category::ip_block
        | lt::