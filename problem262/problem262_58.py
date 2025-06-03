
N = int(input())
X = []
Y = []
for _ in range(N):
    a = int(input())
    tmp = []
    for _ in range(a):
        tmp.append(list(map(int, input().split())))

    X.append(a)
    Y.append(tmp)

ans = 0
for bit in range(2 ** N):
    flag = True
    for i in range(N):
        if bit >> i & 1:
            for x, y in Y[i]:
                flag &= (bit >> (x - 1) & 1) == y

    if flag:
        ans = max(ans, bin(bit).count("1"))

print(ans)
