N=int(input())

f=[0]*(N+1)

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            temp=x**2+y**2+z**2+x*y+y*z+z*x
            if temp<=N:
                f[temp]+=1

for i in range(1,N+1):
    print(f[i])
