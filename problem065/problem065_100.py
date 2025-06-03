#coding: utf-8


w = input()
w = w.upper()
s = []
c = 0
while True:
    i = input()
    if i == "END_OF_TEXT":
        break
    s.append(i.upper())

for i in s:
    for j in i.split(" "):
        if j == w:
            c += 1

print(c)
