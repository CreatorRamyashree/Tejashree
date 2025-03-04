L = [3, 5, 7, 21, 74, 13, 8, 10]
print("Original list: ", L)

count = 0

for i in L:
    count += i
    
avg = count/len(L)
print("Sum is qequal to: ", count)
print("Average is equal to: ", avg)

L.sort()
Large = L.sort(print("Largest element is: ", L[-1]))
print(Large) 

Small = L.sort(print("Smallest element is: ", L[0]))
print(Small)