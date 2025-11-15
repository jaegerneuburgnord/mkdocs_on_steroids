# API Documentation for `suggest_piece.hpp`

## Function: get_pieces

- **Signature**: `int get_pieces(std::vector<piece_index_t>& p, typed_bitfield<piece_index_t> const& bits, int n)`
- **Description**: This function retrieves a list of piece indices that should be prioritized for downloading based on the current piece availability and priority ordering. It populates the provided vector with piece indices, starting from the highest priority pieces (which are stored at the end of the internal priority list) and filtering by the provided bitfield. The function returns the number of pieces added to the result vector.
- **Parameters**:
  - `p` (std::vector<piece_index_t>&): The output vector that will be populated with piece indices. This vector must be pre-allocated or will be resized as needed. The function adds piece indices to the end of this vector.
  - `bits` (typed_bitfield<piece_index_t> const&): A bitfield representing which pieces are available or have been downloaded. Only pieces where the corresponding bit is set (i.e., pieces that are available) will be considered for inclusion.
  - `n` (int): The maximum number of pieces to return. The function will return at most `n` pieces, though it may return fewer if there are insufficient available pieces.
- **Return Value**:
  - `int`: The number of pieces added to the output vector `p`. This value will be between 0 and `n` (inclusive). A return value of 0 indicates that no pieces were added (either because there were no high-priority pieces available or because the `m_priority_pieces` container was empty).
- **Exceptions/Errors**:
  - **No exceptions**: This function does not throw exceptions. It operates on valid input parameters and assumes the caller has ensured that the `m_priority_pieces` container is properly initialized and contains valid data.
  - **Undefined behavior**: If the `m_priority_pieces` container is not properly initialized or contains invalid piece indices, the function may produce incorrect results or crash.
- **Example**:
```cpp
std::vector<piece_index_t> pieces;
typed_bitfield<piece_index_t> available_pieces; // Assume this is populated
int result = get_pieces(pieces, available_pieces, 5);
if (result > 0) {
    // Use the list of prioritized pieces
    for (const auto& piece : pieces) {
        std::cout << "Prioritized piece: " << piece << std::endl;
    }
} else {
    std::cout << "No pieces to suggest" << std::endl;
}
```
- **Preconditions**:
  - `m_priority_pieces` must be a valid, non-empty container containing piece indices in order of priority (highest priority at the end).
  - `bits` must be a valid bitfield that represents piece availability.
  - `n` must be a non-negative integer.
  - The `p` vector must be a valid, writable container.
- **Postconditions**:
  - The `p` vector will contain up to `n` piece indices that are both available (as indicated by `bits`) and have the highest priority.
  - The order of pieces in the output vector will be from highest to lowest priority (based on the internal `m_priority_pieces` ordering).
  - The function will return the number of pieces added to the `p` vector.
- **Thread Safety**:
  - **Not thread-safe**: This function accesses shared state (`m_priority_pieces`) that may be modified by other threads. It should only be called from a single thread or under appropriate synchronization.
- **Complexity**:
  - **Time complexity**: O(n) in the worst case, where n is the number of pieces to return. The function iterates through the priority list until it finds `n` available pieces.
  - **Space complexity**: O(1) additional space, not counting the output vector `p`.
- **See Also**: `add_piece`, `m_priority_pieces`, `typed_bitfield`

## Function: add_piece

- **Signature**: `void add_piece(piece_index_t const index, int const availability, int const max_queue_size)`
- **Description**: This function updates the internal state of the piece suggestion mechanism by adding a new piece to the availability tracking system. It records the availability of a specific piece and maintains a running average of piece availability. Pieces with availability above the current average are filtered out (not considered for prioritization). The function also respects a maximum queue size to prevent unbounded growth of the internal data structures.
- **Parameters**:
  - `index` (piece_index_t const): The piece index that is being updated. This must be a valid piece index within the range of the torrent's piece set.
  - `availability` (int const): The number of peers that have this piece. This value should be non-negative and represents the current availability of the piece.
  - `max_queue_size` (int const): The maximum size of the internal queue or buffer used to track piece availability statistics. This parameter limits the number of historical availability samples that are kept.
- **Return Value**:
  - `void`: This function does not return a value.
- **Exceptions/Errors**:
  - **No exceptions**: This function does not throw exceptions.
  - **Undefined behavior**: If the `index` is invalid or if the availability value is negative, the function may produce incorrect results or crash.
- **Example**:
```cpp
// Assume we have a piece index and availability information
piece_index_t piece = 42;
int availability = 3; // 3 peers have this piece
int max_queue_size = 100;

add_piece(piece, availability, max_queue_size);
// The internal state is now updated with this piece's availability
```
- **Preconditions**:
  - `index` must be a valid piece index.
  - `availability` must be a non-negative integer.
  - `max_queue_size` must be a positive integer.
  - The internal availability tracking system (`m_availability`) must be properly initialized.
- **Postconditions**:
  - The internal availability tracking system will have updated its state to include the new availability sample for the given piece.
  - The running average of piece availability will be recalculated.
  - The internal queue of availability samples will be truncated to `max_queue_size` elements if necessary.
- **Thread Safety**:
  - **Not thread-safe**: This function modifies shared state (`m_availability`) and should only be called from a single thread or under appropriate synchronization.
- **Complexity**:
  - **Time complexity**: O(1) average case, O(log n) worst case depending on the implementation of the `m_availability` data structure.
  - **Space complexity**: O(1) additional space, not counting the storage in the internal data structures.
- **See Also**: `get_pieces`, `m_availability`, `m_priority_pieces`

# Usage Examples

## Basic Usage

```cpp
#include "libtorrent/aux_/suggest_piece.hpp"
#include <vector>

// Initialize a piece suggestion system
std::vector<piece_index_t> pieces;
typed_bitfield<piece_index_t> available_pieces; // Populate this with available pieces
int max_pieces_to_suggest = 10;

// Get prioritized pieces
int num_suggested = get_pieces(pieces, available_pieces, max_pieces_to_suggest);
if (num_suggested > 0) {
    std::cout << "Suggested " << num_suggested << " pieces for download:" << std::endl;
    for (const auto& piece : pieces) {
        std::cout << "  Piece " << piece << std::endl;
    }
}
```

## Error Handling

```cpp
#include "libtorrent/aux_/suggest_piece.hpp"
#include <iostream>

// Example of handling the case where no pieces are available
std::vector<piece_index_t> pieces;
typed_bitfield<piece_index_t> available_pieces; // Assume this is empty

int result = get_pieces(pieces, available_pieces, 5);
if (result == 0) {
    std::cout << "No pieces to suggest - all pieces are already downloaded or unavailable" << std::endl;
} else {
    std::cout << "Suggested " << result << " pieces for download" << std::endl;
}
```

## Edge Cases

```cpp
#include "libtorrent/aux_/suggest_piece.hpp"
#include <vector>

// Edge case: max_queue_size is zero
std::vector<piece_index_t> pieces;
typed_bitfield<piece_index_t> available_pieces;
int max_queue_size = 0; // This is an edge case

// add_piece should handle this by not tracking any samples
add_piece(42, 3, max_queue_size);

// get_pieces will still work as expected
int result = get_pieces(pieces, available_pieces, 10);
if (result > 0) {
    // This should not happen since no pieces were added to the suggestion list
    std::cout << "Unexpected: " << result << " pieces suggested" << std::endl;
}
```

# Best Practices

- **Use appropriate data structures**: Always ensure that the `available_pieces` bitfield is properly initialized and reflects the current state of piece availability.
- **Avoid excessive calls**: The `add_piece` function should only be called when there is actual availability data to update. Frequent calls without meaningful changes can degrade performance.
- **Handle edge cases**: Be aware that the function returns 0 when no pieces are available, so check the return value appropriately.
- **Thread synchronization**: If these functions are used in a multi-threaded environment, implement proper synchronization to prevent race conditions.
- **Performance**: For large torrents with many pieces, consider the impact of the `m_priority_pieces` container size on performance.

# Code Review & Improvement Suggestions

## Potential Issues

### Function: get_pieces
**Issue**: The function uses a `m_priority_pieces` container without showing its definition or ensuring proper bounds checking. This could lead to undefined behavior if the container is not properly initialized or if the piece indices are out of bounds.
**Severity**: Medium
**Impact**: Could cause crashes or incorrect results
**Fix**: Add bounds checking and ensure proper initialization of the `m_priority_pieces` container.

### Function: add_piece
**Issue**: The function name and parameter names are not descriptive enough. The variable `max_queue_size` is not clearly named, and the function lacks validation for the `availability` parameter.
**Severity**: Medium
**Impact**: Could lead to confusion for users and potential runtime issues
**Fix**: Improve naming and add input validation:

```cpp
void add_piece(piece_index_t const piece_index, int const piece_availability, int const max_samples)
{
    // Validate input parameters
    if (piece_availability < 0) {
        throw std::invalid_argument("Piece availability cannot be negative");
    }
    
    // Keep a running average of the availability of pieces, and filter anything above average.
    int const mean = m_availability.mean();
    m_availability.add_sample(piece_availability);
    
    // Filter pieces with availability above average
    if (piece_availability > mean) {
        // Handle filtering logic
    }
}
```

## Modernization Opportunities

### Function: get_pieces
**Opportunity**: Add `[[nodiscard]]` attribute to indicate that the return value is important.
**Suggestion**: 
```cpp
[[nodiscard]] int get_pieces(std::vector<piece_index_t>& p, typed_bitfield<piece_index_t> const& bits, int n)
```

### Function: add_piece
**Opportunity**: Use `std::span` for the piece index if the function is intended to handle arrays.
**Suggestion**: 
```cpp
void add_piece(std::span<const piece_index_t> indices, std::span<const int> availabilities, int max_queue_size)
```

## Refactoring Suggestions

### Function: get_pieces
**Suggestion**: Split into two functions: one for getting the list of pieces and another for calculating the number of pieces to return. This would make the function more modular and easier to test.

### Function: add_piece
**Suggestion**: Move the availability filtering logic into a separate function to improve code readability and maintainability.

## Performance Optimizations

### Function: get_pieces
**Opportunity**: Use `std::vector::reserve()` to pre-allocate memory for the output vector, reducing the number of reallocations.
**Suggestion**: 
```cpp
p.reserve(n); // Pre-allocate space for at most n pieces
```

### Function: add_piece
**Opportunity**: Use move semantics for the availability data if it's being passed from another function.
**Suggestion**: 
```cpp
void add_piece(piece_index_t const index, int&& availability, int const max_queue_size)
```

# Final Notes

The `suggest_piece.hpp` functions provide essential functionality for a BitTorrent client's piece selection algorithm. The `get_pieces` function is responsible for prioritizing pieces for download based on availability and user preferences, while `add_piece` updates the internal state with new availability information. Both functions are critical for efficient and fair piece distribution in a BitTorrent swarm.