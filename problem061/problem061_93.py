# coding: utf-8
# Your code here!

n = input()
t = ""
for i in range(len(n)):
    m = str(n[i])
    if (n[i].islower()):
        m = n[i].upper()
    else:
        m = n[i].lower()
    t += m
print(t)
