A,B=map(int,input().split())
N = list(map(int,input().split()))

c=0

for i in range(A):
  if N[i] >= B:
    c+=1
  else:
    pass
  i+=1
print(c)
