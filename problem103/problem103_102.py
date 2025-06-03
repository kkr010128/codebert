N = int(input())

A = list(map(int,input().split()))
chk = []

for i in range(N-1):
    if A[i+1] > A[i]:
        chk.append(1)
    else:
        chk.append(0)

ans = 1000 
for i in range(N-1):
    if chk[i] == 1:
        ans += (A[i+1] - A[i]) * (ans//A[i])
print(ans)