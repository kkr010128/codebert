#template
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
A = inputlist()
A.sort()
ans = 1
if A[0] == 0:
    print(0)
    exit()
for i in range(N):
    ans *= A[i]
    if ans > 10**18:
        print(-1)
        exit()
print(ans)