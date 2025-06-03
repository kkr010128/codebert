import numpy as np

n = int(input())
a =  [x for x in range(1,10)]

for i in a:
    for j in a:
        if i * j == n:
            print('Yes')
            exit()
print('No')
