# libtorrent CNG API Documentation

## throw_ntstatus_error

- **Signature**: `void throw_ntstatus_error(char const* name, NTSTATUS status)`
- **Description**: Throws a std::system_error exception with the given NTSTATUS error code and a descriptive message. This function is a helper to convert NTSTATUS errors from Windows CNG (Cryptography Next Generation) functions into C++ exceptions.
- **Parameters**:
  - `name` (char const*): The name of the function that failed, used in the error message. This should be a null-terminated string.
  - `status` (NTSTATUS): The NTSTATUS error code returned by a Windows CNG function.
- **Return Value**: None. This function does not return normally as it throws an exception.
- **Exceptions/Errors**: Throws `std::system_error` with the NTSTATUS code and the provided name. The error category is system_category().
- **Example**:
```cpp
try {
    // Some CNG operation that might fail
    if (some_cng_function() < 0) {
        throw_ntstatus_error("some_cng_function", status);
    }
} catch (const std::system_error& e) {
    std::cerr << "CNG error: " << e.what() << std::endl;
}
```
- **Preconditions**: The function name should be valid and not null.
- **Postconditions**: None. The function throws an exception and does not return.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `cng_open_algorithm_handle`, `cng_gen_random`

## cng_open_algorithm_handle

- **Signature**: `BCRYPT_ALG_HANDLE cng_open_algorithm_handle(LPCWSTR alg_name)`
- **Description**: Opens a handle to a cryptographic algorithm provider using the Windows CNG (Cryptography Next Generation) API. This function is used to obtain a handle for subsequent cryptographic operations.
- **Parameters**:
  - `alg_name` (LPCWSTR): A pointer to a wide character string specifying the name of the algorithm to open. Common values include `BCRYPT_RNG_ALGORITHM` for random number generation.
- **Return Value**: Returns a `BCRYPT_ALG_HANDLE` on success. On failure, throws `std::system_error` with the NTSTATUS error code.
- **Exceptions/Errors**: Throws `std::system_error` if `BCryptOpenAlgorithmProvider` fails (i.e., returns a negative NTSTATUS code).
- **Example**:
```cpp
try {
    BCRYPT_ALG_HANDLE handle = cng_open_algorithm_handle(BCRYPT_RNG_ALGORITHM);
    // Use the handle for cryptographic operations
} catch (const std::system_error& e) {
    std::cerr << "Failed to open algorithm: " << e.what() << std::endl;
}
```
- **Preconditions**: The `alg_name` parameter must be a valid pointer to a wide character string.
- **Postconditions**: Returns a valid `BCRYPT_ALG_HANDLE` that can be used for cryptographic operations, or throws an exception.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `cng_get_algorithm_object_size`, `cng_gen_random`

## cng_get_algorithm_object_size

- **Signature**: `DWORD cng_get_algorithm_object_size(BCRYPT_ALG_HANDLE algorithm_handle)`
- **Description**: Retrieves the size of the algorithm object (typically a hash or key object) for a given algorithm handle. This information is needed to allocate sufficient memory for the cryptographic object.
- **Parameters**:
  - `algorithm_handle` (BCRYPT_ALG_HANDLE): The handle to the algorithm obtained from `cng_open_algorithm_handle`.
- **Return Value**: Returns the size of the algorithm object in bytes. On failure, throws `std::system_error`.
- **Exceptions/Errors**: Throws `std::system_error` if `BCryptGetProperty` fails to retrieve the `BCRYPT_OBJECT_LENGTH` property.
- **Example**:
```cpp
BCRYPT_ALG_HANDLE alg_handle = cng_open_algorithm_handle(BCRYPT_RNG_ALGORITHM);
DWORD object_size = cng_get_algorithm_object_size(alg_handle);
// Use object_size to allocate memory for cryptographic operations
```
- **Preconditions**: The `algorithm_handle` must be a valid handle obtained from `cng_open_algorithm_handle`.
- **Postconditions**: Returns the size of the algorithm object in bytes, which can be used to allocate memory for cryptographic operations.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `cng_open_algorithm_handle`, `cng_gen_random`

## cng_gen_random

- **Signature**: `void cng_gen_random(span<char> buffer)`
- **Description**: Generates cryptographically secure random bytes using the Windows CNG (Cryptography Next Generation) API. This function uses a previously opened algorithm handle for random number generation.
- **Parameters**:
  - `buffer` (span<char>): A span of characters where the random bytes will be stored. The span must have sufficient size to hold the requested number of bytes.
- **Return Value**: None. On failure, throws `std::system_error`.
- **Exceptions/Errors**: Throws `std::system_error` if `BCryptGenRandom` fails (i.e., returns a negative NTSTATUS code).
- **Example**:
```cpp
std::vector<char> random_data(32);
cng_gen_random(random_data);
// random_data now contains 32 cryptographically secure random bytes
```
- **Preconditions**: The `buffer` must be a valid span with sufficient size to hold the requested random data.
- **Postconditions**: The buffer is filled with cryptographically secure random bytes.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) where n is the number of bytes requested.
- **See Also**: `throw_ntstatus_error`, `cng_open_algorithm_handle`

## cng_hash

- **Signature**: `cng_hash()`
- **Description**: Default constructor that initializes a hash object by calling the `create()` method. This constructor is used to create a new hash object from scratch.
- **Parameters**: None.
- **Return Value**: None. The constructor does not return a value.
- **Exceptions/Errors**: Can throw `std::system_error` if `create()` fails.
- **Example**:
```cpp
cng_hash hasher;
// hasher is now initialized and ready for use
```
- **Preconditions**: None.
- **Postconditions**: The hash object is initialized and ready for use.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `create`, `destroy`

## cng_hash

- **Signature**: `cng_hash(cng_hash const& h)`
- **Description**: Copy constructor that creates a new hash object by duplicating an existing hash object. This constructor is used to create a copy of a hash object.
- **Parameters**:
  - `h` (cng_hash const&): The hash object to copy.
- **Return Value**: None. The constructor does not return a value.
- **Exceptions/Errors**: Can throw `std::system_error` if `duplicate()` fails.
- **Example**:
```cpp
cng_hash original;
cng_hash copy(original);
// copy is now a duplicate of original
```
- **Preconditions**: The `h` parameter must be a valid hash object.
- **Postconditions**: The new hash object is a copy of the original hash object.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `duplicate`, `destroy`

## cng_hash

- **Signature**: `~cng_hash()`
- **Description**: Destructor that cleans up the hash object by calling the `destroy()` method. This function is called when a hash object goes out of scope.
- **Parameters**: None.
- **Return Value**: None. The destructor does not return a value.
- **Exceptions/Errors**: Can throw `std::system_error` if `destroy()` fails.
- **Example**:
```cpp
{
    cng_hash hasher;
    // Use hasher
} // hasher is automatically destroyed here
```
- **Preconditions**: The hash object must be valid.
- **Postconditions**: The hash object is destroyed and its resources are freed.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `destroy`, `create`

## operator=

- **Signature**: `cng_hash& operator=(cng_hash const& h)`
- **Description**: Assignment operator that assigns the state of one hash object to another. This operator handles self-assignment and assignment between different hash objects.
- **Parameters**:
  - `h` (cng_hash const&): The hash object to assign from.
- **Return Value**: Returns a reference to the current object (`*this`).
- **Exceptions/Errors**: Can throw `std::system_error` if `destroy()` or `duplicate()` fails.
- **Example**:
```cpp
cng_hash hasher1;
cng_hash hasher2;
hasher2 = hasher1;
// hasher2 now has the same state as hasher1
```
- **Preconditions**: The `h` parameter must be a valid hash object.
- **Postconditions**: The current hash object has the same state as the source hash object.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `destroy`, `duplicate`

## reset

- **Signature**: `void reset()`
- **Description**: Resets the hash object to its initial state by calling `destroy()` followed by `create()`. This function is used to reinitialize a hash object for reuse.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `destroy()` or `create()` fails.
- **Example**:
```cpp
cng_hash hasher;
// Use hasher for some operations
hasher.reset();
// hasher is now reset and ready for new operations
```
- **Preconditions**: The hash object must be valid.
- **Postconditions**: The hash object is in a fresh state and ready for new operations.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `destroy`, `create`

## update

- **Signature**: `void update(span<char const> data)`
- **Description**: Updates the hash state with additional data. This function processes the input data and incorporates it into the ongoing hash computation.
- **Parameters**:
  - `data` (span<char const>): A span of constant characters containing the data to be hashed.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `BCryptHashData` fails.
- **Example**:
```cpp
cng_hash hasher;
std::vector<char> data = {0x1, 0x2, 0x3};
hasher.update(data);
// Hasher now includes the data in its hash computation
```
- **Preconditions**: The `data` parameter must be a valid span with sufficient size to hold the data.
- **Postconditions**: The hash state is updated to include the input data.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(n) where n is the size of the data.
- **See Also**: `get_hash`, `create`

## get_hash

- **Signature**: `void get_hash(char *digest, std::size_t digest_size)`
- **Description**: Finalizes the hash computation and returns the hash value. This function calls `BCryptFinishHash` to complete the hash computation and store the result in the provided buffer.
- **Parameters**:
  - `digest` (char *): Pointer to a buffer where the hash value will be stored.
  - `digest_size` (std::size_t): Size of the digest buffer in bytes.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `BCryptFinishHash` fails.
- **Example**:
```cpp
cng_hash hasher;
std::vector<char> data = {0x1, 0x2, 0x3};
hasher.update(data);
std::vector<char> hash(32); // Assuming SHA-256
hasher.get_hash(hash.data(), hash.size());
// hash now contains the computed hash value
```
- **Preconditions**: The `digest` buffer must be valid and have sufficient size to hold the hash output. The `digest_size` must be at least as large as the expected hash output size.
- **Postconditions**: The hash value is stored in the provided buffer, and the hash object is in a finalized state.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `update`, `create`

## create

- **Signature**: `void create()`
- **Description**: Creates a hash object for the current algorithm. This function calls `BCryptCreateHash` to create a new hash object that will be used for hashing operations.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `BCryptCreateHash` fails.
- **Example**:
```cpp
cng_hash hasher;
hasher.create();
// hasher is now initialized and ready for use
```
- **Preconditions**: The hash object must be in a state that allows creation (typically after reset or construction).
- **Postconditions**: The hash object is created and ready for use.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `destroy`, `reset`

## destroy

- **Signature**: `void destroy()`
- **Description**: Destroys the hash object and releases its resources. This function calls `BCryptDestroyHash` to free the hash object and its associated resources.
- **Parameters**: None.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `BCryptDestroyHash` fails.
- **Example**:
```cpp
cng_hash hasher;
// Use hasher
hasher.destroy();
// hasher's resources are now released
```
- **Preconditions**: The hash object must be valid and created.
- **Postconditions**: The hash object is destroyed and its resources are freed.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `create`, `reset`

## duplicate

- **Signature**: `void duplicate(cng_hash const& h)`
- **Description**: Duplicates an existing hash object. This function creates a new hash object that is a copy of the source hash object.
- **Parameters**:
  - `h` (cng_hash const&): The hash object to duplicate.
- **Return Value**: None.
- **Exceptions/Errors**: Can throw `std::system_error` if `BCryptDuplicateHash` fails.
- **Example**:
```cpp
cng_hash original;
cng_hash copy;
copy.duplicate(original);
// copy is now a duplicate of original
```
- **Preconditions**: The `h` parameter must be a valid hash object.
- **Postconditions**: The current hash object is a duplicate of the source hash object.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1).
- **See Also**: `create`, `destroy`

## get_algorithm_handle

- **Signature**: `BCRYPT_ALG_HANDLE get_algorithm_handle()`
- **Description**: Gets the algorithm handle for the current algorithm. This function returns a static handle that is cached and reused across all instances of the hash object.
- **Parameters**: None.
- **Return Value**: Returns a `BCRYPT_ALG_HANDLE` that can be used for cryptographic operations.
- **Exceptions/Errors**: None. This function does not throw exceptions.
- **Example**:
```cpp
cng_hash hasher;
BCRYPT_ALG_HANDLE alg_handle = hasher.get_algorithm_handle();
// Use alg_handle for cryptographic operations
```
- **Preconditions**: None.
- **Postconditions**: Returns a valid algorithm handle.
- **Thread Safety**: Thread-safe due to the use of static caching.
- **Complexity**: O(1).
- **See Also**: `cng_open_algorithm_handle`, `cng_get_algorithm_object_size`

## get_algorithm_object_size

- **Signature**: `std::size_t get_algorithm_object_size()`
- **Description**: Gets the size of the algorithm object for the current algorithm. This function returns a cached size value that was determined during initialization.
- **Parameters**: None.
- **Return Value**: Returns the size of the algorithm object in bytes.
- **Exceptions/Errors**: None. This function does not throw exceptions.
- **Example**:
```cpp
cng_hash hasher;
std::size_t object_size = hasher.get_algorithm_object_size();
// Use object_size to allocate memory for cryptographic operations
```
- **Preconditions**: None.
- **Postconditions**: Returns the size of the algorithm object in bytes.
- **Thread Safety**: Thread-safe due to the use of static caching.
- **Complexity**: O(1).
- **See Also**: `cng_get_algorithm_object_size`, `get_algorithm_handle`

# Usage Examples

## Basic Usage

```cpp
#include <libtorrent/aux_/win_cng.hpp>
#include <vector>

int main() {
    // Create a hash object
    cng_hash hasher;
    
    // Update with some data
    std::vector<char> data = {0x1, 0x2, 0x3, 0x4};
    hasher.update(data);
    
    // Get the final hash
    std::vector<char> hash(32); // Assuming SHA-256
    hasher.get_hash(hash.data(), hash.size());
    
    return 0;
}
```

## Error Handling

```cpp
#include <libtorrent/aux_/win_cng.hpp>
#include <iostream>
#include <vector>

int main() {
    try {
        cng_hash hasher;
        
        // Try to update with invalid data
        std::vector<char> invalid_data;
        hasher.update(invalid_data);
        
        // Get hash
        std::vector<char> hash(32);
        hasher.get_hash(hash.data(), hash.size());
        
        std::cout << "Hash computed successfully" << std::endl;
    } catch (const std::system_error& e) {
        std::cerr << "CNG error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Other error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```

## Edge Cases

```cpp
#include <libtorrent/aux_/win