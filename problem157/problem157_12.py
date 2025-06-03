n=int(input())
a=map(int,input().split())
pulasu_i=dict()
mainasu_i=dict()
for i,num in enumerate(a):
    x=i+1
    if num+x not in pulasu_i:
        pulasu_i[num+x]=1
    else:
        pulasu_i[num+x]+=1
    if num-x not in mainasu_i:
        mainasu_i[num-x]=1
    else:
        mainasu_i[num-x]+=1
#print(pulasu_i,mainasu_i)
ans=0
for num,cnt in pulasu_i.items():
    if -num not in mainasu_i:
        continue
    else:
        ans+=cnt*mainasu_i[-num]
print(ans) 