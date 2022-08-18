# total = input()

# king, queen, rook, bishop, knight, pawns = total.split(" ")



# if king == 0:
#     print("0")

# elif king > 1:
#     print(king - 1)

# elif king < 1:
#     print()


list = input()

needed = [1, 1, 2, 2, 2, 8]
have   = [int(x) for x in list.split()]

difference = []
for i in range(len(needed)):
    difference.append(needed[i] - have[i])

print(" ".join([str(x) for x in difference]))

# import sys

# inputstd = sys.stdin.read()

# correct = [1, 1, 2, 2, 2, 8]

# line = inputstd.strip("\n")
# values = line.split(" ")

# i = 0
# correction = ""

# for item in values:
# 	item = int(item)
# 	correction += str((correct[i] - item)) + " "
# 	i += 1
	
# print (correction)