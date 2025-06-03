N=int(input())
A=[int(x) for x in input().split()]
Q=int(input())
somme=sum(A)

from collections import Counter
D=Counter()

for l in A:
    D[l]+=1
    
for step in range(Q):
    b,c=map(int,input().split())

    if b not in D:
        print(somme)
        continue

    somme=somme+(c-b)*D[b]

    D[c]=D[c]+D[b]
    del D[b]    
    print(somme)