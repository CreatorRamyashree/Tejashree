class science:
    def _init_(self, physics, chemistry, biology):
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
class biology(science):
    pass
Living = biology(78, 98, 74)
print(Living.physics, Living.chemistry, Living.biology)