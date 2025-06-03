N=int(input())
alp=["a","b","c","d","e","f","g","h","i","j"]
alp=alp[:N]
ans=[]
def dfs(now):
    
    if len(now)==N:
        ans.append(now)
        return
    for i,s in enumerate(alp):
        if len(set(now))>=i:
            next_s=now+s
            dfs(next_s)
dfs("a")
ans=sorted(ans)
for a in ans:
    print(a)
