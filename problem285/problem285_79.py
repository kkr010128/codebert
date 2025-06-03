s = input()
l, count = [], 0
for i in s:
    if i=='>': count+=1
    else:
        if count: l.append(count)
        count = 0
if count: l.append(count); count = 0
j = 0
ans = []
if s[0]=='<': ans.append(0)
else:
    ans.append(l[0])
    l[0]-=1

for i in range(len(s)):
    if s[i]=='<': ans.append(ans[-1]+1)
    else:
        if i==0: ans.append(ans[-1]-1); continue
        if l[j]==0: j+=1
        if ans[-1]>=l[j]:
            l[j]-=1
            ans.append(l[j])
                
        else:
            ans[-1]=l[j]
            l[j]-=1
            ans.append(l[j])
print(sum(ans))
