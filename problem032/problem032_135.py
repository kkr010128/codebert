n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
i = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
for _ in range(n):
    if x[i] > y[i]:
        p1 = (x[i] - y[i]) + p1
    else:
        p1 = (y[i] - x[i]) + p1
    i = i + 1
print('{:.8f}'.format(p1))

i = 0
for _ in range(n):
    p2 = ((x[i] - y[i]))**2 + p2
    i = i + 1
print('{:.8f}'.format(p2**(1/2)))

i = 0
for _ in range(n):
    if x[i] > y[i]:
        p3 = ((x[i] - y[i]))**3 + p3
    else:
        p3 = ((y[i] - x[i]))**3 + p3
    i = i + 1
print('{:.8f}'.format(p3**(1/3)))

i = 0
M = 0
for _ in range(n):
    if x[i] > y[i]:
        p4 = x[i] - y[i]
        if M < p4:
            M = p4
    else:
        p4 = y[i] - x[i]
        if M < p4:
            M = p4
    i = i + 1
print('{:.8f}'.format(M))
