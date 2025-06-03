N = int(input())
A = list(map(int, input().split()))
f = 0

if 0 in A:
    print("0")
    f = 1
else:

    ans = A[0]
    for i in range(1, N):
        ans = ans * A[i]
        if ans > 10**18:
            print("-1")
            f = 1
            break

if f == 0:
    print(ans)