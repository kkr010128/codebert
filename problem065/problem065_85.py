#coding:utf-8
#1_9_A 2015.4.12
w = input().lower()
c = 0
while True:
    t = input().split()
    if 'END_OF_TEXT' in t:
        break
    for word in t:
        if w == word.lower():
            c += 1
print(c)