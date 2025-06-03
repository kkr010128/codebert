import sys
from collections import deque

N = int(sys.stdin.readline())
A = [int(i) for i in sys.stdin.readline().split(' ')]

A.sort(reverse=True)
max_value = A.pop(0)
diff = deque([max_value])
ans = 0
for i in A:
    ans = ans + diff.popleft()
    diff.append(i)
    diff.append(i)

print(ans)