/**
 * @file hello_world.cpp
 * @brief Simple Hello World example using AdvLib
 *
 * This example demonstrates:
 * - Basic project setup
 * - Using the String class
 * - Simple logging
 * - Version information
 *
 * Build:
 *   g++ -std=c++20 hello_world.cpp -ladvancedlib -o hello_world
 *
 * Run:
 *   ./hello_world
 */

#include <advlib/core.hpp>
#include <iostream>

using namespace advlib;

int main() {
    // Initialize logging system
    log::init(log::Level::Info);

    // Log a simple message
    log::info("Hello, AdvLib!");

    // Use String class
    String message = "Welcome to C++ Advanced Library";
    std::cout << message << std::endl;

    // Display version information
    std::cout << "AdvLib Version: "
              << ADVLIB_VERSION_MAJOR << "."
              << ADVLIB_VERSION_MINOR << "."
              << ADVLIB_VERSION_PATCH << std::endl;

    // String operations
    String name = "World";
    String greeting = String("Hello, ") + name + "!";
    log::info(greeting.c_str());

    return 0;
}
