word, num = input(), 0
while True:
    sentence = input()
    if sentence=="END_OF_TEXT":
        break
    word_list = sentence.lower().replace(".", " ").split()
    for i in word_list:
        if word==i:
            num += 1
print(num)

