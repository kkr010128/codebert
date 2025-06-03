n=int(input())
ans=[0 for i in range(10**5)]
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            tmp=x*x+y*y+z*z+x*y+y*z+z*x
            ans[tmp]+=1
for i in range(1,n+1):
    print(ans[i])