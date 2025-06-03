n = int(input())

table = [0]*(10**4+100)

for x in range(1,105):
    for y in range(1,105):
        for z in range(1,105):
            total = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if total < 10100:
                table[total] += 1
            
for i in range(n):
    print(table[i+1])