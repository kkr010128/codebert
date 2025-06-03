n = int(input())
A = [int(x) for x in input().split()]
q = int(input())
M = [int(x) for x in input().split()]

ans = ["no"]*2000

for i in range(1<<n):
    a = 0
    for j in range(n):
        if (i>>j)&1 == 1:
            a += A[j]
    ans[a] = "yes"

for j in M:
    print(ans[j])
