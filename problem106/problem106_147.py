f = [0  for i in range(0, 10001)]
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if n <= 10000:
                f[n] += 1 
N = int(input())
for n in range(1, N+1):
    print(f[n])