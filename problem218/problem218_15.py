n=int(input())
dic=dict()
for i in range(n):
    s=input()
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
ans=[]
val=max(dic.values())
for kv in dic.items():
    if kv[1]==val:
        ans.append(kv[0])
ans=sorted(ans)
for a in ans:
    print(a)
