number = input("")
list1 = list(number)

while len(list1) != 1:
    product = 1

    for i in list1:
        if i != '0':
            product *= int(i)
    list1 = list(str(product))
    

print(list1[0])