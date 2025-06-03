N = int(input())
A = [int(x) for x in input().split()]

for i in range(N):
    if A[i] == 0:
        print(0)
        exit()

ans = A[0]
for i in range(1, N):
    ans *= A[i]
    if ans > 10**18:
        print(-1)
        exit()

print(ans)
