import math

N=int(input())
ARR=[0]*(N+1)

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            res=x**2+y**2+z**2+x*y+y*z+z*x
            if res<=N:
                ARR[res]+=1

for i in ARR[1:]:
    print(i)