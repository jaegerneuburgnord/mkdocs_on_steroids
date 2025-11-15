# libtorrent::aux::torrent_list API Documentation

## empty

- **Signature**: `bool empty() const`
- **Description**: Checks if the torrent list is empty.
- **Parameters**: None
- **Return Value**: 
  - `true` if the list contains no torrents
  - `false` if the list contains one or more torrents
- **Exceptions/Errors**: None
- **Example**:
```cpp
if (torrent_list.empty()) {
    std::cout << "No torrents in the list" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `size()`, `clear()`

## begin (non-const)

- **Signature**: `iterator begin()`
- **Description**: Returns an iterator pointing to the first torrent in the list.
- **Parameters**: None
- **Return Value**: Iterator to the first torrent in the list
- **Exceptions/Errors**: None
- **Example**:
```cpp
auto it = torrent_list.begin();
while (it != torrent_list.end()) {
    // Process *it
    ++it;
}
```
- **Preconditions**: None
- **Postconditions**: The iterator points to the first element
- **Thread Safety**: Not thread-safe (modifies internal state)
- **Complexity**: O(1)
- **See Also**: `end()`, `cbegin()`, `cend()`

## end (non-const)

- **Signature**: `iterator end()`
- **Description**: Returns an iterator pointing to the position past the last torrent in the list.
- **Parameters**: None
- **Return Value**: Iterator to the position past the last element
- **Exceptions/Errors**: None
- **Example**:
```cpp
for (auto it = torrent_list.begin(); it != torrent_list.end(); ++it) {
    // Process *it
}
```
- **Preconditions**: None
- **Postconditions**: The iterator points to the position past the last element
- **Thread Safety**: Not thread-safe (modifies internal state)
- **Complexity**: O(1)
- **See Also**: `begin()`, `cbegin()`, `cend()`

## begin (const)

- **Signature**: `const_iterator begin() const`
- **Description**: Returns a const iterator pointing to the first torrent in the list.
- **Parameters**: None
- **Return Value**: Const iterator to the first torrent in the list
- **Exceptions/Errors**: None
- **Example**:
```cpp
for (auto it = torrent_list.begin(); it != torrent_list.end(); ++it) {
    // Read-only access to *it
}
```
- **Preconditions**: None
- **Postconditions**: The iterator points to the first element
- **Thread Safety**: Thread-safe (reads only)
- **Complexity**: O(1)
- **See Also**: `end()`, `cbegin()`, `cend()`

## end (const)

- **Signature**: `const_iterator end() const`
- **Description**: Returns a const iterator pointing to the position past the last torrent in the list.
- **Parameters**: None
- **Return Value**: Const iterator to the position past the last element
- **Exceptions/Errors**: None
- **Example**:
```cpp
for (auto it = torrent_list.cbegin(); it != torrent_list.cend(); ++it) {
    // Read-only access to *it
}
```
- **Preconditions**: None
- **Postconditions**: The iterator points to the position past the last element
- **Thread Safety**: Thread-safe (reads only)
- **Complexity**: O(1)
- **See Also**: `begin()`, `cbegin()`, `cend()`

## size

- **Signature**: `std::size_t size() const`
- **Description**: Returns the number of torrents currently in the list.
- **Parameters**: None
- **Return Value**: Number of torrents in the list
- **Exceptions/Errors**: None
- **Example**:
```cpp
std::size_t count = torrent_list.size();
std::cout << "Number of torrents: " << count << std::endl;
```
- **Preconditions**: None
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `empty()`, `clear()`

## operator[] (non-const)

- **Signature**: `T* operator[](std::size_t const idx)`
- **Description**: Accesses the torrent at the specified index with bounds checking.
- **Parameters**:
  - `idx` (std::size_t): Index of the torrent to access
    - Valid values: 0 to size()-1
    - Must be within bounds, otherwise assertion fails
- **Return Value**: 
  - Pointer to the torrent at the specified index
  - `nullptr` if the index is out of bounds (but this should never happen due to assertion)
- **Exceptions/Errors**: 
  - Assertion failure if index is out of bounds
  - Undefined behavior if the assertion is disabled
- **Example**:
```cpp
T* torrent = torrent_list[0];  // Get first torrent
if (torrent) {
    // Process torrent
}
```
- **Preconditions**: 
  - Index must be within valid range (0 to size()-1)
  - `idx < m_array.size()` must be true
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Not thread-safe (reads and modifies internal state)
- **Complexity**: O(1)
- **See Also**: `operator[] (const)`, `find()`

## operator[] (const)

- **Signature**: `T const* operator[](std::size_t const idx) const`
- **Description**: Accesses the torrent at the specified index with bounds checking (const version).
- **Parameters**:
  - `idx` (std::size_t): Index of the torrent to access
    - Valid values: 0 to size()-1
    - Must be within bounds, otherwise assertion fails
- **Return Value**: 
  - Pointer to the torrent at the specified index
  - `nullptr` if the index is out of bounds (but this should never happen due to assertion)
- **Exceptions/Errors**: 
  - Assertion failure if index is out of bounds
  - Undefined behavior if the assertion is disabled
- **Example**:
```cpp
T const* torrent = torrent_list[0];  // Get first torrent
if (torrent) {
    // Read-only access to torrent
}
```
- **Preconditions**: 
  - Index must be within valid range (0 to size()-1)
  - `idx < m_array.size()` must be true
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `operator[] (non-const)`, `find()`

## insert

- **Signature**: `bool insert(info_hash_t const& ih, std::shared_ptr<T> t)`
- **Description**: Inserts a new torrent into the list with the specified info hash.
- **Parameters**:
  - `ih` (info_hash_t const&): Info hash of the torrent to insert
  - `t` (std::shared_ptr<T>): Shared pointer to the torrent object to insert
    - Must not be null
- **Return Value**: 
  - `true` if the torrent was successfully inserted
  - `false` if a torrent with the same info hash already exists
- **Exceptions/Errors**: 
  - Assertion failure if `t` is null
  - Assertion failure if invariant check fails
- **Example**:
```cpp
info_hash_t ih = create_info_hash();
std::shared_ptr<Torrent> torrent = std::make_shared<Torrent>(ih);
bool inserted = torrent_list.insert(ih, torrent);
if (inserted) {
    std::cout << "Torrent inserted successfully" << std::endl;
} else {
    std::cout << "Duplicate torrent" << std::endl;
}
```
- **Preconditions**: 
  - `t` must not be null
  - The info hash must be valid
- **Postconditions**: 
  - If successful: The torrent is added to the list
  - If unsuccessful: The list remains unchanged
- **Thread Safety**: Not thread-safe
- **Complexity**: O(n) where n is the number of hashes in the info hash
- **See Also**: `erase()`, `find()`, `find_obfuscated()`

## find_obfuscated

- **Signature**: `T* find_obfuscated(sha1_hash const& ih)`
- **Description**: Finds a torrent with the specified obfuscated SHA-1 hash.
- **Parameters**:
  - `ih` (sha1_hash const&): The obfuscated SHA-1 hash to search for
- **Return Value**: 
  - Pointer to the found torrent if found
  - `nullptr` if no torrent with the specified hash exists
- **Exceptions/Errors**: None
- **Example**:
```cpp
sha1_hash hash = generate_obfuscated_hash();
T* torrent = torrent_list.find_obfuscated(hash);
if (torrent) {
    // Process found torrent
} else {
    std::cout << "Torrent not found" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(log n) where n is the number of torrents
- **See Also**: `find()`, `insert()`, `erase()`

## find

- **Signature**: `T* find(sha1_hash const& ih) const`
- **Description**: Finds a torrent with the specified SHA-1 hash.
- **Parameters**:
  - `ih` (sha1_hash const&): The SHA-1 hash to search for
- **Return Value**: 
  - Pointer to the found torrent if found
  - `nullptr` if no torrent with the specified hash exists
- **Exceptions/Errors**: None
- **Example**:
```cpp
sha1_hash hash = generate_sha1_hash();
T* torrent = torrent_list.find(hash);
if (torrent) {
    // Process found torrent
} else {
    std::cout << "Torrent not found" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: The list state remains unchanged
- **Thread Safety**: Thread-safe
- **Complexity**: O(log n) where n is the number of torrents
- **See Also**: `find_obfuscated()`, `insert()`, `erase()`

## erase

- **Signature**: `bool erase(info_hash_t const& ih)`
- **Description**: Removes a torrent with the specified info hash from the list.
- **Parameters**:
  - `ih` (info_hash_t const&): Info hash of the torrent to remove
- **Return Value**: 
  - `true` if the torrent was successfully removed
  - `false` if no torrent with the specified info hash exists
- **Exceptions/Errors**: 
  - Assertion failure if invariant check fails
- **Example**:
```cpp
info_hash_t ih = create_info_hash();
bool erased = torrent_list.erase(ih);
if (erased) {
    std::cout << "Torrent removed successfully" << std::endl;
} else {
    std::cout << "Torrent not found" << std::endl;
}
```
- **Preconditions**: None
- **Postconditions**: 
  - If successful: The torrent is removed from the list
  - If unsuccessful: The list remains unchanged
- **Thread Safety**: Not thread-safe
- **Complexity**: O(n) where n is the number of hashes in the info hash
- **See Also**: `insert()`, `find()`, `clear()`

## clear

- **Signature**: `void clear()`
- **Description**: Removes all torrents from the list.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: 
  - Assertion failure if invariant check fails
- **Example**:
```cpp
torrent_list.clear();
std::cout << "All torrents removed" << std::endl;
```
- **Preconditions**: None
- **Postconditions**: The list is empty
- **Thread Safety**: Not thread-safe
- **Complexity**: O(n) where n is the number of torrents
- **See Also**: `empty()`, `size()`, `insert()`

## check_invariant

- **Signature**: `void check_invariant() const`
- **Description**: Checks the internal consistency of the torrent list. This function is only enabled when expensive invariant checks are enabled.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: 
  - Assertion failure if the invariant check fails
- **Example**:
```cpp
// This is typically called internally by the implementation
// but can be called manually for debugging purposes
torrent_list.check_invariant();
```
- **Preconditions**: None
- **Postconditions**: None (unless assertion fails)
- **Thread Safety**: Thread-safe
- **Complexity**: O(n log n) where n is the number of torrents
- **See Also**: `empty()`, `size()`, `insert()`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/aux_/torrent_list.hpp"
#include "libtorrent/aux_/torrent.hpp"
#include "libtorrent/info_hash.hpp"
#include <iostream>

int main() {
    // Create a torrent list
    libtorrent::aux::torrent_list<libtorrent::aux::torrent> torrent_list;
    
    // Insert some torrents
    info_hash_t ih1, ih2;
    ih1.assign("hash1");
    ih2.assign("hash2");
    
    auto torrent1 = std::make_shared<libtorrent::aux::torrent>(ih1);
    auto torrent2 = std::make_shared<libtorrent::aux::torrent>(ih2);
    
    torrent_list.insert(ih1, torrent1);
    torrent_list.insert(ih2, torrent2);
    
    // Iterate through the list
    for (auto it = torrent_list.begin(); it != torrent_list.end(); ++it) {
        std::cout << "Found torrent" << std::endl;
    }
    
    // Check if a torrent exists
    sha1_hash hash1 = ih1.get_hashes()[0];
    T* found_torrent = torrent_list.find(hash1);
    if (found_torrent) {
        std::cout << "Found torrent with hash: " << hash1.to_string() << std::endl;
    }
    
    // Remove a torrent
    torrent_list.erase(ih1);
    
    // Check if the list is empty
    if (torrent_list.empty()) {
        std::cout << "List is empty" << std::endl;
    }
    
    return 0;
}
```

## Error Handling

```cpp
#include "libtorrent/aux_/torrent_list.hpp"
#include "libtorrent/aux_/torrent.hpp"
#include "libtorrent/info_hash.hpp"
#include <iostream>
#include <memory>

int main() {
    libtorrent::aux::torrent_list<libtorrent::aux::torrent> torrent_list;
    
    // Try to insert a null pointer (this will assert)
    info_hash_t ih;
    ih.assign("hash1");
    
    // This will cause an assertion failure in debug builds
    // auto result = torrent_list.insert(ih, std::shared_ptr<libtorrent::aux::torrent>());
    
    // Safer approach: check for null pointers
    auto torrent = std::make_shared<libtorrent::aux::torrent>(ih);
    if (torrent) {
        bool inserted = torrent_list.insert(ih, torrent);
        if (!inserted) {
            std::cout << "Failed to insert torrent: duplicate" << std::endl;
        }
    } else {
        std::cout << "Failed to create torrent object" << std::endl;
    }
    
    // Try to find a non-existent torrent
    sha1_hash non_existent_hash;
    non_existent_hash.assign("nonexistent");
    
    T* found = torrent_list.find(non_existent_hash);
    if (!found) {
        std::cout << "Torrent not found" << std::endl;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include "libtorrent/aux_/torrent_list.hpp"
#include "libtorrent/aux_/torrent.hpp"
#include "libtorrent/info_hash.hpp"
#include <iostream>
#include <vector>

int main() {
    libtorrent::aux::torrent_list<libtorrent::aux::torrent> torrent_list;
    
    // Test with empty list
    if (torrent_list.empty()) {
        std::cout << "List is initially empty" << std::endl;
    }
    
    // Test with one element
    info_hash_t ih;
    ih.assign("hash1");
    auto torrent = std::make_shared<libtorrent::aux::torrent>(ih);
    torrent_list.insert(ih, torrent);
    
    if (!torrent_list.empty()) {
        std::cout << "List is not empty after insertion" << std::endl;
    }
    
    // Test with multiple elements
    for (int i = 0; i < 10; ++i) {
        info_hash_t new_ih;
        new_ih.assign("hash" + std::to_string(i));
        auto new_torrent = std::make_shared<libtorrent::aux::torrent>(new_ih);
        torrent_list.insert(new_ih, new_torrent);
    }
    
    // Test index access with valid and invalid indices
    if (torrent_list.size() > 0) {
        T* first_torrent = torrent_list[0];
        if (first_torrent) {
            std::cout << "Successfully accessed first torrent" << std::endl;
        }
    }
    
    // Test clear
    torrent_list.clear();
    if (torrent_list.empty()) {
        std::cout << "List is empty after clear" << std::endl;
    }
    
    return 0;
}
```

# Best Practices

## Effective Usage

1. **Use const methods when possible**: Use `find()` instead of `find_obfuscated()` when you don't need obfuscated hash lookup
2. **Check return values**: Always check the return value of `insert()` to handle duplicates
3. **Use range-based for loops**: When possible, use range-based for loops for iteration
4. **Prefer find over operator[]**: Use `find()` for lookup operations as it's more explicit and doesn't require assertions

## Common Mistakes to Avoid