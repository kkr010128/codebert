from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for key in A:
    d[key] += 1
    #print(d)

Sum = 0
for i in d:
    n = d[i]
    Sum += (n * (n - 1)) // 2
    #print((n * (n - 1)) // 2)
    #print(d[A[i]],i)
    #print(d)

#print(Sum)

for i in range(N):
    n = d[A[i]]
    hoge = Sum - (n*(n-1))//2
    n -= 1
    hoge += (n*(n-1))//2
    print(hoge)