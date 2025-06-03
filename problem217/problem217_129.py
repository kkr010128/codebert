N = int(input())

A = list(map(int, input().split())) 

ans = 'APPROVED'

for i in range(0,N):
    if (A[i]%2)==0:
        if not ((A[i] % 3) == 0 or (A[i] % 5) == 0):
            ans = 'DENIED'
            break

print(ans)