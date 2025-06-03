import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])

print(arr2.shape)
print(arr2.dtype)

print(arr1[0])
print(arr1[1:4])

print(arr2[1, 1])
print(arr2[:, 0])

arr = np.array([1, 2, 3])
print(arr + 5)
print(arr * 2)
print(arr ** 2)

data = np.array([10, 20, 30, 40])
print(np.mean(data))
print(np.max(data))
print(np.min(data))
print(np.std(data))

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape((2, 3))
print(b)

x = np.array([1, 2])
y = np.array([3, 4])
print(np.concatenate((x, y)))

nums = np.array([1, 2, 3, 4, 5, 6])
even = nums[nums % 2 == 0]
print(even)

unsorted = np.array([5, 3, 1, 4, 2])
sorted_arr = np.sort(unsorted)
print(sorted_arr)

print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))