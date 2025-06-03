from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
l = deque()

for _ in range(n):
    op = input().strip().split()
    if op[0] == "insert":
        l.appendleft(op[1])
    elif op[0] == "delete":
        if op[1] in l:
            l.remove(op[1])
    elif op[0] == "deleteFirst":
        l.popleft()
    elif op[0] == "deleteLast":
        l.pop()
print(" ".join(l))

