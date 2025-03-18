s1 = {4, 3, 2}
s2 = {"e", "g", "f"}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [12, 4, 34, 6, 36, 24]
list2 = [5, 4, 3, 2, 1, 0]

for x, y, in zip(list1, list2[::-1]):
    print(x, y)

stocks = ["Videocom", "AAI", "Coca Cola"]
prices = [5620, 9807, 3621]

new_dict = { stocks: prices for stocks, prices in zip(stocks, prices)}
print("\n", format(new_dict))