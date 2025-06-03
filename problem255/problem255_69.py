N=int(input())
S,T=input().split()
list=[]
i=0
while i<N:
  list.append(S[i])
  list.append(T[i])
  i=i+1
print(*list, sep='')