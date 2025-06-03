N = int(input())
l = [0]*N
upper = round((N-1)**0.5-1)
for x in range(1, upper+1):
    for y in range(1, upper + 1):
        for z in range(1, upper + 1):
            tmp = x**2+y**2+z**2+x*y+y*z+z*x
            if tmp < N+1:
                l[tmp-1]+=1
for x in l:
    print(x)