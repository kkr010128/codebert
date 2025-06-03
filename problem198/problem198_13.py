n=int(input())
l=["a","b","c","d","e","f","g","h","i","j"]
a="a"
ans=["a"]
for i in range(1,n):
    tt=[]
    for j in ans:
        s=len(set(j))
        for k in range(s+1):
            tt.append(j+l[k])
    ans=tt
ans.sort()
for i in ans:
    print(i)