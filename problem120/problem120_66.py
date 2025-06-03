N = list(map(int,input().split()))
L = list(map(int,input().split()))
a = 0
L.sort()
for i in range(N[1]):
  a += L[i]
print(a)