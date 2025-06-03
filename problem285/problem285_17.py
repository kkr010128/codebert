from itertools import groupby
S=input()
T=groupby(S)
s=0
total=0
keys=[]
groups=[]
for key,group in T:
    keys.append(key)
    groups.append(len(list(group)))

if keys[0]==">":
    total+=sum([i for i in range(groups[0]+1)])
if keys[-1]=="<":
    total+=sum([i for i in range(groups[-1]+1)])
for i in range(len(keys)-1):
    if keys[i]=="<":
        if groups[i]<=groups[i+1]:
            total+=sum([j for j in range(groups[i])])
            total+=sum([j for j in range(groups[i+1]+1)])
        else:
            total+=sum([k for k in range(groups[i]+1)])
            total+=sum([k for k in range(groups[i+1])])
print(total)