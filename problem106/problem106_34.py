n=int(input())
p=round(n**0.5)+1
ans=[0]*n
for x in range(1,p):
    for y in range(1,p):
        for z in range(1,p):
            k=x**2+y**2+z**2+x*y+y*z+z*x
            k-=1
            if 0<=k<=n-1:
                ans[k]+=1
for i in ans:
    print(i)