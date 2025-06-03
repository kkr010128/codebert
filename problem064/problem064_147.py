#coding: utf-8

s = input()
p = input()

for i in range(len(s)):
    s = s[1:] + s[0:1]
    if s.find(p) != -1:
        print("Yes")
        exit()

print("No")

