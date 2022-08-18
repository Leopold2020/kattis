kattis = input()

X, Y, N = kattis.split(" ")


for nummer in range(1, int(N)+1):

    if nummer % int(X) == 0 and nummer % int(Y) == 0:
        print("FizzBuzz")

    elif nummer % int(X) == 0:
        print("Fizz")

    elif nummer % int(Y) == 0:
        print("Buzz")
    
    else:
        print(nummer)