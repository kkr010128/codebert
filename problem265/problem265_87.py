import math
import sys
n = int(input())
found = False

if(n <= 12):
    print(n)
    sys.exit()

for y in range(n):
    if n == math.floor(y*1.08):
        print(y)
        found = True
        break
if (found == False):
    print(":(")
