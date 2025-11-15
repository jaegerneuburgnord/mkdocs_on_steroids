# libtorrent Merkle Tree API Documentation

## merkle_tree

- **Signature**: `merkle_tree()`
- **Description**: Default constructor for the merkle_tree class. Creates an uninitialized merkle tree object. This constructor is provided for compatibility but is not recommended for use as it creates an "uninitialized" tree. The preferred approach is to use the parameterized constructor that initializes the tree with the required dimensions.
- **Parameters**: None
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
// Note: This usage is discouraged as it creates an uninitialized tree
merkle_tree tree;
```
- **Preconditions**: None
- **Postconditions**: A merkle_tree object is created in an uninitialized state
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `merkle_tree(int num_blocks, int blocks_per_piece)`

## merkle_tree

- **Signature**: `merkle_tree(int num_blocks, int blocks_per_piece)`
- **Description**: Parameterized constructor for the merkle_tree class. Initializes a merkle tree with the specified number of blocks and blocks per piece. This constructor sets up the internal structure of the merkle tree to support the required file layout and piece organization.
- **Parameters**:
  - `num_blocks` (int): The total number of blocks in the file. Must be non-negative. This determines the size of the merkle tree.
  - `blocks_per_piece` (int): The number of blocks in each piece. Must be a power of 2 and greater than 0. This determines the granularity of the merkle tree.
- **Return Value**: None (constructor)
- **Exceptions/Errors**: None
- **Example**:
```cpp
// Create a merkle tree for a file with 1024 blocks, 8 blocks per piece
merkle_tree tree(1024, 8);
```
- **Preconditions**: `num_blocks >= 0`, `blocks_per_piece > 0` and `blocks_per_piece` is a power of 2
- **Postconditions**: A merkle_tree object is created with the specified dimensions
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `merkle_tree()`, `blocks_per_piece()`

## end_index

- **Signature**: `int end_index() const`
- **Description**: Returns the end index of the merkle tree, which is equivalent to the total number of blocks in the tree. This function provides the upper bound for valid block indices in the merkle tree.
- **Parameters**: None
- **Return Value**: 
  - `int`: The number of blocks in the merkle tree (size of the tree)
- **Exceptions/Errors**: None
- **Example**:
```cpp
merkle_tree tree(1024, 8);
int end_idx = tree.end_index();
// end_idx will be 1024
```
- **Preconditions**: The merkle_tree object must be properly initialized
- **Postconditions**: The returned value is equal to the size of the merkle tree
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `size()`, `blocks_per_piece()`

## blocks_per_piece

- **Signature**: `int blocks_per_piece() const`
- **Description**: Returns the number of blocks per piece in the merkle tree. This value is stored as a logarithm (m_blocks_per_piece_log) and is returned as 2^log_value, which gives the actual number of blocks per piece.
- **Parameters**: None
- **Return Value**: 
  - `int`: The number of blocks per piece in the merkle tree
- **Exceptions/Errors**: None
- **Example**:
```cpp
merkle_tree tree(1024, 8);
int blocks_per_piece_val = tree.blocks_per_piece();
// blocks_per_piece_val will be 8
```
- **Preconditions**: The merkle_tree object must be properly initialized
- **Postconditions**: The returned value is the number of blocks per piece
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `piece_levels()`, `merkle_tree(int num_blocks, int blocks_per_piece)`

## piece_levels

- **Signature**: `int piece_levels() const`
- **Description**: Returns the number of levels in the piece hierarchy, which is equivalent to the logarithm (base 2) of the number of blocks per piece. This value represents the depth of the merkle tree for each piece.
- **Parameters**: None
- **Return Value**: 
  - `int`: The number of levels in the piece hierarchy (log2(blocks_per_piece))
- **Exceptions/Errors**: None
- **Example**:
```cpp
merkle_tree tree(1024, 8);
int levels = tree.piece_levels();
// levels will be 3 (since 2^3 = 8)
```
- **Preconditions**: The merkle_tree object must be properly initialized
- **Postconditions**: The returned value is the logarithm (base 2) of blocks_per_piece
- **Thread Safety**: Thread-safe
- **Complexity**: O(1)
- **See Also**: `blocks_per_piece()`, `merkle_tree(int num_blocks, int blocks_per_piece)`

## Usage Examples

### Basic Usage
```cpp
#include <libtorrent/aux_/merkle_tree.hpp>

int main() {
    // Create a merkle tree for a file with 1024 blocks, 8 blocks per piece
    merkle_tree tree(1024, 8);
    
    // Get the number of blocks per piece
    int blocks_per_piece = tree.blocks_per_piece();
    // blocks_per_piece will be 8
    
    // Get the number of levels in the piece hierarchy
    int piece_levels = tree.piece_levels();
    // piece_levels will be 3
    
    // Get the end index (total number of blocks)
    int end_idx = tree.end_index();
    // end_idx will be 1024
    
    return 0;
}
```

### Error Handling
```cpp
#include <libtorrent/aux_/merkle_tree.hpp>
#include <iostream>

int main() {
    // Proper usage with error checking
    try {
        // Create a valid merkle tree
        merkle_tree tree(1024, 8);
        
        // Use the tree
        int blocks_per_piece = tree.blocks_per_piece();
        std::cout << "Blocks per piece: " << blocks_per_piece << std::endl;
        
        int piece_levels = tree.piece_levels();
        std::cout << "Piece levels: " << piece_levels << std::endl;
        
        int end_idx = tree.end_index();
        std::cout << "End index: " << end_idx << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error creating merkle tree: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```

### Edge Cases
```cpp
#include <libtorrent/aux_/merkle_tree.hpp>
#include <iostream>

int main() {
    // Edge case 1: Zero blocks
    merkle_tree tree_zero(0, 1);
    std::cout << "Zero blocks end index: " << tree_zero.end_index() << std::endl;
    // Output: 0
    
    // Edge case 2: Single block per piece
    merkle_tree tree_single(1024, 1);
    std::cout << "Single block per piece blocks: " << tree_single.blocks_per_piece() << std::endl;
    // Output: 1
    std::cout << "Single block per piece levels: " << tree_single.piece_levels() << std::endl;
    // Output: 0
    
    // Edge case 3: Large number of blocks
    merkle_tree tree_large(1000000, 1024);
    std::cout << "Large tree end index: " << tree_large.end_index() << std::endl;
    // Output: 1000000
    
    return 0;
}
```

## Best Practices

1. **Use the parameterized constructor**: Always use the parameterized constructor `merkle_tree(int num_blocks, int blocks_per_piece)` instead of the default constructor to ensure the tree is properly initialized.

2. **Validate parameters**: Ensure that `num_blocks` is non-negative and `blocks_per_piece` is a positive power of 2 when creating the tree.

3. **Use const correctness**: Use `const` methods where possible to avoid unnecessary copies and to make the code more readable.

4. **Consider the tree size**: Be mindful of the memory footprint when creating large merkle trees with many blocks.

5. **Avoid uninitialized trees**: The default constructor creates an uninitialized tree, which is not recommended for production use.

6. **Use the provided functions**: Use the `blocks_per_piece()`, `piece_levels()`, and `end_index()` functions to access tree properties rather than accessing internal members directly.

## Code Review & Improvement Suggestions

### Potential Issues

**Function**: `merkle_tree()`
**Issue**: Default constructor creates an uninitialized tree, which is not recommended
**Severity**: High
**Impact**: Can lead to undefined behavior when using the tree
**Fix**: Remove the default constructor and require initialization:
```cpp
// Remove the default constructor
// merkle_tree() = default;

// Instead, only provide the parameterized constructor
merkle_tree(int num_blocks, int blocks_per_piece);
```

**Function**: `blocks_per_piece()`
**Issue**: The function returns the number of blocks per piece, but the internal representation is stored as a logarithm
**Severity**: Medium
**Impact**: Could lead to confusion about the internal representation
**Fix**: Add documentation about the logarithmic storage:
```cpp
// Add documentation
int blocks_per_piece() const { 
    // Returns the number of blocks per piece (2^m_blocks_per_piece_log)
    return 1 << m_blocks_per_piece_log; 
}
```

**Function**: `piece_levels()`
**Issue**: The function returns the logarithm of blocks_per_piece, which might be confusing
**Severity**: Medium
**Impact**: Could lead to confusion about the relationship between levels and blocks per piece
**Fix**: Add documentation about the relationship:
```cpp
// Add documentation
int piece_levels() const { 
    // Returns the number of levels in the piece hierarchy (log2(blocks_per_piece))
    return m_blocks_per_piece_log; 
}
```

### Modernization Opportunities

**Function**: All functions
**Opportunity**: Add `[[nodiscard]]` attribute to functions that return important values
**Benefit**: Prevents ignoring important return values
**Implementation**:
```cpp
// Add [[nodiscard]] to functions that return important values
[[nodiscard]] int end_index() const;
[[nodiscard]] int blocks_per_piece() const;
[[nodiscard]] int piece_levels() const;
```

**Function**: `merkle_tree()`
**Opportunity**: Use `constexpr` for compile-time evaluation of tree properties
**Benefit**: Enables compile-time checks and optimizations
**Implementation**:
```cpp
// Add constexpr where possible
constexpr int end_index() const { return int(size()); }
constexpr int blocks_per_piece() const { return 1 << m_blocks_per_piece_log; }
constexpr int piece_levels() const { return m_blocks_per_piece_log; }
```

### Refactoring Suggestions

**Function**: `merkle_tree()`
**Suggestion**: Remove the default constructor and make the parameterized constructor the only constructor
**Benefit**: Ensures all merkle trees are properly initialized
**Implementation**:
```cpp
// Remove the default constructor
// merkle_tree() = default;

// Make the parameterized constructor the only constructor
merkle_tree(int num_blocks, int blocks_per_piece);
```

**Function**: `end_index()`, `blocks_per_piece()`, `piece_levels()`
**Suggestion**: Consider combining these into a single method that returns a struct with all the information
**Benefit**: Reduces function calls and provides a more complete view of the tree's configuration
**Implementation**:
```cpp
struct TreeConfig {
    int num_blocks;
    int blocks_per_piece;
    int piece_levels;
};

[[nodiscard]] TreeConfig get_config() const;
```

### Performance Optimizations

**Function**: `merkle_tree()`
**Optimization**: Use move semantics for efficient construction
**Benefit**: Reduces unnecessary copying of tree data
**Implementation**:
```cpp
// Ensure the class supports move operations
merkle_tree(merkle_tree&& other) noexcept;
merkle_tree& operator=(merkle_tree&& other) noexcept;
```

**Function**: `end_index()`, `blocks_per_piece()`, `piece_levels()`
**Optimization**: Ensure these functions are inlined for maximum performance
**Benefit**: Eliminates function call overhead
**Implementation**:
```cpp
// Mark these functions as inline
inline int end_index() const { return int(size()); }
inline int blocks_per_piece() const { return 1 << m_blocks_per_piece_log; }
inline int piece_levels() const { return m_blocks_per_piece_log; }
```