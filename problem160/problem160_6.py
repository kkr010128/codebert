def mi(): return map(int,input().split())
def lmi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()

from itertools import combinations_with_replacement
n,m,q=mi()
ll=[i for i in range(1,m+1)]

input_list=[]
for i in range(q):
  abcd=lmi()
  input_list.append(abcd)

ans=0
la=list(combinations_with_replacement(ll,n))
for i in la:
  suma=0
  #print(i)
  for j in input_list:
    a=j[0]
    b=j[1]
    c=j[2]
    d=j[3]
    if (i[b-1]-i[a-1])==c:
      suma+=d
      #print(suma)
  ans=max(ans,suma)
  
print(ans)