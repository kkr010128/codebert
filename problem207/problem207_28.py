A=[]
for i in range(3):
  A.append(list(map(int,input().split())))

N=int(input())
for i in range(N):
  x=int(input())
  for row in A:
    for num in range(len(row)):
      if x==row[num]:
        row[num]=0

for i in A:
  if i==[0,0,0]:
    print("Yes")
    exit(0)
for i in range(3):
  if A[0][i]==0 and A[1][i]==0 and A[2][i]==0:
    print("Yes")
    exit(0)
if A[0][0]==0 and A[1][1]==0 and A[2][2]==0:
    print("Yes")
    exit(0)
if A[2][0]==0 and A[1][1]==0 and A[0][2]==0:
    print("Yes")
    exit(0)
print("No")
