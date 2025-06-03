
N = int(input())
myans = [ 0 for n in range(N+1)]
upper = int(N**(2/3))
#print(upper)
for x in range(1, 105):
    for y in range(1, 105):
        for z in range(1, 105):
            v = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if v < N+1:
                myans[v] += 1
#print(myans)
for a,b in enumerate(myans):
    if a != 0:
        print(b)
