n = int(input())
a = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    a[i] = int(input())
    t = [[int(j) for j in input().split()] for k in range(a[i])]
    x[i] = [j[0] for j in t]
    y[i] = [j[1] for j in t]

mx = 0
for bit in range(1<<n):
    flag = True
    tf = [0] * n
    for i in range(n):
        if bit & (1 << i): 
            tf[i] = 1
    for i in range(n):
        if tf[i] == 0:
            continue
        for j in range(a[i]):
            if tf[x[i][j]-1] != y[i][j]:
                flag = False
    if flag: mx = max(mx, bin(bit).count("1"))
print(mx)