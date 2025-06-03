n=int(input())
a,b=[],[]
for i in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
a.sort()
b.sort(reverse=True)
ans=0
if n%2==1:
    s=a[n//2]
    g=b[n//2]
    ans=g-s+1
else:
    s1,s2=a[n//2-1],a[n//2]
    g2,g1=b[n//2-1],b[n//2]
    ans=(g2+g1)-(s2+s1)+1
print(ans)