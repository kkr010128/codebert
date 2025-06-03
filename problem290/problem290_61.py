import sys

def input():
    return sys.stdin.readline().rstrip('\n')

##### main

N,K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)
AxF = [A[i]*F[i] for i in range(N)]
AxFmax = max(AxF)

def is_possible(x):
    _sum = 0
    for i in range(N):
        _sum += max(0, A[i] - x//F[i])
    #print(x,_sum,K)
    return _sum <= K

left = 0
right = AxFmax

while(left != right):
    x = (left+right)//2
    if is_possible(x):
        right = x
    else:
        left = x+1
    #print('main', left, right, x)
            
print(left)
