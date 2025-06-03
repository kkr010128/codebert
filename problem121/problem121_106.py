from bisect import bisect_right
import string
N=int(input())
L=[0]*13
for i in range(1,13):
    L[i]=(L[i-1]+1)*26
# print(L)

# やるべきことは26進数

def bisectsearch_right(L,a):
    i=bisect_right(L,a)
    return(i)

S=string.ascii_lowercase
l=bisectsearch_right(L,N-1)
s=['']*l
tmp=N-1-L[l-1]
# print(l,tmp)
j=l-1
while j>=0:
    s[j]=S[tmp%26]
    tmp//=26
    j-=1
print(''.join(s))