N = int(input())
A = list(map(int, input().split()))
ans = "APPROVED"

for n in range(N):
    if A[n] % 2 == 1:
        pass
    elif A[n] % 3 == 0:
        pass
    elif A[n] % 5 == 0:
        pass
    else:
        ans = "DENIED"
        break
print(ans)