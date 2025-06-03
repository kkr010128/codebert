n=int(input())
Ans=[0]*n
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            num=x**2+y**2+z**2+x*y+y*z+z*x
            if num<=n:
                Ans[num-1]+=1
print(*Ans,sep='\n')