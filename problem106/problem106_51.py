n=int(input())
ans = [0] * 100000
for x in range(1,101):
    for y in range(1,101):
        for z  in range(1,101):
            ans[x*x+y*y+z*z+x*y+y*z+z*x]+=1
for i in range(1,n+1):
    print(ans[i])
