n=int(input())
N=10**4+20;M=103
a=[0 for _ in range(N)]
for x in range(1,M):
    for y in range(1,M):
        for z in range(1,M):
            res=x*x+y*y+z*z+x*y+y*z+z*x;
            if res<N:a[res]+=1
for i in range(n):
    print(a[i+1])