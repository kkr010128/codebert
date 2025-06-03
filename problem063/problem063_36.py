#!/usr/bin/env python

letters = []
for i in range(26):
    letters.append(chr(i + 97) + " : ")

contents = []
while True:
    try:
        text = input()
    except EOFError:
        break
    contents.append(text)


#65-90 uppercase
#97-122lowercase
i = 0
for y in letters:
    value = 0
    for text in contents:
        for x in text:
            if x.isupper():
                x = x.lower()
                if x in y:
                    value += 1
            elif x.islower():
                if x in y:
                    value += 1
    letters[i] = letters[i] + str(value)
    i += 1

for x in letters:
    print(x)