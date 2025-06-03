N = int(input())
dic = {}
ans = 0
A = list(map(int, input().split()))
for i in range(N):
    dic[i] = 0

for i in range(N):
    b = A[i]+N-i-1
    if A[i] < N-i:
        a = N-i-A[i]-1
        dic[a] += 1
    if b < N:
        ans += dic[b]
print(ans)