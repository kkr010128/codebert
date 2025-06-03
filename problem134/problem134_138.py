N = int(input())
A = sorted(list(map(int,input().split())))
ans = A[0]
if ans == 0:
    print(ans)
    exit()
else:
    for i in range(1,N):
        ans = ans * A[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)