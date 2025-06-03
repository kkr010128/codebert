N = int(input())
A = list(map(int,input().split()))

Adict = {}

for i in range(N):
    Adict[A[i]] = (i+1)

ans = []
for i in range(1,N+1):
    ans.append(str(Adict[i]))

print(" ".join(ans))