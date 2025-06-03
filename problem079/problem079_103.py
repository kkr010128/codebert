S = int(input())
if S == 1:
    print(0)
    exit()
MOD = 10**9 + 7
A = [0] * (S + 1)
A[0] = 1
A[1] = 0
A[2] = 0

cumsum = 1
for i in range(3, len(A)):
    A[i] = (A[i - 1] + A[i - 3]) % MOD
print(A[-1])
