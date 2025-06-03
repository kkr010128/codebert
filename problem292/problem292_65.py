# ABC143
# B Tkoyaki Festival 2019
n = int(input())
D = list(map(int, input().split()))
ct = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if i < j:
                ct += D[i] * D[j]
print(ct)
