number = input()

numb1, numb2 = number.split(" ") 

number1 = numb1[::-1]
number2 = numb2[::-1]

if number1 > number2:
    print(number1)

else:
    print(number2)

