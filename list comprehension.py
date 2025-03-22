num = int(input("Enter a number: "))
odds_under_num = [i for i in range(num) if i % 2 != 0]
odds_list = [i for i in range(1, num*2, 2)]
print("Odd numbers under input:", odds_under_num)
print("Odd numbers list:", odds_list)

