# Advanced Concurrency

Meistere Multithreading, Async/Await und parallele Algorithmen mit AdvLib.

## Lernziele

- [x] Thread Pools effizient nutzen
- [x] Async/Await Pattern in C++
- [x] Lock-Free Data Structures
- [x] Parallele Algorithmen
- [x] Memory Ordering verstehen

**Geschätzte Zeit:** 2 Stunden
**Level:** Advanced

## Thread Pools

### Basis Thread Pool

```cpp
#include <advlib/concurrency/thread_pool.hpp>

using namespace advlib;

int main() {
    // Erstelle Thread Pool mit 4 Threads
    ThreadPool pool(4);

    // Submit einfache Tasks
    auto future1 = pool.submit([]() {
        return compute_something();
    });

    auto future2 = pool.submit([](int x, int y) {
        return x + y;
    }, 10, 20);

    // Warte auf Ergebnisse
    auto result1 = future1.get();
    auto result2 = future2.get();

    log::info("Results: {}, {}", result1, result2);

    return 0;
}
```

### Advanced Thread Pool Features

```cpp
class AdvancedThreadPoolExample {
public:
    void demonstrate() {
        // Thread Pool mit Priority
        PriorityThreadPool pool(8);

        // High Priority Task
        pool.submit_priority(Priority::High, []() {
            critical_operation();
        });

        // Low Priority Task
        pool.submit_priority(Priority::Low, []() {
            background_cleanup();
        });

        // Batch Processing
        std::vector<int> data(10000);
        auto results = pool.parallel_map(data, [](int x) {
            return expensive_computation(x);
        });

        // Task Cancellation
        auto cancelable = pool.submit_cancelable([]() {
            for (int i = 0; i < 1000000; ++i) {
                if (should_cancel()) {
                    return;
                }
                process_item(i);
            }
        });

        // Cancel nach 100ms
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        cancelable.cancel();

        // Wait for all tasks
        pool.wait_all();
    }

private:
    void critical_operation() { /* ... */ }
    void background_cleanup() { /* ... */ }
    int expensive_computation(int x) { return x * x; }
    void process_item(int i) { /* ... */ }
    bool should_cancel() { return false; }
};
```

### Work-Stealing Thread Pool

```cpp
// Effizienterer Thread Pool mit Work Stealing
WorkStealingThreadPool pool(std::thread::hardware_concurrency());

// Rekursive Tasks (ideal für Work Stealing)
auto fibonacci = [](auto& self, int n) -> Future<int> {
    if (n <= 1) return make_ready_future(n);

    auto f1 = pool.submit([&]() { return self(self, n - 1); });
    auto f2 = pool.submit([&]() { return self(self, n - 2); });

    return when_all(f1, f2).then([](auto results) {
        return std::get<0>(results) + std::get<1>(results);
    });
};

auto result = fibonacci(fibonacci, 10).get();
log::info("Fibonacci(10) = {}", result);
```

## Async/Await Pattern {#asyncawait}

### C++20 Coroutines

```cpp
#include <advlib/async/task.hpp>

using namespace advlib;

// Async Funktion
Task<int> fetch_data_async(const String& url) {
    // Simuliere async HTTP Request
    co_await async_sleep(std::chrono::seconds(1));

    log::info("Fetching from: {}", url);

    // Simuliere Antwort
    co_return 42;
}

// Verkettete Async Operations
Task<String> process_pipeline() {
    // Warte auf ersten Request
    int data1 = co_await fetch_data_async("https://api.example.com/data1");

    log::info("Got data1: {}", data1);

    // Warte auf zweiten Request (abhängig von erstem)
    int data2 = co_await fetch_data_async(
        format("https://api.example.com/data2?id={}", data1)
    );

    log::info("Got data2: {}", data2);

    // Verarbeite und return
    co_return format("Result: {}", data1 + data2);
}

// Parallele Async Operations
Task<std::vector<int>> fetch_multiple() {
    // Starte mehrere async operations parallel
    auto f1 = fetch_data_async("url1");
    auto f2 = fetch_data_async("url2");
    auto f3 = fetch_data_async("url3");

    // Warte auf alle
    auto results = co_await when_all(f1, f2, f3);

    co_return std::vector<int>{
        std::get<0>(results),
        std::get<1>(results),
        std::get<2>(results)
    };
}
```

### Async HTTP Client

```cpp
#include <advlib/net/http_client.hpp>

Task<void> http_example() {
    HttpClient client;

    // Einfacher GET Request
    auto response = co_await client.get("https://api.github.com/users/github");

    if (response.status() == 200) {
        log::info("Response: {}", response.body());
    }

    // POST Request
    json payload = {
        {"name", "John Doe"},
        {"email", "john@example.com"}
    };

    auto post_response = co_await client.post(
        "https://api.example.com/users",
        payload.dump(),
        {{"Content-Type", "application/json"}}
    );

    log::info("Created user, status: {}", post_response.status());

    // Parallele Requests
    auto [resp1, resp2, resp3] = co_await when_all(
        client.get("https://api.example.com/endpoint1"),
        client.get("https://api.example.com/endpoint2"),
        client.get("https://api.example.com/endpoint3")
    );

    log::info("All requests completed");
}
```

### Async mit Timeout

```cpp
Task<Result<int, String>> fetch_with_timeout(const String& url) {
    try {
        // Timeout nach 5 Sekunden
        auto result = co_await timeout(
            fetch_data_async(url),
            std::chrono::seconds(5)
        );

        co_return Ok(result);

    } catch (const TimeoutException& e) {
        co_return Err(String("Request timed out"));
    }
}
```

## Lock-Free Data Structures

### Lock-Free Queue

```cpp
#include <advlib/concurrency/lockfree_queue.hpp>

// SPSC: Single Producer Single Consumer
void spsc_example() {
    LockFreeQueue<int, QueueType::SPSC> queue(1024);

    // Producer Thread
    std::thread producer([&]() {
        for (int i = 0; i < 10000; ++i) {
            while (!queue.push(i)) {
                // Queue voll, retry
                std::this_thread::yield();
            }
        }
    });

    // Consumer Thread
    std::thread consumer([&]() {
        int value;
        int count = 0;

        while (count < 10000) {
            if (queue.pop(value)) {
                process(value);
                ++count;
            } else {
                std::this_thread::yield();
            }
        }
    });

    producer.join();
    consumer.join();
}

// MPMC: Multiple Producer Multiple Consumer
void mpmc_example() {
    LockFreeQueue<Task, QueueType::MPMC> queue(2048);

    // Mehrere Producer
    std::vector<std::thread> producers;
    for (int i = 0; i < 4; ++i) {
        producers.emplace_back([&, i]() {
            for (int j = 0; j < 1000; ++j) {
                Task task{i, j};
                while (!queue.push(task)) {
                    std::this_thread::yield();
                }
            }
        });
    }

    // Mehrere Consumer
    std::vector<std::thread> consumers;
    for (int i = 0; i < 4; ++i) {
        consumers.emplace_back([&]() {
            Task task;
            while (true) {
                if (queue.pop(task)) {
                    process_task(task);
                    if (is_termination_task(task)) {
                        break;
                    }
                }
            }
        });
    }

    // Wait for completion
    for (auto& t : producers) t.join();
    for (auto& t : consumers) t.join();
}
```

### Lock-Free Stack

```cpp
template<typename T>
class LockFreeStack {
public:
    void push(const T& value) {
        Node* new_node = new Node(value);
        new_node->next = head_.load(std::memory_order_relaxed);

        while (!head_.compare_exchange_weak(
            new_node->next,
            new_node,
            std::memory_order_release,
            std::memory_order_relaxed
        ));
    }

    bool pop(T& result) {
        Node* old_head = head_.load(std::memory_order_acquire);

        while (old_head != nullptr) {
            if (head_.compare_exchange_weak(
                old_head,
                old_head->next,
                std::memory_order_release,
                std::memory_order_acquire
            )) {
                result = old_head->value;
                delete old_head;
                return true;
            }
        }

        return false;
    }

private:
    struct Node {
        T value;
        Node* next;

        Node(const T& val) : value(val), next(nullptr) {}
    };

    std::atomic<Node*> head_{nullptr};
};
```

## Parallele Algorithmen

### Parallel For

```cpp
#include <advlib/algorithms/parallel.hpp>

// Einfaches parallel_for
std::vector<int> data(10000000);

parallel_for(0, data.size(), [&](size_t i) {
    data[i] = expensive_computation(i);
});

// Mit Chunk-Size
parallel_for(0, data.size(), [&](size_t i) {
    data[i] = process(i);
}, 1000);  // Process in chunks of 1000

// 2D Parallel For
parallel_for_2d(0, height, 0, width, [&](size_t y, size_t x) {
    image[y][x] = compute_pixel(x, y);
});
```

### Parallel Algorithms

```cpp
std::vector<int> numbers(1000000);
std::iota(numbers.begin(), numbers.end(), 0);

// Parallel Sort
parallel_sort(numbers.begin(), numbers.end());

// Parallel Transform
std::vector<int> squared(numbers.size());
parallel_transform(
    numbers.begin(), numbers.end(),
    squared.begin(),
    [](int x) { return x * x; }
);

// Parallel Reduce
auto sum = parallel_reduce(
    numbers.begin(), numbers.end(),
    0,
    std::plus<>()
);

log::info("Sum: {}", sum);

// Parallel Filter
auto evens = parallel_filter(numbers, [](int x) {
    return x % 2 == 0;
});

// Parallel Map-Reduce
auto word_counts = parallel_map_reduce(
    documents.begin(), documents.end(),
    // Map phase
    [](const Document& doc) {
        return count_words(doc);
    },
    // Reduce phase
    [](const WordCount& a, const WordCount& b) {
        return merge_counts(a, b);
    }
);
```

## Memory Ordering

### Understanding Memory Order

```cpp
#include <advlib/concurrency/atomic.hpp>

class SpinLock {
public:
    void lock() {
        while (flag_.exchange(true, std::memory_order_acquire)) {
            // Busy wait
            while (flag_.load(std::memory_order_relaxed)) {
                std::this_thread::yield();
            }
        }
    }

    void unlock() {
        flag_.store(false, std::memory_order_release);
    }

private:
    std::atomic<bool> flag_{false};
};

// Sequentially Consistent Ordering (Strongest)
std::atomic<int> seq_var{0};
seq_var.store(42, std::memory_order_seq_cst);
int value = seq_var.load(std::memory_order_seq_cst);

// Release-Acquire Ordering
std::atomic<bool> ready{false};
int data = 0;

// Thread 1 (Producer)
void producer() {
    data = 42;  // Non-atomic write
    ready.store(true, std::memory_order_release);  // Synchronizes with acquire
}

// Thread 2 (Consumer)
void consumer() {
    while (!ready.load(std::memory_order_acquire)) {
        // Wait
    }
    // data is guaranteed to be 42
    assert(data == 42);
}

// Relaxed Ordering (Weakest, only atomicity)
std::atomic<int> counter{0};
void increment() {
    counter.fetch_add(1, std::memory_order_relaxed);
}
```

### Double-Checked Locking Pattern

```cpp
class Singleton {
public:
    static Singleton& instance() {
        Singleton* tmp = instance_.load(std::memory_order_acquire);

        if (tmp == nullptr) {
            std::lock_guard<std::mutex> lock(mutex_);
            tmp = instance_.load(std::memory_order_relaxed);

            if (tmp == nullptr) {
                tmp = new Singleton();
                instance_.store(tmp, std::memory_order_release);
            }
        }

        return *tmp;
    }

private:
    Singleton() = default;

    static std::atomic<Singleton*> instance_;
    static std::mutex mutex_;
};
```

## Best Practices

### Avoid Data Races

```cpp
// BAD: Data Race
int shared_data = 0;

void thread1() {
    shared_data = 42;  // Unsynchronized write
}

void thread2() {
    if (shared_data == 42) {  // Unsynchronized read
        // May not see the write!
    }
}

// GOOD: Synchronized
std::atomic<int> shared_data{0};

void thread1() {
    shared_data.store(42, std::memory_order_release);
}

void thread2() {
    if (shared_data.load(std::memory_order_acquire) == 42) {
        // Guaranteed to see the write
    }
}
```

### Prefer High-Level Abstractions

```cpp
// Instead of manual thread management
// BAD:
std::vector<std::thread> threads;
for (int i = 0; i < 8; ++i) {
    threads.emplace_back([&, i]() {
        process_chunk(i);
    });
}
for (auto& t : threads) t.join();

// GOOD: Use thread pool
ThreadPool pool(8);
for (int i = 0; i < 8; ++i) {
    pool.submit([i]() {
        process_chunk(i);
    });
}
pool.wait_all();
```

## Performance Tips

1. **Minimize Contention**: Reduce shared state
2. **Use Lock-Free**: When possible and appropriate
3. **Batch Operations**: Reduce synchronization overhead
4. **Appropriate Granularity**: Not too fine, not too coarse
5. **Profile First**: Measure before optimizing

## Zusammenfassung

Du hast gelernt:

- Thread Pools für effiziente Task-Verwaltung
- Async/Await für eleganten asynchronen Code
- Lock-Free Data Structures für maximale Performance
- Parallele Algorithmen für Multi-Core Nutzung
- Memory Ordering für korrektes Concurrent Programming

## Weitere Ressourcen

- [Architecture: Threading Model](../architecture/threading.md)
- [API Reference: Concurrency](../api-reference/concurrency.md)
- [Performance Optimization](advanced-performance.md)
