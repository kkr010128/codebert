n = int(input())

import math

N = math.ceil(math.sqrt(n))
from collections import defaultdict
counter = defaultdict(int)

from collections import defaultdict
counter = defaultdict(int)

for x in range(1,N + 1):
    answer_x = x * x
    for y in range(x, N + 1):
        answer_y = answer_x + y * y + x * y
        if answer_y > n:
            continue
        for z in range(y, N + 1):
            answer_z = answer_y + z * z + x * z + y * z
            if answer_z <= n:
                if x == y and x == z:
                    counter[answer_z] += 1
                elif x == y or x == z or y == z:
                    counter[answer_z] += 3
                else:
                    counter[answer_z] += 6

for i in range(1,n+1):
  print(counter[i])

