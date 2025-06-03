from sys import stdin
from collections import deque

# 入力
n = int(input())

# command = [stdin.readline()[:-1] for a in range(n)]
command = stdin

# process
output = deque([])

for a in command:
    if a[0] == 'i':
        output.appendleft(int(a[7:]))
    elif a[0:7] == 'delete ':
        try:
            output.remove(int(a[7:]))
        except ValueError:
            pass
    elif a[6] == 'F':
        output.popleft()
    else:
        output.pop()

# 出力
print(*list(output))

