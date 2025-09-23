# Python NumPy Library
NumPy is a fundamental package for scientific computing in Python. It provides a high-performance multidimensional array object and tools for working with these arrays. This guide covers some of the essential functionalities of the NumPy library.

### 1. Creating Arrays
Arrays are the core data structure in NumPy. They can be created from Python lists or nested lists.

- 1D Array: A single row of data.
```python
import numpy as np

my_list = [1, 2, 3, 4, 5]
array_from_list = np.array(my_list)
print(f"---- 1D Array ---- \n{array_from_list}")
```
- 2D Array: A grid of data with rows and columns.
```python
nested_list = [[1, 2, 3], [4, 5, 6]]
two_d_array = np.array(nested_list)
print(f"---- 2D Array ---- \n {two_d_array}")
```

### 2. Array Attributes and Basic Operations
NumPy arrays have various attributes that provide information about their structure and content. You can also perform basic mathematical operations on them.
```python
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print("Original 1D Array:", arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)
print("Sum:", arr1.sum())
print("Mean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())
```

- `shape`: The dimensions of the array. For `arr1`, the shape `(5,)` means it has 5 elements.

- `dtype`: The data type of the elements in the array (e.g., `int64`).

### 3. Element-wise Operations
NumPy allows you to perform mathematical operations on every element of an array efficiently, a concept known as vectorization.
```python
arr1 = np.array([10, 20, 30, 40, 50])

print("Array + 5:", arr1 + 5)
print("Array * 2:", arr1 * 2)

# Operations between two arrays
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])

print("Element-wise Addition:", arr3 + arr4)
print("Element-wise Subtraction:", arr3 - arr4)
print("Element-wise Multiplication:", arr3 * arr4)
```
### 4. Array Indexing and Slicing
You can access and modify parts of an array using indexing and slicing, similar to Python lists.

```python
arr1 = np.array([10, 20, 30, 40, 50])
print("First 3 elements:", arr1[:3])
print("Last 2 elements:", arr1[-2:])
```
For 2D arrays, you specify both the row and column.

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Access a single element
print("Element at (0, 1):", arr2[0, 1])

# Access an entire row
print("First row:", arr2[0])

# Access an entire column
print("Second column:", arr2[:, 1])
```
### 5. Array Manipulation
NumPy provides powerful functions for changing the shape and structure of arrays.

- Transpose (`.T`): Flips the array over its diagonal, so rows become columns and vice versa.

```Python

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Transposed Array:\n", arr2.T)
```
- Reshape (`.reshape()`): Changes the shape of an array without changing its data.
```Python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = arr2.reshape((3, 2))
print("Reshaped Array:\n", reshaped)
```

- Flatten (`.flatten()`): Converts a multidimensional array into a 1D array.
```Python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
flat = arr2.flatten()
print("Flattened Array:", flat)
```
- Concatenate (`np.concatenate`): Joins a sequence of arrays along an existing axis.

```Python

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("Concatenated:\n", concatenated_arr)
```