from collections import Counter
n = int(input())
A = list(map(int, input().split()))        
C = lambda x: x*(x-1)//2
s = 0
D = Counter(A)
for i,j in D.items():
  s += C(j)
for i in A:
  print(s-D[i]+1)