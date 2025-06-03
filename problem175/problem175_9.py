#162D
#RGB Triplets

import collections

n=int(input())
S=input()
s=collections.Counter(S)
ans=s['R']*s['G']*s['B']
for i in range(n):
    for d in range(n):
        j=i+d
        k=j+d
        if k>n-1:
            break
        if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
            ans-=1
print(ans)