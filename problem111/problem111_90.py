N = int(input())
A = list(map(int,input().split()))

A.sort(reverse = True)
ans = A[0]
j = 1
for i in range(2,N):
    ans += A[j]
    if i % 2 == 1:
        j += 1

print(ans)