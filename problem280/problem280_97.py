import itertools

n = int(input())
lis = []
for i in range(n):
    x, y = map(int, input().split())
    lis.append((x, y))

LIS = [i for i in range(n)]

big_lis = list(itertools.permutations(LIS))
L = len(big_lis)


def sai(i, j):
    return (lis[A[i + 1]][j] - lis[A[i]][j]) ** 2


keep = 0
ANS = 0
for i in range(L):
    A = list(big_lis[i])
    keep = 0
    for j in range(n - 1):
        keep += (sai(j, 0) + sai(j, 1)) ** (1 / 2)
    ANS += keep
print(ANS / L)
