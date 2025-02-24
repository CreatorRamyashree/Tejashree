try:
    num1, num2 = eval(input("Enter two numbers, separated using a coma:"))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error!!")
except SyntaxError:
    print("Coma is missing. Enter numbers using a coma like this; 1,2")
except:
    print("Wrong input!")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what.")