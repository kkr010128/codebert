import sys
from collections import deque

d = deque()
n = int(input())
lines = sys.stdin.readlines()
for i in range(n):
    ins = lines[i].split()
    command = ins[0]
    if command == "insert":
        d.appendleft(ins[1])
    elif command == "delete":
        try:
            d.remove(ins[1])
        except:
            pass
    elif command == "deleteFirst":
        d.popleft()
    elif command == "deleteLast":
        d.pop()

print(" ".join(d))