class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, breed, name, info):
        self.breed = breed
        self.name = name
        self.info = info

    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")
        print(f"Info: {self.info}")

dog1 = Dog("Labrador Retriever", "Buddy", "Friendly and outgoing breed, great for families.")
dog2 = Dog("German Shepherd", "Max", "Intelligent and loyal, often used as a working dog.")

dog1.display_details()
dog2.display_details()
