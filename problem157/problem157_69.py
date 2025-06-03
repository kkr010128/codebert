from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A1 = []
A2 = []

for i in range(1,N+1):
   A1.append(i + A[i-1])
   A2.append(i - A[i-1])
  
c1 = Counter(A1)
c2 = Counter(A2)

result = 0
for k in set(c1).intersection(c2):
    result += c1[k] * c2[k]
print(result)