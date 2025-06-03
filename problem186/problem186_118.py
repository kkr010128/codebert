K,N = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in range(N-1):
  temp = A[i+1]-A[i]
  B.append(temp)
B.append(K-A[-1]+A[0])
B.sort()
#print(B)
ans = K-B[-1]
print(ans)
