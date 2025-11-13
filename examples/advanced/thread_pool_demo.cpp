/**
 * @file thread_pool_demo.cpp
 * @brief Advanced thread pool demonstration
 *
 * This example demonstrates:
 * - Creating and using thread pools
 * - Submitting tasks with return values
 * - Parallel processing of data
 * - Performance comparison with sequential processing
 * - Task prioritization
 *
 * Build:
 *   g++ -std=c++20 -O3 thread_pool_demo.cpp -ladvancedlib -pthread -o thread_pool_demo
 */

#include <advlib/concurrency/thread_pool.hpp>
#include <advlib/core.hpp>
#include <iostream>
#include <vector>
#include <numeric>
#include <chrono>
#include <cmath>

using namespace advlib;
using namespace std::chrono;

/**
 * Simulates expensive computation
 */
double expensive_computation(int n) {
    double result = 0.0;
    for (int i = 1; i <= n; ++i) {
        result += std::sqrt(i) * std::sin(i) * std::cos(i);
    }
    return result;
}

/**
 * Demonstrates basic thread pool usage
 */
void demo_basic_thread_pool() {
    log::info("=== Demo 1: Basic Thread Pool ===");

    // Create thread pool with 4 worker threads
    ThreadPool pool(4);

    // Submit simple tasks
    auto future1 = pool.submit([]() {
        log::info("Task 1 executing on thread {}", std::this_thread::get_id());
        return 42;
    });

    auto future2 = pool.submit([](int x, int y) {
        log::info("Task 2 executing on thread {}", std::this_thread::get_id());
        return x + y;
    }, 10, 20);

    // Wait for results
    int result1 = future1.get();
    int result2 = future2.get();

    log::info("Task 1 result: {}", result1);
    log::info("Task 2 result: {}", result2);
}

/**
 * Parallel data processing
 */
void demo_parallel_processing() {
    log::info("\n=== Demo 2: Parallel Processing ===");

    const int NUM_TASKS = 100;
    const int WORK_SIZE = 10000;

    ThreadPool pool(std::thread::hardware_concurrency());

    // Prepare data
    std::vector<int> inputs(NUM_TASKS);
    std::iota(inputs.begin(), inputs.end(), 1);

    // Sequential processing
    auto seq_start = high_resolution_clock::now();

    std::vector<double> seq_results;
    for (int input : inputs) {
        seq_results.push_back(expensive_computation(WORK_SIZE));
    }

    auto seq_end = high_resolution_clock::now();
    auto seq_duration = duration_cast<milliseconds>(seq_end - seq_start);

    log::info("Sequential processing: {} ms", seq_duration.count());

    // Parallel processing
    auto par_start = high_resolution_clock::now();

    std::vector<Future<double>> futures;
    for (int input : inputs) {
        futures.push_back(pool.submit([input]() {
            return expensive_computation(WORK_SIZE);
        }));
    }

    std::vector<double> par_results;
    for (auto& future : futures) {
        par_results.push_back(future.get());
    }

    auto par_end = high_resolution_clock::now();
    auto par_duration = duration_cast<milliseconds>(par_end - par_start);

    log::info("Parallel processing: {} ms", par_duration.count());
    log::info("Speedup: {:.2f}x",
              static_cast<double>(seq_duration.count()) / par_duration.count());
}

/**
 * Batch processing with map operation
 */
void demo_batch_processing() {
    log::info("\n=== Demo 3: Batch Processing ===");

    ThreadPool pool(8);

    std::vector<int> data(1000);
    std::iota(data.begin(), data.end(), 1);

    // Parallel map operation
    auto start = high_resolution_clock::now();

    auto results = pool.parallel_map(data, [](int x) {
        return x * x;  // Square each element
    });

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);

    log::info("Processed {} elements in {} µs", data.size(), duration.count());
    log::info("First 10 results: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]",
              results[0], results[1], results[2], results[3], results[4],
              results[5], results[6], results[7], results[8], results[9]);
}

/**
 * Task cancellation
 */
void demo_task_cancellation() {
    log::info("\n=== Demo 4: Task Cancellation ===");

    ThreadPool pool(4);

    // Submit long-running task
    auto cancelable = pool.submit_cancelable([]() {
        for (int i = 0; i < 1000; ++i) {
            if (should_cancel()) {
                log::info("Task cancelled at iteration {}", i);
                return -1;
            }

            std::this_thread::sleep_for(milliseconds(10));
        }
        return 1000;
    });

    // Let it run for a bit
    std::this_thread::sleep_for(milliseconds(150));

    // Cancel the task
    cancelable.cancel();
    log::info("Cancellation requested");

    // Wait for result
    int result = cancelable.get();
    log::info("Task result: {}", result);
}

/**
 * Exception handling in thread pool
 */
void demo_exception_handling() {
    log::info("\n=== Demo 5: Exception Handling ===");

    ThreadPool pool(4);

    // Submit task that throws
    auto future = pool.submit([]() -> int {
        log::info("Task throwing exception...");
        throw std::runtime_error("Task failed!");
        return 42;
    });

    // Try to get result
    try {
        int result = future.get();
        log::info("Result: {}", result);
    } catch (const std::exception& e) {
        log::error("Caught exception: {}", e.what());
    }
}

/**
 * Priority-based task scheduling
 */
void demo_priority_scheduling() {
    log::info("\n=== Demo 6: Priority Scheduling ===");

    PriorityThreadPool pool(4);

    // Submit tasks with different priorities
    pool.submit_priority(Priority::Low, []() {
        log::info("Low priority task");
    });

    pool.submit_priority(Priority::High, []() {
        log::info("High priority task (should run first)");
    });

    pool.submit_priority(Priority::Medium, []() {
        log::info("Medium priority task");
    });

    pool.submit_priority(Priority::Critical, []() {
        log::info("Critical priority task (should run first)");
    });

    // Wait for all tasks
    std::this_thread::sleep_for(milliseconds(100));
    pool.wait_all();
}

int main() {
    log::init(log::Level::Info);

    log::info("Thread Pool Demonstration");
    log::info("Hardware Concurrency: {} threads\n",
              std::thread::hardware_concurrency());

    try {
        demo_basic_thread_pool();
        demo_parallel_processing();
        demo_batch_processing();
        demo_task_cancellation();
        demo_exception_handling();
        demo_priority_scheduling();

        log::info("\n=== All demos completed successfully ===");

    } catch (const std::exception& e) {
        log::error("Fatal error: {}", e.what());
        return 1;
    }

    return 0;
}
