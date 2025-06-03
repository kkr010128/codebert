n=int(input())
a,b=list(input().split())
ans=[]
for i in range(2*n):
    if i%2==0:
        ans.append(a[i//2])
    else:
        ans.append(b[i//2])
ansl=""
for i in ans:
    ansl+=i
print(ansl)