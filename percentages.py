print("Enter marks obtained in the 4 subjects:")
math= int(input("Math:"))
science= int(input("Science: "))
art= int(input("Art: "))
ins= int(input("InS: "))

sum= math+science+art+ins
print("sum of math, science, art, and ins is: ", sum)

perc= (sum/400)*100

print(end = "Percentage: ")
print(perc)
