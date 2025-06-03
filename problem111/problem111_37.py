N = int(input())
A = list(map(int,input().split()))

A = sorted(A, reverse = True)

B = [A[0]] + [A[i] for i in range(1,N)] * 2

B = sorted(B, reverse = True)

ans = 0

for i in range(N - 1):
   ans +=  B[i]
print(ans)