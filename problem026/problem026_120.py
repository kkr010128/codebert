def m(L,R):
 global c;c+=len(L)+len(R)
 T=[];j=0
 for l in L:
  while j<len(R)and R[j]<l:T+=[R[j]];j+=1
  T+=[l]
 while j<len(R):T+=[R[j]];j+=1
 return T
def d(A):s=len(A)//2;return m(d(A[:s]),d(A[s:])) if len(A)>1 else A
c=0
input()
print(*d(list(map(int,input().split()))))
print(c)
