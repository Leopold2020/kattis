correct_word = input("")
guess = input("")

wrong = 0
right = 0

correct_len = len(correct_word)


for i in guess:

    if correct_word.count(i) > 0:
        right += correct_word.count(i)

    else:
        wrong += 1

    #print(right, wrong)
    if right == correct_len:
        print("WIN")
        break

    if wrong == 10:
        print("LOSE")
        break   
