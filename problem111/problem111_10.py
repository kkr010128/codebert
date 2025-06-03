N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = A[0]
N -= 2
for i in range(1, N):
    if N >= 2:
        ans += A[i]*2
        N -= 2
    elif N  == 1:
        ans += A[i]
        N -= 1
    else:
        break
print(ans)



