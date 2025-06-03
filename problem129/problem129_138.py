N = int(input())
A = list(map(int, input().split()))

mina = min(A)
maxa = max(A)
AA = [0]*(maxa-mina+1)

for i in range(N):
    maxj = maxa//A[i]
    for j in range(1,maxj+1):
        AA[j*A[i]-mina]+=1

ans = 0

for i in range(N):
    if AA[A[i]-mina] == 1:
        ans += 1
        
print(ans)