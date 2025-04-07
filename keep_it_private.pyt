class myClass:
    __privateVar = 27
    def __privmeth(self):
        print("I'm inside class myClass")
    def __hello(self):
        print("Private variable value: ", myClass.__privateVar)

foo = myClass
foo.__hello
foo.__privMeth
