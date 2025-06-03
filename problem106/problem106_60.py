N = int(input())
l = [0] * 10 ** 5
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n = (pow(x + y,2) + pow(y + z,2) + pow(z + x,2)) // 2
            l[n] += 1
for n in range(1,N + 1):
    print(l[n])