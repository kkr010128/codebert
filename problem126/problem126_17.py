import math
a = list(map(int, input().strip().split()))

for i in a:
    if a[i] == 0:
        o = i
        break
    else:
        pass

print(o+1)