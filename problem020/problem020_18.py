# -*- coding:utf-8 -*-

from collections import deque

result = deque()

def operation(command):
    if command[0] == "insert":
        result.appendleft(command[1])
    elif command[0] == "delete":
        if command[1] in result:
            result.remove(command[1])
    elif command[0] == "deleteFirst":
        result.popleft()
    elif command[0] == "deleteLast":
        result.pop()

n = int(input())
for i in range(n):
    command = input().split()
    operation(command)
print(*result)