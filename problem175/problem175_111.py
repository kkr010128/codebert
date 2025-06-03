import collections
n=int(input())
S=input()
c=collections.Counter(S)
ans=c['R']*c['B']*c['G']
hiku=0
for i in range(n):
    for d in range(n):
        j=i+d
        k=j+d
        if k>n-1:
            break
        if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
          hiku+=1
print(ans-hiku)