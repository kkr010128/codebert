N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
for i in range(N-1):
    if i == 0:
        ans += A[i]
    else:
        ans += A[1+(i-1)//2]
print(ans)