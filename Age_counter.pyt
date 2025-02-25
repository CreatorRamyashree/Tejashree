def check_age():
    try:
        age = int(input("Enter your age: "))
        
        if age <= 0:
            print("Error: Age must be a positive integer.")
        else:
            if age % 2 == 0:
                print(f"The entered age {age} is even.")
            else:
                print(f"The entered age {age} is odd.")
    
    except ValueError:
        print("Error: Please enter a valid number.")
check_age()
