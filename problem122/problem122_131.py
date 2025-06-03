from collections import Counter
N = int(input())

A = list(map(int,input().split()))
Q = int(input())

counter = Counter(A)
sum_res = sum(A)
#print(sum_res,counter)
for _ in range(Q):
    bf,af = map(int,input().split())
    sum_res -= bf*counter[bf]
    sum_res += af*counter[bf]
    
    counter[af] += counter[bf]
    counter[bf] = 0
    
    print(sum_res)