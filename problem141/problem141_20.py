N = int(input())
A = list(map(int, input().split()))
V = [0]*(N+1)
flug = 0
Lsum= sum(A)
 
V[0] = 1
for i in range(N):
    V[i+1] = (V[i]*2 - A[i+1])
    if V[i+1] < 0 :
        flug = 1
    Lsum = Lsum - A[i+1]
    if V[i+1] > Lsum :
        V[i+1] = Lsum
 
ans = sum(V)+sum(A)
if A[0] != 0 or A[N] == 0:
    ans = -1
if flug == 1:
   ans = -1
if N == 0 and A[0] != 1:
    ans = -1
elif N == 0 and A[0] == 1:
    ans = 1
 
print(ans)