import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline()[:-1].split(" ")
    if commands[0] == "insert":
        queue.appendleft(commands[1])
    elif commands[0] == "delete":
        try:
            queue.remove(commands[1])
        except ValueError:
            pass
    elif commands[0] == "deleteFirst":
        queue.popleft()
    elif commands[0] == "deleteLast":
        queue.pop()

print(" ".join(queue))