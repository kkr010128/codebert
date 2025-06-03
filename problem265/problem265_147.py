import math
N = int(input())
X = N / 1.08

floor = math.ceil(N/1.08)
ceil = math.ceil((N+1)/1.08)

for i in range(floor,ceil):
    print(i)
    break
else:
    print(":(")