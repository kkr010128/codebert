import copy

H, W, K = list(map(int, input().split()))
c = [0]*H
for i in range(H):
    char = input()
    c[i] = []
    for j in range(W):
        if char[j] == "#":
            c[i].append(1)
        else:
            c[i].append(0)

count = 0

for i in range(2**H):
    for j in range(2**W):
        d = copy.deepcopy(c)
        i2 = i
        j2 = j
        for k in range(H):
            if i2 & 1:
                d[k] = [0]*W
            i2 >>= 1
        for l in range(W):
            if j2 & 1:
                for m in range(H):
                    d[m][l] = 0
            j2 >>= 1
        s = sum(map(sum, d))
        if s == K:
            count += 1

print(count)