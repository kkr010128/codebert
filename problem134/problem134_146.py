N = int(input())
A = input().split()

ans = 1
zero_count = A.count("0")

if zero_count != 0:
    print(0)
else:
    for i in range(N):
        ans *= int(A[i])
        if ans > 10**18:
            ans = -1
            break

    print(ans)