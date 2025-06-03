N = int(input())

def calc(n):
    ans = [0 for i in range(n+1)]
    for x in range(1,n+1):
        a = x**2
        if a>=n:
            break
        for y in range(1,1+n):
            b = y**2
            if b>=n:
                break
            for z in range(1,1+n):
                c = z**2
                if c>=n:
                    break
                f = a+b+c+x*y+y*z+z*x
                if f>n:
                    break
                ans[f]+=1
    return ans

res = calc(N)
for i in range(N):
    print(res[i+1])