import sys
N = int(input())
A = list(map(int, input().split()))
a=1
if 0 in A:
    print('0')
    sys.exit()
for i in range(N):    
    a=A[i]*a
    if a>10**18:
        print('-1')
        sys.exit()
print(a)