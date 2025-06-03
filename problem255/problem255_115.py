a=int(input())
b,c=list(input().split())
ans=[]
for i in range(a):
    ans.append(b[i])
    ans.append(c[i])
sinans="".join(ans)
print(sinans)