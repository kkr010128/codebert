s=input()
sr=s[::-1]
cntl=0
cntr=0
ll=[0]
rl=[0]

for i in range(len(s)):
    if s[i]=="<":
        cntl+=1
    else:
        cntl=0
    
    if sr[i]==">":
        cntr+=1
    else:
        cntr=0
    ll.append(cntl)
    rl.append(cntr)
    
rrl=rl[::-1]
ans=[]
for i in range(len(s)+1):
    ans.append(max(rrl[i],ll[i]))

print(sum(ans))