N = int(input())
L = [0]*10001
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            if x**2 + y**2 + z**2 + x*y + y*z +z*x <= 10000:
                L[x**2 + y**2 + z**2 + x*y + y*z +z*x] += 1
for k in range(1,N+1):
    print(L[k])
