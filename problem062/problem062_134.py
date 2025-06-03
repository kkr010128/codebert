import sys
from functools import reduce
for line in sys.stdin:
    if int(line) == 0:
        break
    s = reduce(lambda a,b: int(a)+int(b), line.strip())
    print(s)