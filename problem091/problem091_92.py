n = int(input())
arr = list(map(int, input().split()))
res = 0
for ii, i in enumerate(arr):
    for jj, j in enumerate(arr):
        for kk, k in enumerate(arr):
            if ii < jj < kk and i != j and j != k and k != i:
                if i + j > k and j + k > i and k + i > j:
                    res += 1
print(res)                    