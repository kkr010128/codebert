n = int(input())
A = [0]
A.extend(list(map(int,input().split())))
B = {}
pair = 0

for i in range(1,n+1):
  if i+A[i] in B:
    B[i+A[i]] += 1
  else:
    B[i+A[i]] = 1
  
for j in range(2,n+1):
  if j-A[j] in B:
    pair += B[j-A[j]]

print(pair)