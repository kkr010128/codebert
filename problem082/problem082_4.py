s = input()
t = input()
a = len(s) - len(t) + 1
c1= 0

for i in range(a):
    c2 = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            c2 += 1
        else:
            continue
    c1 = max(c1,c2)


print(len(t)-c1)
