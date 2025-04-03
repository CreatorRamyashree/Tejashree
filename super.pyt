class bird:
    def _init_(self):
        print(" Bird is ready.")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print(" Swim faster!")
class penguin(bird):
    def _init_(self):
        super()._init_()
        print(" Penguin is ready.")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster!")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()