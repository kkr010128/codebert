N=int(input())
A=0
B=0
C=0
D=0

for i in range(N+1):
  A+=i

for i in range(N+1):
  if i % 3 == 0:
    B+=i
    
for i in range(N+1):
  if i % 5 == 0:
    C+=i
    
for i in range(N+1):
  if i % 15 == 0:
    D+=i
    
print(A-B-C+D)