import array as arr

array_num= arr.array("b", [2, 4, 5, 5, 2, 3, 4, 7, 5, 5, 4])
print("Original array: "+ str(array_num))
print("Number of occurences of the number 5 in the said array is:" +str(array_num.count(4)))

a= [2, 4, 6, 8, 10]
a.reverse()
print("Reverse of the items:")
print(str(a))