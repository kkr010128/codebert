import sys

N,K = map(int,input().split())
array = [ a for a in range(1,N+1) ]

for I in range(K):
    _ = input()
    sweets = list(map(int,input().split()))
    for K in sweets:
        if K in array:
            array.remove(K)
print(len(array))