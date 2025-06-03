# coding=utf-8
from collections import deque
n = int(input())
deque = deque()
input_lines = [input().split() for x in range(n)]

for i in range(n):
    inp = input_lines[i]
    if inp[0] == 'deleteFirst':
        deque.popleft()
    elif inp[0] == 'deleteLast':
        deque.pop()
    elif inp[0] == 'insert':
        deque.appendleft(inp[1])
    else:
        if inp[1] in deque:
            deque.remove(inp[1])

print(*deque)