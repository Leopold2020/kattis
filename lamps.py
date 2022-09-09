days = 0
lowenergy = 60
lamp = 5
lowenergy_effect = 11
lamp_effect = 60
lowenergy_hours = 0
lamp_hours = 0
hours = 0
electricity_price = 0

initial_input = input("")

hours, electricity_price = initial_input.split(" ")

hours = int(hours)
electricity_price = int(electricity_price)

while lowenergy > lamp:
    days += 1

    lowenergy_hours += hours
    lamp_hours += hours

    if lamp_hours == 1000 or lamp_hours > 1000:
        lamp_hours -= 1000
        lamp += 5
    
    if lowenergy_hours == 8000 or lowenergy_hours > 8000:
        lowenergy_hours -= 8000
        lowenergy += 60

    lowenergy += (lowenergy_effect * hours * electricity_price)/100000

    lamp += (lamp_effect * hours * electricity_price)/100000


print(days)