sentence = input("")
words = sentence.split(" ")
word_amount = len(words)
ae_count = 0

for word in words:
    if "ae" in word:
        ae_count += 1

if ae_count/word_amount < 0.4:
    print("haer talar vi rikssvenska")

else:
    print("dae ae ju traeligt va")