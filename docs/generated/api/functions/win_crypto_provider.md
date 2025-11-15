# libtorrent Win Crypto Provider API Documentation

## crypt_acquire_provider

- **Signature**: `HCRYPTPROV crypt_acquire_provider(DWORD provider_type)`
- **Description**: Acquires a cryptographic service provider (CSP) context for Windows Crypto API operations. This function is used to obtain a handle to a cryptographic provider that can be used for various cryptographic operations.
- **Parameters**:
  - `provider_type` (DWORD): The type of cryptographic provider to acquire. Common values include `PROV_RSA_FULL` for RSA encryption, `PROV_RSA_SIG` for RSA signing, etc.
- **Return Value**:
  - Returns a valid `HCRYPTPROV` handle on success.
  - Throws a `system_error` exception on failure.
- **Exceptions/Errors**:
  - Throws `system_error` if `CryptAcquireContext` fails (e.g., provider not found, insufficient permissions).
  - Error codes from `GetLastError()` are captured in the exception.
- **Example**:
```cpp
try {
    HCRYPTPROV provider = crypt_acquire_provider(PROV_RSA_FULL);
    // Use the provider for cryptographic operations
} catch (const system_error& e) {
    // Handle error
    std::cerr << "Failed to acquire crypto provider: " << e.what() << std::endl;
}
```
- **Preconditions**: The Windows Cryptographic API must be available.
- **Postconditions**: Returns a valid `HCRYPTPROV` handle that can be used for cryptographic operations.
- **Thread Safety**: Not thread-safe due to global state (static variable in get_provider).
- **Complexity**: O(1) time and space complexity.
- **See Also**: `get_provider`, `crypt_gen_random`, `crypt_hash`

## crypt_gen_random

- **Signature**: `void crypt_gen_random(span<char> buffer)`
- **Description**: Generates cryptographically strong random bytes using the Windows Crypto API. This function uses a shared cryptographic provider acquired at the first call.
- **Parameters**:
  - `buffer` (span<char>): The buffer to fill with random bytes. The buffer must be non-empty and have sufficient capacity for the requested number of bytes.
- **Return Value**:
  - Returns void. The function modifies the provided buffer in-place.
- **Exceptions/Errors**:
  - Throws `system_error` if `CryptGenRandom` fails (e.g., insufficient entropy, invalid parameters).
  - Error codes from `GetLastError()` are captured in the exception.
- **Example**:
```cpp
std::vector<char> random_data(32);
try {
    crypt_gen_random(random_data);
    // Use random_data for cryptographic purposes
} catch (const system_error& e) {
    // Handle error
    std::cerr << "Failed to generate random bytes: " << e.what() << std::endl;
}
```
- **Preconditions**: The function must be called after `crypt_acquire_provider` has been called at least once (via `get_provider`).
- **Postconditions**: The buffer is filled with cryptographically random bytes.
- **Thread Safety**: Not thread-safe due to shared state in `get_provider`.
- **Complexity**: O(n) time complexity where n is the number of bytes to generate.
- **See Also**: `crypt_acquire_provider`, `get_provider`

## crypt_hash

- **Signature**: `crypt_hash()`
- **Description**: Default constructor for the `crypt_hash` class. Initializes a new hash object by creating a new cryptographic hash object.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: Throws `system_error` if `CryptCreateHash` fails.
- **Example**:
```cpp
crypt_hash hash;
// Use the hash object for hashing operations
```
- **Preconditions**: The function must be called in a context where Windows Cryptographic API is available.
- **Postconditions**: A new cryptographic hash object is created and stored in the instance.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_hash(const crypt_hash&)`, `~crypt_hash()`, `operator=(const crypt_hash&)`

## crypt_hash

- **Signature**: `crypt_hash(crypt_hash const& h)`
- **Description**: Copy constructor for the `crypt_hash` class. Creates a new hash object by duplicating an existing hash object.
- **Parameters**:
  - `h` (crypt_hash const&): The hash object to copy.
- **Return Value**: None
- **Exceptions/Errors**: Throws `system_error` if `CryptDuplicateHash` fails.
- **Example**:
```cpp
crypt_hash hash1;
// ... perform some hashing operations on hash1
crypt_hash hash2(hash1); // Copy constructor
// hash2 now has the same hash state as hash1
```
- **Preconditions**: The source hash object must be valid.
- **Postconditions**: A new hash object is created with the same state as the source object.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_hash()`, `~crypt_hash()`, `operator=(const crypt_hash&)`

## crypt_hash

- **Signature**: `~crypt_hash()`
- **Description**: Destructor for the `crypt_hash` class. Cleans up the cryptographic hash object by destroying it.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: None (functionally no exception can be thrown from a destructor).
- **Example**:
```cpp
{
    crypt_hash hash;
    // ... use hash for hashing operations
    // hash is automatically destroyed when it goes out of scope
}
```
- **Preconditions**: The object must have been constructed with a valid hash.
- **Postconditions**: The cryptographic hash object is destroyed and resources are released.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_hash()`, `crypt_hash(const crypt_hash&)`, `operator=(const crypt_hash&)`

## operator=

- **Signature**: `crypt_hash& operator=(crypt_hash const& h) &`
- **Description**: Assignment operator for the `crypt_hash` class. Assigns the state of one hash object to another, replacing the current state.
- **Parameters**:
  - `h` (crypt_hash const&): The hash object to assign from.
- **Return Value**: Returns a reference to the current object (`*this`).
- **Exceptions/Errors**: Throws `system_error` if `CryptDuplicateHash` or `CryptDestroyHash` fails.
- **Example**:
```cpp
crypt_hash hash1;
// ... perform some hashing operations on hash1
crypt_hash hash2;
hash2 = hash1; // Assignment operator
// hash2 now has the same hash state as hash1
```
- **Preconditions**: The source hash object must be valid.
- **Postconditions**: The current hash object has the same state as the source object, and the old hash state is destroyed.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_hash()`, `crypt_hash(const crypt_hash&)`, `~crypt_hash()`

## reset

- **Signature**: `void reset()`
- **Description**: Resets the hash object to its initial state, effectively creating a new hash object with the same algorithm and provider.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**: Throws `system_error` if `CryptCreateHash` or `CryptDestroyHash` fails.
- **Example**:
```cpp
crypt_hash hash;
// ... perform some hashing operations on hash
hash.reset(); // Reset the hash
// ... perform more hashing operations on hash
```
- **Preconditions**: The object must have been constructed with a valid hash.
- **Postconditions**: The hash object is reset to its initial state, ready for new hashing operations.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_hash()`, `update()`, `get_hash()`

## update

- **Signature**: `void update(span<char const> data)`
- **Description**: Updates the hash object with additional data. This function can be called multiple times to hash a stream of data.
- **Parameters**:
  - `data` (span<char const>): The data to hash. The span must be non-empty and the data must be valid.
- **Return Value**: None
- **Exceptions/Errors**: Throws `system_error` if `CryptHashData` fails (e.g., invalid hash handle, insufficient memory).
- **Example**:
```cpp
crypt_hash hash;
std::vector<char> data1 = {0x01, 0x02, 0x03};
std::vector<char> data2 = {0x04, 0x05, 0x06};
// ... perform hashing operations on hash
hash.update(data1);
hash.update(data2);
```
- **Preconditions**: The hash object must be valid and not destroyed.
- **Postconditions**: The hash object is updated with the provided data.
- **Thread Safety**: Not thread-safe due to shared state in the hash object.
- **Complexity**: O(n) time complexity where n is the number of bytes in the data.
- **See Also**: `crypt_hash()`, `reset()`, `get_hash()`

## get_hash

- **Signature**: `void get_hash(char *digest, std::size_t digest_size)`
- **Description**: Retrieves the final hash value from the hash object. The hash must be complete (no more data can be added) before calling this function.
- **Parameters**:
  - `digest` (char*): Pointer to a buffer where the hash value will be stored. The buffer must be large enough to hold the hash.
  - `digest_size` (std::size_t): The size of the digest buffer in bytes.
- **Return Value**: None
- **Exceptions/Errors**: Throws `system_error` if `CryptGetHashParam` fails (e.g., invalid hash handle, insufficient buffer size).
- **Example**:
```cpp
crypt_hash hash;
std::vector<char> data = {0x01, 0x02, 0x03};
hash.update(data);
hash.update(data); // Hash the data twice
std::vector<char> digest(32); // Assuming SHA-256, 32 bytes
hash.get_hash(digest.data(), digest.size());
// Now digest contains the hash value
```
- **Preconditions**: The hash object must be valid and not destroyed. The digest buffer must be large enough to hold the hash value.
- **Postconditions**: The digest buffer contains the final hash value.
- **Thread Safety**: Not thread-safe due to shared state in the hash object.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `update()`, `reset()`, `crypt_hash()`

## create

- **Signature**: `HCRYPTHASH create()`
- **Description**: Creates a new cryptographic hash object using the shared provider and algorithm specified by the class.
- **Parameters**: None
- **Return Value**:
  - Returns a valid `HCRYPTHASH` handle on success.
  - Throws a `system_error` exception on failure.
- **Exceptions/Errors**:
  - Throws `system_error` if `CryptCreateHash` fails (e.g., invalid provider, insufficient memory).
  - Error codes from `GetLastError()` are captured in the exception.
- **Example**:
```cpp
try {
    HCRYPTHASH hash = create();
    // Use the hash for cryptographic operations
    CryptDestroyHash(hash);
} catch (const system_error& e) {
    // Handle error
    std::cerr << "Failed to create hash: " << e.what() << std::endl;
}
```
- **Preconditions**: The function must be called in a context where Windows Cryptographic API is available.
- **Postconditions**: Returns a valid `HCRYPTHASH` handle that can be used for cryptographic operations.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `duplicate`, `get_provider`, `crypt_hash`

## duplicate

- **Signature**: `HCRYPTHASH duplicate(crypt_hash const& h)`
- **Description**: Duplicates a cryptographic hash object, creating a new hash object with the same state as the original.
- **Parameters**:
  - `h` (crypt_hash const&): The hash object to duplicate.
- **Return Value**:
  - Returns a valid `HCRYPTHASH` handle on success.
  - Throws a `system_error` exception on failure.
- **Exceptions/Errors**:
  - Throws `system_error` if `CryptDuplicateHash` fails (e.g., invalid hash handle, insufficient memory).
  - Error codes from `GetLastError()` are captured in the exception.
- **Example**:
```cpp
crypt_hash hash1;
// ... perform some hashing operations on hash1
HCRYPTHASH hash2 = duplicate(hash1);
// hash2 now has the same hash state as hash1
CryptDestroyHash(hash2);
```
- **Preconditions**: The source hash object must be valid.
- **Postconditions**: Returns a new hash object with the same state as the source object.
- **Thread Safety**: Not thread-safe due to shared provider state.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `create`, `get_provider`, `crypt_hash`

## get_provider

- **Signature**: `HCRYPTPROV get_provider()`
- **Description**: Retrieves the cryptographic provider handle used by the hash operations. The provider is acquired at the first call and cached for subsequent calls.
- **Parameters**: None
- **Return Value**:
  - Returns a valid `HCRYPTPROV` handle on success.
  - Throws a `system_error` exception if the provider cannot be acquired.
- **Exceptions/Errors**:
  - Throws `system_error` if `CryptAcquireContext` fails (e.g., provider not found, insufficient permissions).
  - Error codes from `GetLastError()` are captured in the exception.
- **Example**:
```cpp
try {
    HCRYPTPROV provider = get_provider();
    // Use the provider for cryptographic operations
} catch (const system_error& e) {
    // Handle error
    std::cerr << "Failed to get crypto provider: " << e.what() << std::endl;
}
```
- **Preconditions**: The function must be called in a context where Windows Cryptographic API is available.
- **Postconditions**: Returns a valid `HCRYPTPROV` handle that can be used for cryptographic operations.
- **Thread Safety**: Not thread-safe due to global static variable.
- **Complexity**: O(1) time and space complexity.
- **See Also**: `crypt_acquire_provider`, `create`, `duplicate`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/win_crypto_provider.hpp>
#include <vector>

// Create a hash object
crypt_hash hash;

// Update the hash with some data
std::vector<char> data = {0x01, 0x02, 0x03, 0x04};
hash.update(data);

// Get the final hash
std::vector<char> digest(32); // Assuming SHA-256
hash.get_hash(digest.data(), digest.size());

// Use the digest for whatever purpose
```

## Error Handling

```cpp
#include <libtorrent/aux_/win_crypto_provider.hpp>
#include <iostream>
#include <vector>

void hash_with_error_handling() {
    try {
        // Create a hash object
        crypt_hash hash;
        
        // Update with data
        std::vector<char> data = {0x01, 0x02, 0x03};
        hash.update(data);
        
        // Get the hash
        std::vector<char> digest(32);
        hash.get_hash(digest.data(), digest.size());
        
        // Use the digest
        std::cout << "Hash computed successfully." << std::endl;
        
    } catch (const std::system_error& e) {
        std::cerr << "Cryptographic operation failed: " << e.what() << std::endl;
        // Handle error appropriately
    } catch (const std::exception& e) {
        std::cerr << "Other error: " << e.what() << std::endl;
    }
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/win_crypto_provider.hpp>
#include <iostream>
#include <vector>

void edge_cases() {
    // Empty update
    crypt_hash hash;
    hash.update({}); // Empty span
    std::cout << "Empty update successful." << std::endl;
    
    // Large data
    std::vector<char> large_data(1000000, 0x01); // 1MB of data
    try {
        crypt_hash hash;
        hash.update(large_data);
        
        std::vector<char> digest(32);
        hash.get_hash(digest.data(), digest.size());
        
        std::cout << "Large data hashing successful." << std::endl;
    } catch (const std::system_error& e) {
        std::cerr << "Large data hashing failed: " << e.what() << std::endl;
    }
    
    // Reset and reuse
    try {
        crypt_hash hash;
        std::vector<char> data1 = {0x01, 0x02};
        std::vector<char> data2 = {0x03, 0x04};
        
        hash.update(data1);
        hash.reset();
        hash.update(data2);
        
        std::vector<char> digest(32);
        hash.get_hash(digest.data(), digest.size());
        
        std::cout << "Reset and reuse successful." << std::endl;
    } catch (const std::system_error& e) {
        std::cerr << "Reset and reuse failed: " << e.what() << std::endl;
    }
}
```

# Best Practices

1. **Always check for errors**: Use try-catch blocks around cryptographic operations to handle potential failures.
2. **Use proper error handling**: Handle `system_error` exceptions and provide meaningful error messages.
3. **Validate input**: Ensure that buffer sizes are sufficient and data spans are valid.
4. **Avoid repeated provider acquisition**: The provider is acquired at the first call to `get_provider` and cached,