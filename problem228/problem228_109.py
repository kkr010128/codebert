H = int(input())

import math

def caracal(H):
    if H == 1:
        return 1
    return 2*caracal(math.floor(H/2)) + 1

print(caracal(H))
