/**
 * @file error_handling.cpp
 * @brief Demonstrates error handling with Result<T, E> and Optional<T>
 *
 * This example shows:
 * - Using Result for error handling
 * - Optional for optional values
 * - Error propagation patterns
 * - Pattern matching
 *
 * Build:
 *   g++ -std=c++20 error_handling.cpp -ladvancedlib -o error_handling
 */

#include <advlib/core.hpp>
#include <iostream>
#include <cmath>

using namespace advlib;

/**
 * Safe division that returns Result instead of throwing
 */
Result<double, String> safe_divide(double a, double b) {
    if (b == 0.0) {
        return Err(String("Division by zero"));
    }
    return Ok(a / b);
}

/**
 * Safe square root that returns Result
 */
Result<double, String> safe_sqrt(double x) {
    if (x < 0.0) {
        return Err(String("Cannot take square root of negative number"));
    }
    return Ok(std::sqrt(x));
}

/**
 * Find element in array, returns Optional
 */
Optional<int> find_element(const std::vector<int>& vec, int target) {
    for (size_t i = 0; i < vec.size(); ++i) {
        if (vec[i] == target) {
            return Optional<int>(static_cast<int>(i));
        }
    }
    return Optional<int>::none();
}

/**
 * Complex calculation with error handling
 */
Result<double, String> complex_calculation(double a, double b, double c) {
    // Chain operations with and_then
    return safe_divide(a, b)
        .and_then([c](double result) {
            return safe_sqrt(result + c);
        })
        .map([](double result) {
            return result * 2.0;
        });
}

int main() {
    log::init(log::Level::Info);

    // Example 1: Basic Result usage
    log::info("=== Example 1: Basic Result ===");

    auto result1 = safe_divide(10.0, 2.0);
    if (result1.is_ok()) {
        log::info("10 / 2 = {}", result1.value());
    }

    auto result2 = safe_divide(10.0, 0.0);
    if (result2.is_err()) {
        log::error("Error: {}", result2.error());
    }

    // Example 2: Pattern matching
    log::info("\n=== Example 2: Pattern Matching ===");

    safe_divide(20.0, 4.0).match(
        [](double value) {
            log::info("Success: 20 / 4 = {}", value);
        },
        [](const String& error) {
            log::error("Failed: {}", error);
        }
    );

    // Example 3: Chaining operations
    log::info("\n=== Example 3: Chaining Operations ===");

    auto result3 = safe_divide(100.0, 4.0)
        .map([](double x) { return x * 2.0; })
        .map([](double x) { return x + 10.0; });

    log::info("Result: {}", result3.value_or(0.0));

    // Example 4: Complex calculation
    log::info("\n=== Example 4: Complex Calculation ===");

    auto calc_result = complex_calculation(16.0, 4.0, 0.0);
    calc_result.match(
        [](double value) {
            log::info("Calculation result: {}", value);
        },
        [](const String& error) {
            log::error("Calculation failed: {}", error);
        }
    );

    // Example 5: Optional usage
    log::info("\n=== Example 5: Optional Values ===");

    std::vector<int> numbers = {10, 20, 30, 40, 50};

    auto found = find_element(numbers, 30);
    if (found.has_value()) {
        log::info("Found 30 at index {}", found.value());
    } else {
        log::warn("Element not found");
    }

    auto not_found = find_element(numbers, 99);
    auto index = not_found.value_or(-1);
    log::info("Element 99 index: {} (default)", index);

    // Example 6: Optional with map
    log::info("\n=== Example 6: Optional Transformations ===");

    auto upper_bound = find_element(numbers, 40)
        .map([&numbers](int idx) {
            return numbers[idx] * 2;
        })
        .value_or(0);

    log::info("Upper bound: {}", upper_bound);

    return 0;
}
