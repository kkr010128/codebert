from collections import Counter

N = int(input())
A = list(map(int, input().split()))
max_a = max(A)

A.sort()

count = Counter(A)

divisible = [False] * (max_a + 1)

ans = 0

for a in A:
    if divisible[a]:
        continue
    for i in range(1, max_a // a + 1):
        divisible[i * a] = True
    if count[a] == 1:
        ans += 1
print(ans)


