import numpy as np
import sys

K = int(input())
A, B = list(map(int, input().split()))

array = np.arange(A, B+1)

for _ in array:
    if(_%K == 0):
        print("OK")
        sys.exit(0)

print("NG")