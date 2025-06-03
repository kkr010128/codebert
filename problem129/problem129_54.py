n = int(input())
A = list(map(int, input().split()))
A.sort()
freq = [0] * (10**6+1)
for a in A:
    freq[a] += 1
m = A[-1]
ans = n
for i in range(n):
    a = A[i]
    if freq[a] > 1:
        ans -= freq[a]
        freq[a] = 0
    for j in range(2 * a, m+1, a):
        if freq[j] > 0 and j % a == 0:
            ans -= freq[j]
            freq[j] = 0
print (ans)
