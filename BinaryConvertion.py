def decimal_to_binary(n):
    if n == 0:
        return "0"

    integer_part = int(n)
    fractional_part = abs(n - integer_part)     
   
    binary_integer = "0" if integer_part == 0 else ""
    while integer_part > 0:
        remainder = integer_part % 2
        binary_integer = str(remainder) + binary_integer
        integer_part //= 2

    binary_fractional = ""
    count = 0
    while fractional_part > 0 and count < 10:  
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        count += 1

    return binary_integer + ("." + binary_fractional if binary_fractional else "")

try:
    num = float(input("Enter a decimal number: "))
    print(f"Decimal: {num} -> Binary: {decimal_to_binary(num)}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
