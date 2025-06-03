import sys

N = int(input())
A = list(map(int, input().split()))
LA = len(A)
ans = A[0]
for j in range(LA):
    if A[j] == 0:
        print('0')
        sys.exit()

for i in range(LA-1):
    ans = ans*A[i+1]
    if ans > 10**18:
        print('-1')
        sys.exit()
        
print(ans)
