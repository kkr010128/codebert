N = int(input())
A = list(map(int,input().split()))

A.sort(reverse = True)

ans = A[0]

if N%2 == 0:
    ans += 2*sum(A[1:(N-2)//2+1])
else:
    ans += 2*sum(A[1:(N-2)//2+1])+A[(N-2)//2+1]

print(ans)