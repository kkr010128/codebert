N = int(input())
A = list(map(int, input().split()))
LN = max(A) + 1
L = [0 for i in range(LN)]
count = 0
for i in A:
    for j in range(i, LN, i):
        L[j] += 1
for i in A:
    if L[i] == 1:
        count += 1
print(count)