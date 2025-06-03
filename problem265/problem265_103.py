import math
a = int(input())
for i in range(50001):
    if math.floor(i*1.08) == a:
        print(i)
        exit()
print(":(")