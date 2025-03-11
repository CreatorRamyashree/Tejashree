country_code = {"India": "0091", "Australia": "0025", "Nepal": "00977", "Congo": "00243"}

print("Country code for India - ")
print(country_code.get("India", "Not Found"))

print("Country code for Japan - ")
print(country_code.get("Japan", "Not Found"))

print("Country code for Congo - ")
print(country_code.get("Congo", "Not Found"))
