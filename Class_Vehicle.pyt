class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(250, 17)

print("Model max speed:",modelX.max_speed)
print("Model mileage:",modelX.mileage)