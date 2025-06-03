import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

A,B=list(map(int,input().split()))
C = math.gcd(A,B)

def factorization(n):
    arr = [[1,1]]
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    return arr

Cfac = factorization(C)
print(len(Cfac))
