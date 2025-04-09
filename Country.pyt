class india():
    def capital(self):
        print("New Dheli is the capital city of India.")
    def language(self):
        print("English is the offical language in India.")
    def type(self):
        print("India is a developing country.")

class congo:
    def capital(self):
        print("Kinshasa is the capital city of Congo.")
    def language(self):
        print("French is the official language of Congo.")
    def type(self):
        print("Congo is also a developing country.")

obj_ind = india()
obj_con = congo()

for country in (obj_ind, obj_con):
    country.capital()
    country.language()
    country.type()