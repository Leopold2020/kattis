E_BULB = 60
E_LED = 11
LIFE_BULB = 1000
LIFE_LED = 8000
PRICE_BULB = 5
PRICE_LED = 60

h_p = input().split(" ")
h = int(h_p[0])
p = int(h_p[1])

k_bulb = PRICE_BULB
k_led = PRICE_LED
life_bulb = LIFE_BULB
life_led = LIFE_LED
days = 1

while k_led > k_bulb:
    life_bulb += h
    life_led += h

    if life_bulb > LIFE_BULB:
        life_bulb = life_bulb % LIFE_BULB
        k_bulb += PRICE_BULB

    if life_led > LIFE_LED:
        life_led = life_led % LIFE_LED
        k_led += PRICE_LED
    
    k_bulb += (E_BULB*h*p)/100_000
    k_led += (E_LED*h*p)/100_000

    days += 1

print(days)