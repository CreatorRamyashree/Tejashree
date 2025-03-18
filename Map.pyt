numbers1 = [4, 5, 6]
numbers2 = [7, 8, 9]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

nums = [10, 11, 12, 13, 14, 15]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in the list")
print(square)