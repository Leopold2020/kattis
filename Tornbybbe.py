

last_thing = 0
towers = 0

amount = input("")
number = input("")

number_list = number.split(" ")


for i in number_list:

    if int(i) > int(last_thing):
       towers += 1
    

    last_thing = i

print(towers)