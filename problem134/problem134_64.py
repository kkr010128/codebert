N=int(input())

A=list(map(int,input().split()))
ans=A[0]

if 0 in A:
    print(0)
    exit()

for cnt in range(N-1):
    ans = ans * A[cnt+1]
    if ans > 1000000000000000000:
        break
    elif ans == 0:
        break
if ans > 1000000000000000000:
    print(-1)
else:
    print(ans)