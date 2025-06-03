a, b, c, k = (int(i) for i in input().split())

re = k
na = min(a, re)
re -= na
nb = min(b, re)
re -= nb
nc = min(c, re)

print(na - nc)
