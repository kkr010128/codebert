#coding: UTF-8

word = input().upper()
cnt = 0

while True:
    sentence = list(map(str, input().split()))
    if 'END_OF_TEXT' in sentence:
        break
    for i in range(len(sentence)):
        if word == sentence[i].upper():
            cnt += 1

print(cnt)
