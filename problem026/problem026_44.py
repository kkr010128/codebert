def m(L,R):
 global c
 T=[];i=j=0
 for _ in L[:-1]+R[:-1]:
  if L[i]<R[j]:T+=[L[i]];i+=1
  else:T+=[R[j]];j+=1
  c+=1
 return T
def d(A):s=len(A)//2;return m(d(A[:s])+[1e9],d(A[s:])+[1e9]) if len(A)>1 else A
c=0
input()
print(*d(list(map(int,input().split()))))
print(c)
