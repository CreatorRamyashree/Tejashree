def mirrored_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
        
n = int(input("Enter the number of rows for the mirrored triangle: "))
mirrored_triangle(n)
