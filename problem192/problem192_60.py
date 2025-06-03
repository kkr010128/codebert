from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt_A = Counter(A)
ans = sum([k * (k - 1) // 2 for k in cnt_A.values()])

for i in range(N):
    print(ans - (cnt_A[A[i]] - 1))
