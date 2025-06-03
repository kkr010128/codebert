N = int(input())
Z = []
max = 0
for i in range(N):
    A = int(input())
    Z.append([list(map(int, input().split())) for i in range(A)])
for a in range(2 ** N):
    flag = 1
    for i in range(N):
        if (((a >> i) + 1) & 1):
            continue
        z = Z[i]
        for x in z:
            if not (((a >> (x[0] - 1)) + 1 - x[1]) & 1):
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        x = bin(a).count('1')
        if x > max:
            max = x
print(max)