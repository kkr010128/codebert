n = int(input())
ans = [0 for _ in range(n+1)]
for x in range(1,int(n**0.5)+1):
    for y in range(1,x+1):
        for z in range(1,y+1):
            if x**2+y**2+z**2+x*y+y*z+z*x<=n:
                if x==y==z:
                    ans[x**2+y**2+z**2+x*y+y*z+z*x] += 1
                if (x==y and y != z) or (y==z and z !=x) or (z==x and x != y):
                    ans[x**2+y**2+z**2+x*y+y*z+z*x] += 3
                if (x!=y) and (y!=z) and (z!=x):
                    ans[x**2+y**2+z**2+x*y+y*z+z*x] += 6
for a in ans[1:]:
    print(a)