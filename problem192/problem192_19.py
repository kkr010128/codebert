from collections import Counter

N = int(input())
A = list(map(int, input().split()))


kosu = Counter(A)

tempSum = 0
for v in kosu.values():
    tempSum += v * (v - 1) // 2



for a in A:
    print(tempSum - kosu[a]+1)


