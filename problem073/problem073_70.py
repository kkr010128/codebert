n = int(input())

s = 0
a = 1
b = 1
while a*b < n:
    while a*b < n and b <= a:
        if a == b:
            s += 1
        else:
            s += 2
        b += 1
    a += 1
    b = 1
print(s)
