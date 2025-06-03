N=int(input())
sum=[0]*N
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            a=x*x+y*y+z*z+x*y+y*z+x*z
            if a<=N:
                sum[a-1]=sum[a-1]+1

for i in sum:
    print(i)