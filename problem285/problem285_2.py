s=input()
sl=len(s)

l=[0 for i in range(sl+1)]
for i in range(sl):
    if s[i]=='<':
        l[i+1]=max(l[i]+1, l[i+1])

for i in reversed(range(sl)): # reversed(range(sl))
    if s[i]=='>':
        l[i]=max(l[i+1]+1, l[i])

print(sum(l))