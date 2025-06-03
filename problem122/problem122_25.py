#template
def inputlist(): return [int(j) for j in input().split()]
#template
from collections import Counter
N = int(input())
A = inputlist()
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i] = inputlist()
A_sum = sum(A)
dic = Counter(A)
for i in range(Q):
    A_sum += (C[i]-B[i])*dic[B[i]]
    print(A_sum)
    dic[C[i]] += dic[B[i]]
    dic[B[i]] = 0