def separate_squares(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print("All Squares:", squares)
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

separate_squares(start_range, end_range)