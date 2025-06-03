n = int(input())
table = [0]*(10**5)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            table[x**2+y**2+z**2+x*y+y*z+z*x] += 1

for i in range(1, n+1):
    print(table[i])