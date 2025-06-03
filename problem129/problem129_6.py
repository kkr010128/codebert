N = int(input())
A = list(map(int,input().split()))
ma = max(A)
l = [0 for _ in range(ma + 10)]
for i in range(N):
    temp = A[i]
    while(temp <= ma + 5):
        l[temp] += 1
        temp += A[i]
ans = 0
for i in range(N):
    if l[A[i]] == 1:  ans += 1
print(ans)