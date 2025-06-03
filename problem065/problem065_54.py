#coding:utf-8
#1_9_A 2015.4.12
w = input().lower()
c = 0
while True:
    t = input()
    if 'END_OF_TEXT' in t:
        break
    c += t.lower().split().count(w)
print(c)