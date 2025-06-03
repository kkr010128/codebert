s = input()
t = input()

def f(k):
    c = 0
    for i in range(len(t)):
        if s[k + i] == t[i]:
            c += 1
    return c

maxi = f(0)
for i in range(len(s) - len(t) + 1):
    if f(i) > maxi:
        maxi = f(i)

print(len(t) - maxi)