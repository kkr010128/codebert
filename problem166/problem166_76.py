s=[int(x) for x in list(input())]
for c in range(len(s)-1,-1,-1):
    if c==len(s)-1:
        continue
    s[c]=(pow(10,len(s)-c-1,2019)*s[c]+s[c+1])%2019
s.append(0)
s.sort()
h=[1]
d=s[0]
for c in range(1,len(s)):
    if s[c]!=d:
        h.append(1)
        d=s[c]
    else:
        h[-1]+=1
k=[(x*(x-1))//2 for x in h]
print(sum(k))