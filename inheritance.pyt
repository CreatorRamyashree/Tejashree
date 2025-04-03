class dad:
    def _init_(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive
    def display(self):
         print(" Your eye color is", self.eyes)
         print(" You are aggressive", self.aggressive)

class son(dad):
    def _init_(self, name, age, eyes, aggressive):
        self.name = name
        self.age = age
        super()._init_(eyes, aggressive)
obj = son("Penguin", 8, "blue", True)
obj.display()
obj2 = son(" Panda", 7, "green", True)
obj2.display()