import itertools
n,m,q=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(q)]
a=list(range(1,m+1))
A=[]
for i in itertools.combinations_with_replacement(a,n):
  A.append(list(i))
ans=[0]
for j in range(len(A)):
  AA=A[j]
  count=0
  for i in range(q):
    if AA[array[i][1]-1]-AA[array[i][0]-1]==array[i][2]:
      count+=array[i][3]
    else:
      pass
  ans.append(count)
print(max(ans))