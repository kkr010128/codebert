#!/usr/bin/env python

contents = []
counter = 0

word = input()

while True:
    text = input()
    if text == "END_OF_TEXT":
        break
    textWords = text.split()
    contents.append(textWords)

for x in contents:
    for y in x:
        if y.lower() == word:
            counter += 1

print(counter)