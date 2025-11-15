# C++ Python Bindings Converters API Documentation

## Function: convert (Endpoint to Python Tuple)

- **Signature**: `static PyObject* convert(T const& ep)`
- **Description**: Converts a network endpoint (IP address and port) to a Python tuple containing the string representation of the IP address and the port number. This function is used as part of the Boost.Python conversion system to automatically convert C++ endpoint objects to Python tuples.
- **Parameters**:
  - `ep` (T const&): The endpoint object to convert, where T is a network endpoint type (likely `lt::endpoint` or similar). The endpoint must be valid and contain both an IP address and port.
- **Return Value**:
  - `PyObject*`: A reference to a Python tuple containing the IP address string and port number. The reference count is incremented, so the caller must eventually decref the returned object.
- **Exceptions/Errors**:
  - No exceptions thrown
  - Potential memory allocation failure if `bp::make_tuple` fails
- **Example**:
```cpp
// This function would typically be used internally in the converter registration
// Not directly called by users
PyObject* py_tuple = convert(my_endpoint);
```
- **Preconditions**: The endpoint object must be valid and properly initialized.
- **Postconditions**: Returns a valid Python tuple object with the endpoint information.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time and space complexity.

## Function: tuple_to_endpoint

- **Signature**: `tuple_to_endpoint()`
- **Description**: Registers a conversion from Python tuples to C++ network endpoint objects. This function registers the conversion logic with the Boost.Python converter registry so that Python tuples (containing IP address string and port) can be automatically converted to C++ endpoint objects.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called during initialization
tuple_to_endpoint();
// Now Python tuples can be converted to endpoints
```
- **Preconditions**: The Boost.Python converter registry must be initialized.
- **Postconditions**: Registers a conversion from Python tuples to C++ endpoint objects.
- **Thread Safety**: Not thread-safe - should only be called during initialization.
- **Complexity**: O(1) time and space complexity.

## Function: convertible (Endpoint)

- **Signature**: `static void* convertible(PyObject* x)`
- **Description**: Checks if a Python object can be converted to a network endpoint. This function is part of the Boost.Python conversion system and is called during the conversion process to determine if a given Python object can be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python object to check for convertibility. This should be a tuple with exactly two elements.
- **Return Value**:
  - `void*`: Returns the Python object if it can be converted to an endpoint, otherwise returns nullptr.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
PyObject* py_tuple = Py_BuildValue("(sH)", "192.168.1.1", 8080);
void* result = convertible(py_tuple);
if (result) {
    // The object can be converted
}
```
- **Preconditions**: The Python object must be valid and not NULL.
- **Postconditions**: Returns the object if it can be converted to an endpoint, otherwise returns nullptr.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.

## Function: construct (Endpoint)

- **Signature**: `static void construct(PyObject* x, converter::rvalue_from_python_stage1_data* data)`
- **Description**: Constructs a C++ endpoint object from a Python tuple during the conversion process. This function is called by Boost.Python when a convertible Python object is found and needs to be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python tuple containing the IP address string and port number.
  - `data` (converter::rvalue_from_python_stage1_data*): The conversion data structure that provides storage for the constructed object.
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
// Not directly called by users
converter::rvalue_from_python_stage1_data data;
construct(py_tuple, &data);
// The converted endpoint object is now stored in data
```
- **Preconditions**: The Python object must be convertible as checked by the `convertible` function.
- **Postconditions**: Constructs a C++ endpoint object in the storage provided by the data parameter.
- **Thread Safety**: Not thread-safe - should not be called concurrently.
- **Complexity**: O(1) time and space complexity.

## Function: convert (Pair to Tuple)

- **Signature**: `static PyObject* convert(const std::pair<T1, T2>& p)`
- **Description**: Converts a C++ pair to a Python tuple. This function is used as part of the Boost.Python conversion system to automatically convert C++ pair objects to Python tuples.
- **Parameters**:
  - `p` (const std::pair<T1, T2>&): The pair object to convert, where T1 and T2 are the types of the pair elements.
- **Return Value**:
  - `PyObject*`: A reference to a Python tuple containing the pair elements. The reference count is incremented.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
std::pair<int, std::string> my_pair(42, "hello");
PyObject* py_tuple = convert(my_pair);
```
- **Preconditions**: The pair object must be valid and properly initialized.
- **Postconditions**: Returns a valid Python tuple object with the pair elements.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time and space complexity.

## Function: convert (Address to String)

- **Signature**: `static PyObject* convert(Addr const& addr)`
- **Description**: Converts a network address to a Python string. This function is used as part of the Boost.Python conversion system to automatically convert C++ address objects to Python strings.
- **Parameters**:
  - `addr` (Addr const&): The address object to convert.
- **Return Value**:
  - `PyObject*`: A reference to a Python string containing the string representation of the address. The reference count is incremented.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function would typically be used internally in the converter registration
// Not directly called by users
PyObject* py_string = convert(my_address);
```
- **Preconditions**: The address object must be valid and properly initialized.
- **Postconditions**: Returns a valid Python string object with the address representation.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(1) time and space complexity.

## Function: tuple_to_pair

- **Signature**: `tuple_to_pair()`
- **Description**: Registers a conversion from Python tuples to C++ pair objects. This function registers the conversion logic with the Boost.Python converter registry so that Python tuples can be automatically converted to C++ pair objects.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called during initialization
tuple_to_pair();
// Now Python tuples can be converted to pairs
```
- **Preconditions**: The Boost.Python converter registry must be initialized.
- **Postconditions**: Registers a conversion from Python tuples to C++ pair objects.
- **Thread Safety**: Not thread-safe - should only be called during initialization.
- **Complexity**: O(1) time and space complexity.

## Function: convertible (Pair)

- **Signature**: `static void* convertible(PyObject* x)`
- **Description**: Checks if a Python object can be converted to a pair. This function is part of the Boost.Python conversion system and is called during the conversion process to determine if a given Python object can be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python object to check for convertibility. This should be a tuple with exactly two elements.
- **Return Value**:
  - `void*`: Returns the Python object if it can be converted to a pair, otherwise returns nullptr.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
PyObject* py_tuple = Py_BuildValue("(iO)", 42, PyString_FromString("hello"));
void* result = convertible(py_tuple);
if (result) {
    // The object can be converted
}
```
- **Preconditions**: The Python object must be valid and not NULL.
- **Postconditions**: Returns the object if it can be converted to a pair, otherwise returns nullptr.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.

## Function: construct (Pair)

- **Signature**: `static void construct(PyObject* x, converter::rvalue_from_python_stage1_data* data)`
- **Description**: Constructs a C++ pair object from a Python tuple during the conversion process. This function is called by Boost.Python when a convertible Python object is found and needs to be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python tuple containing the pair elements.
  - `data` (converter::rvalue_from_python_stage1_data*): The conversion data structure that provides storage for the constructed object.
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
// Not directly called by users
converter::rvalue_from_python_stage1_data data;
construct(py_tuple, &data);
// The converted pair object is now stored in data
```
- **Preconditions**: The Python object must be convertible as checked by the `convertible` function.
- **Postconditions**: Constructs a C++ pair object in the storage provided by the data parameter.
- **Thread Safety**: Not thread-safe - should not be called concurrently.
- **Complexity**: O(1) time and space complexity.

## Function: convert (String View)

- **Signature**: `static PyObject* convert(lt::string_view v)`
- **Description**: Converts a string view to a Python string object. This function is used as part of the Boost.Python conversion system to automatically convert C++ string views to Python strings.
- **Parameters**:
  - `v` (lt::string_view): The string view to convert.
- **Return Value**:
  - `PyObject*`: A reference to a Python string object containing the string view content. The reference count is incremented.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function would typically be used internally in the converter registration
// Not directly called by users
lt::string_view sv("hello world");
PyObject* py_string = convert(sv);
```
- **Preconditions**: The string view must be valid and not contain invalid characters.
- **Postconditions**: Returns a valid Python string object with the string view content.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(n) time complexity where n is the length of the string view.

## Function: to_string_view

- **Signature**: `to_string_view()`
- **Description**: Registers a conversion from Python objects to C++ string views. This function registers the conversion logic with the Boost.Python converter registry so that Python objects can be automatically converted to C++ string views.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called during initialization
to_string_view();
// Now Python objects can be converted to string views
```
- **Preconditions**: The Boost.Python converter registry must be initialized.
- **Postconditions**: Registers a conversion from Python objects to C++ string views.
- **Thread Safety**: Not thread-safe - should only be called during initialization.
- **Complexity**: O(1) time and space complexity.

## Function: construct (String View)

- **Signature**: `static void construct(PyObject* x, converter::rvalue_from_python_stage1_data* data)`
- **Description**: Constructs a C++ string view from a Python object during the conversion process. This function is called by Boost.Python when a convertible Python object is found and needs to be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python object to convert, which should be a string.
  - `data` (converter::rvalue_from_python_stage1_data*): The conversion data structure that provides storage for the constructed object.
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
// Not directly called by users
converter::rvalue_from_python_stage1_data data;
construct(py_string, &data);
// The converted string view object is now stored in data
```
- **Preconditions**: The Python object must be convertible as checked by the `convertible` function.
- **Postconditions**: Constructs a C++ string view in the storage provided by the data parameter.
- **Thread Safety**: Not thread-safe - should not be called concurrently.
- **Complexity**: O(1) time and space complexity.

## Function: convert (Map to Dictionary)

- **Signature**: `static PyObject* convert(Map const& m)`
- **Description**: Converts a C++ map to a Python dictionary. This function is used as part of the Boost.Python conversion system to automatically convert C++ map objects to Python dictionaries.
- **Parameters**:
  - `m` (Map const&): The map object to convert.
- **Return Value**:
  - `PyObject*`: A reference to a Python dictionary containing the map elements. The reference count is incremented.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function would typically be used internally in the converter registration
// Not directly called by users
std::map<std::string, int> my_map = {{"key1", 1}, {"key2", 2}};
PyObject* py_dict = convert(my_map);
```
- **Preconditions**: The map object must be valid and properly initialized.
- **Postconditions**: Returns a valid Python dictionary object with the map elements.
- **Thread Safety**: Thread-safe as it only reads from the input parameter.
- **Complexity**: O(n) time complexity where n is the number of elements in the map.

## Function: dict_to_map

- **Signature**: `dict_to_map()`
- **Description**: Registers a conversion from Python dictionaries to C++ map objects. This function registers the conversion logic with the Boost.Python converter registry so that Python dictionaries can be automatically converted to C++ map objects.
- **Parameters**: None
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called during initialization
dict_to_map();
// Now Python dictionaries can be converted to maps
```
- **Preconditions**: The Boost.Python converter registry must be initialized.
- **Postconditions**: Registers a conversion from Python dictionaries to C++ map objects.
- **Thread Safety**: Not thread-safe - should only be called during initialization.
- **Complexity**: O(1) time and space complexity.

## Function: convertible (Map)

- **Signature**: `static void* convertible(PyObject* x)`
- **Description**: Checks if a Python object can be converted to a map. This function is part of the Boost.Python conversion system and is called during the conversion process to determine if a given Python object can be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python object to check for convertibility. This should be a dictionary.
- **Return Value**:
  - `void*`: Returns the Python object if it can be converted to a map, otherwise returns nullptr.
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
PyObject* py_dict = PyDict_New();
PyDict_SetItemString(py_dict, "key1", PyLong_FromLong(1));
PyDict_SetItemString(py_dict, "key2", PyLong_FromLong(2));
void* result = convertible(py_dict);
if (result) {
    // The object can be converted
}
```
- **Preconditions**: The Python object must be valid and not NULL.
- **Postconditions**: Returns the object if it can be converted to a map, otherwise returns nullptr.
- **Thread Safety**: Thread-safe.
- **Complexity**: O(1) time and space complexity.

## Function: construct (Map)

- **Signature**: `static void construct(PyObject* x, converter::rvalue_from_python_stage1_data* data)`
- **Description**: Constructs a C++ map object from a Python dictionary during the conversion process. This function is called by Boost.Python when a convertible Python object is found and needs to be converted to the target C++ type.
- **Parameters**:
  - `x` (PyObject*): The Python dictionary containing the map elements.
  - `data` (converter::rvalue_from_python_stage1_data*): The conversion data structure that provides storage for the constructed object.
- **Return Value**: None
- **Exceptions/Errors**:
  - None
- **Example**:
```cpp
// This function is called internally by Boost.Python
// Not directly called by users
converter::rvalue_from_python_stage1_data data;
construct(py_dict, &data);
// The converted map object is now stored in data
```
- **Preconditions**: The Python object must be convertible as checked by the `convertible` function.
- **Postconditions**: Constructs a C++ map object in the storage provided by the data parameter.
- **Thread Safety**: Not thread-safe - should not be called concurrently.
- **Complexity**: O(n) time complexity where n is the number of elements in the dictionary.

## Function: convert (Vector to List)

- **Signature**: `static PyObject* convert(T const& v)`
- **Description**: Converts a C++ vector to a Python list. This function is used as part of the Boost.Python conversion