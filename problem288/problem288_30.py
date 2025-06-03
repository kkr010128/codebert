import math
import sys
N = int(input())
x = math.ceil(math.sqrt(N))
for i in range(x, 0, -1):
    if N % i == 0:
        print(int(i+N/i-2))
        sys.exit()
