from collections import Counter
N = int(input())
A = [int(i) for i in input().split()]
maxA = max(A)
dp = {}
for each in A:
    dp[each] = True
for i in range(N):
    if dp[A[i]]:
        tmp = 2 * A[i]
        while maxA >= tmp:
            if tmp in dp and dp[tmp]:
                dp[tmp] = False
            tmp += A[i]
counter = 0
t = Counter(A)
for i in range(N):
    if dp[A[i]] and t[A[i]] == 1:
        counter += 1
print(counter)