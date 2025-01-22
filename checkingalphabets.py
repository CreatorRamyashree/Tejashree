def check_alphabet(char):
    if char.isalpha():
        if char.islower():
            return f"'{char}' is a lowercase alphabet."
        elif char.isupper():
            return f"'{char}' is an uppercase alphabet."
    else:
        return f"'{char}' is not an alphabet."

char = input("Enter a character: ")

if len(char) == 1:
    result = check_alphabet(char)
    print(result)
else:
    print("Please enter only one character!")
