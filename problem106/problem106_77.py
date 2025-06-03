n = int(input())
l = [0]*10000

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            ind = x**2+y**2+z**2+x*y+y*z+z*x
            if ind <= 10000:
                l[ind-1]+=1

for i in range(n):
    print(l[i])