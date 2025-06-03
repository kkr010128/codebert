from collections import deque
import sys

n = int(input())
deq = deque()

for _ in range(n):
    cmd = input()
    if cmd[0] == "i":
        deq.appendleft(cmd[7:])
    elif cmd[6] == "F":
        deq.popleft()
    elif cmd[6] == "L":
        deq.pop()
    else:
        try:
            deq.remove(cmd[7:])
        except:
            pass

print(" ".join(deq))
