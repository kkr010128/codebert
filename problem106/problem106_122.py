N=int(input())
ans=[0]*(N+1)
for x in range(1,101):  
    for y in range(1,101):
        for z in range(1,101):
            fn=x**2+y**2+z**2+x*y+y*z+z*x
            if fn>N:
                break
            else:
                ans[fn]=ans[fn]+1
for n in range(1,N+1):
    print(ans[n])