# HTTP Parser API Documentation

## Class: http_parser

The `http_parser` class provides a comprehensive interface for parsing HTTP messages, including headers, status codes, and body content. It supports various HTTP features such as chunked encoding, content length tracking, and header extraction.

### http_parser (Constructor)
```cpp
explicit http_parser(int flags = 0);
```

**Description**: Constructs a new HTTP parser with optional configuration flags. The parser can be configured to skip chunk parsing if needed.

**Parameters**:
- `flags` (int): Configuration flags for the parser. Valid values include `dont_parse_chunks` to skip parsing chunked content. Default is 0 (no special flags).

**Return Value**: 
- Constructs and initializes a new `http_parser` instance.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
// Create a parser with default settings
http_parser parser;

// Create a parser that skips chunk parsing
http_parser parser(http_parser::dont_parse_chunks);
```

**Preconditions**: None
**Postconditions**: The parser is initialized and ready to parse HTTP messages
**Thread Safety**: Not thread-safe (constructors should not be called concurrently)
**Complexity**: O(1)

### ~http_parser (Destructor)
```cpp
~http_parser();
```

**Description**: Destroys the HTTP parser instance, releasing any allocated resources.

**Parameters**: None

**Return Value**: None

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
{
    http_parser parser;
    // Use parser...
} // parser is automatically destroyed here
```

**Preconditions**: The parser must be in a valid state
**Postconditions**: All resources are released
**Thread Safety**: Not thread-safe
**Complexity**: O(1)

### header
```cpp
std::string const& header(string_view key) const;
```

**Description**: Retrieves the value of a specific HTTP header field. This method provides access to the parsed header values.

**Parameters**:
- `key` (string_view): The name of the header field to retrieve. Case-sensitive.

**Return Value**:
- Returns a reference to the header value as a `std::string`. If the header is not found, the behavior is undefined (implementation-dependent).

**Exceptions/Errors**:
- No exceptions are thrown.
- If the header is not present, the returned string may be empty or contain garbage (implementation-dependent).

**Example**:
```cpp
http_parser parser;
// Assume parser has been populated with HTTP data
auto content_type = parser.header("Content-Type");
if (!content_type.empty()) {
    std::cout << "Content-Type: " << content_type << std::endl;
}
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid string reference to the header value
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(log n) where n is the number of headers

### header_duration
```cpp
boost::optional<seconds32> header_duration(string_view key) const;
```

**Description**: Retrieves a header value and parses it as a duration (time interval). This is useful for headers like "Timeout" or "Keep-Alive" that specify time durations.

**Parameters**:
- `key` (string_view): The name of the header field to parse as a duration.

**Return Value**:
- Returns a `boost::optional<seconds32>` containing the parsed duration if successful.
- Returns `boost::none` if the header doesn't exist or cannot be parsed as a duration.

**Exceptions/Errors**:
- No exceptions are thrown.
- Returns `boost::none` for invalid values or missing headers.

**Example**:
```cpp
http_parser parser;
auto timeout = parser.header_duration("Keep-Alive");
if (timeout) {
    std::cout << "Keep-Alive timeout: " << *timeout << " seconds" << std::endl;
} else {
    std::cout << "No Keep-Alive header or invalid value" << std::endl;
}
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid optional duration or boost::none
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(log n) where n is the number of headers

### protocol
```cpp
std::string const& protocol() const;
```

**Description**: Returns the HTTP protocol version (e.g., "HTTP/1.1") of the parsed message.

**Parameters**: None

**Return Value**: Returns a reference to the protocol string (e.g., "HTTP/1.1").

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned string is valid as long as the parser instance exists.

**Example**:
```cpp
http_parser parser;
std::string protocol_version = parser.protocol();
std::cout << "Protocol: " << protocol_version << std::endl;
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid string reference to the protocol version
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### status_code
```cpp
int status_code() const;
```

**Description**: Returns the HTTP status code of the parsed message (e.g., 200 for OK, 404 for Not Found).

**Parameters**: None

**Return Value**: Returns the HTTP status code as an integer.

**Exceptions/Errors**:
- No exceptions are thrown.
- The value is valid only after parsing a complete HTTP response.

**Example**:
```cpp
http_parser parser;
int status = parser.status_code();
if (status == 200) {
    std::cout << "Request successful" << std::endl;
} else {
    std::cout << "HTTP error: " << status << std::endl;
}
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid HTTP status code
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### method
```cpp
std::string const& method() const;
```

**Description**: Returns the HTTP method (e.g., "GET", "POST", "PUT") of the parsed message.

**Parameters**: None

**Return Value**: Returns a reference to the HTTP method string.

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned string is valid as long as the parser instance exists.

**Example**:
```cpp
http_parser parser;
std::string method = parser.method();
std::cout << "Method: " << method << std::endl;
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid string reference to the HTTP method
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### path
```cpp
std::string const& path() const;
```

**Description**: Returns the path component of the URL from the HTTP request line.

**Parameters**: None

**Return Value**: Returns a reference to the path string (e.g., "/api/v1/users").

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned string is valid as long as the parser instance exists.

**Example**:
```cpp
http_parser parser;
std::string path = parser.path();
std::cout << "Path: " << path << std::endl;
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid string reference to the path
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### message
```cpp
std::string const& message() const;
```

**Description**: Returns the server message from an HTTP response, typically found in the status line (e.g., "OK", "Not Found", "Internal Server Error").

**Parameters**: None

**Return Value**: Returns a reference to the server message string.

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned string is valid as long as the parser instance exists.

**Example**:
```cpp
http_parser parser;
std::string message = parser.message();
std::cout << "Message: " << message << std::endl;
```

**Preconditions**: The parser must have been initialized and parsed at least one HTTP message
**Postconditions**: Returns a valid string reference to the server message
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### header_finished
```cpp
bool header_finished() const;
```

**Description**: Checks whether the header parsing phase is complete. This indicates that all headers have been parsed and the body is about to be processed.

**Parameters**: None

**Return Value**: 
- Returns `true` if header parsing is complete.
- Returns `false` if header parsing is still in progress or has not started.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
http_parser parser;
// Assume parser is in the middle of parsing
if (parser.header_finished()) {
    std::cout << "Headers have been fully parsed" << std::endl;
} else {
    std::cout << "Still parsing headers" << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a boolean indicating header parsing status
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### finished
```cpp
bool finished() const;
```

**Description**: Checks whether the entire HTTP message parsing is complete.

**Parameters**: None

**Return Value**: 
- Returns `true` if the entire message has been parsed.
- Returns `false` if parsing is incomplete.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
http_parser parser;
// Assume parser is in the middle of parsing
if (parser.finished()) {
    std::cout << "Message parsing complete" << std::endl;
} else {
    std::cout << "Parsing still in progress" << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a boolean indicating parsing completion
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### body_start
```cpp
int body_start() const;
```

**Description**: Returns the position where the body starts in the original data stream.

**Parameters**: None

**Return Value**: Returns the byte offset where the body begins, or -1 if the body hasn't started yet.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
http_parser parser;
int body_start_pos = parser.body_start();
if (body_start_pos >= 0) {
    std::cout << "Body starts at position: " << body_start_pos << std::endl;
} else {
    std::cout << "Body has not started yet" << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a valid position or -1
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### content_length
```cpp
std::int64_t content_length() const;
```

**Description**: Returns the content length of the HTTP message as specified in the "Content-Length" header.

**Parameters**: None

**Return Value**: Returns the content length as a 64-bit integer. If the header is not present, returns 0.

**Exceptions/Errors**:
- No exceptions are thrown.
- If the Content-Length header is invalid, the behavior may be undefined.

**Example**:
```cpp
http_parser parser;
std::int64_t length = parser.content_length();
std::cout << "Content length: " << length << " bytes" << std::endl;
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a valid content length
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### content_range
```cpp
std::pair<std::int64_t, std::int64_t> content_range() const;
```

**Description**: Returns the content range as specified in the "Content-Range" header, typically in the format "bytes start-end/total".

**Parameters**: None

**Return Value**: Returns a pair where the first element is the start position and the second is the end position of the content range.

**Exceptions/Errors**:
- No exceptions are thrown.
- If the Content-Range header is not present or invalid, the behavior may be undefined.

**Example**:
```cpp
http_parser parser;
auto range = parser.content_range();
std::cout << "Content range: " << range.first << "-" << range.second << std::endl;
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a valid content range pair
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### chunked_encoding
```cpp
bool chunked_encoding() const;
```

**Description**: Checks whether the message uses chunked encoding, which allows for streaming of data without knowing the total size in advance.

**Parameters**: None

**Return Value**: 
- Returns `true` if the message uses chunked encoding.
- Returns `false` otherwise.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
http_parser parser;
if (parser.chunked_encoding()) {
    std::cout << "Using chunked encoding" << std::endl;
} else {
    std::cout << "Not using chunked encoding" << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a boolean indicating chunked encoding status
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### connection_close
```cpp
bool connection_close() const;
```

**Description**: Checks whether the connection should be closed after this request/response.

**Parameters**: None

**Return Value**: 
- Returns `true` if the connection should be closed.
- Returns `false` if the connection should be kept alive.

**Exceptions/Errors**:
- No exceptions are thrown.

**Example**:
```cpp
http_parser parser;
if (parser.connection_close()) {
    std::cout << "Connection should be closed after this request" << std::endl;
} else {
    std::cout << "Connection should be kept alive" << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a boolean indicating connection close status
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1)

### headers
```cpp
std::multimap<std::string, std::string, aux::strview_less> const& headers() const;
```

**Description**: Returns a read-only reference to the complete set of parsed headers. The headers are stored in a multimap that preserves insertion order and allows multiple headers with the same name.

**Parameters**: None

**Return Value**: Returns a reference to the multimap containing all parsed headers.

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned reference is valid for the lifetime of the parser instance.

**Example**:
```cpp
http_parser parser;
auto const& header_map = parser.headers();
for (auto const& [key, value] : header_map) {
    std::cout << key << ": " << value << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a valid reference to the header multimap
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1) to return reference, O(n) to iterate

### chunks
```cpp
std::vector<std::pair<std::int64_t, std::int64_t>> const& chunks() const;
```

**Description**: Returns the chunk ranges for chunked encoding, providing information about the size and position of each chunk.

**Parameters**: None

**Return Value**: Returns a reference to a vector of pairs, where each pair represents the start and end positions of a chunk.

**Exceptions/Errors**:
- No exceptions are thrown.
- The returned reference is valid for the lifetime of the parser instance.

**Example**:
```cpp
http_parser parser;
auto const& chunk_ranges = parser.chunks();
for (auto const& [start, end] : chunk_ranges) {
    std::cout << "Chunk: " << start << " to " << end << std::endl;
}
```

**Preconditions**: The parser must have been initialized
**Postconditions**: Returns a valid reference to the chunk ranges vector
**Thread Safety**: Thread-safe (reads only)
**Complexity**: O(1) to return reference, O(n) to iterate

## Usage Examples

### Basic Usage
```cpp
#include "http_parser.hpp"
#include <iostream>
#include <string>

int main() {
    // Create a parser
    http_parser parser;
    
    // Parse some HTTP data (in practice, this would be streamed)
    // Assume data is in a buffer called 'http_data'
    
    // After parsing, access the results
    std::cout << "Protocol: " << parser.protocol() << std::endl;
    std::cout << "Status code: " << parser.status_code() << std::endl;
    std::cout << "Method: " << parser.method() << std::endl;
    std::cout << "Path: " << parser.path() << std::endl;
    
    // Check header values
    auto content_type = parser.header("Content-Type");
    if (!content_type.empty()) {
        std::cout << "Content-Type: " << content_type << std::endl;
    }
    
    // Check if we're done parsing
    if (parser.finished()) {
        std::cout << "Parsing complete" << std::endl;
    }
    
    return 0;
}
```

### Error Handling
```cpp
#include "http_parser.hpp"
#include <iostream>
#include <string>

void process_http_response(const std::string& http_data) {
    http_parser parser;
    
    // Process the HTTP data
    // In real implementation, this would involve calling a parsing method
    // (not shown in the interface)
    
    // Check for parsing errors
    if (parser.finished()) {
        std::cout << "Processing successful" << std::endl;
    } else {
        std::cout << "Parsing incomplete or failed" << std::endl;
    }
    
    // Check for specific header values with fallback
    auto status_code = parser.status_code();
    if (status_code == 200) {
        std::cout << "Success: " << parser.message() <<