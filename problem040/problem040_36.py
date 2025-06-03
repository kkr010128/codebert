def max(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c

def min(a,b,c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    else:
        return c

def mid(a,b,c):
    if (b-a)*(c-a) <= 0:
        return a
    if (a - b) * (c - b) <= 0:
        return b
    else:
        return c


s = input()
s = s.split()
n = []

for i in s:
    n.append(int(i))

a = n[0]
b = n[1]
c = n[2]

print(min(a,b,c),mid(a,b,c),max(a,b,c))
