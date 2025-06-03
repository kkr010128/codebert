n=int(input())
A=[0]*(n+1)
for x in range(1,101):
    for y in range(1,101):
        if x**2+y**2+x*y>n :break
        for z in range(1,101):
            qq= x**2+y**2+z**2+x*y+y*z+z*x 
            if qq>n:break
            A[qq]+=1
print(*A[1:],sep="\n")