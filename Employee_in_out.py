class employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructer called")
def create_obj():
    print("Making object...")
    obj = employee()
    print("fuction end...")
    return obj
print("Calling create_obj() function...")
obj = create_obj()
print("Program end...")