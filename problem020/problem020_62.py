from sys import stdin
from collections import deque
input = stdin.readline

# 自作dequeでは実行時間的に通らないので...

n = int(input())
d: deque = deque([])

for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        x = int(command[1])
        d.appendleft(x)

    elif command[0] == "delete":
        x = int(command[1])
        if d.count(x):
            d.remove(x)

    elif command[0] == "deleteFirst":
        tmp = d.popleft()

    elif command[0] == "deleteLast":
        tmp = d.pop()

while d:
    tmp = d.popleft()

    if d:
        print(tmp, end=" ")
    else:
        print(tmp)

