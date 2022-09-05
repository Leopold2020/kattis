# number1 = int(input(""))
# number2 = number1
# amount_of_posetives = 0
# amount_of_negatives = 0

# while str(number1)[:2:-1] != "99":
#     number1 += 1
#     amount_of_posetives += 1

# while str(number2)[:2:-1] != "99":
#     number2 -= 1
#     amount_of_negatives += 1

# if amount_of_negatives > amount_of_posetives:
#     print(number1)

# if amount_of_posetives > amount_of_negatives:
#     print(number2)

number = int(input())

if number < 100:
    print("99")

else:
    number += 1.1

    print(round(number/100)*100-1)