# coding: UTF-8
from collections import deque

dll = deque()

n = int(input())
for _ in range(n):
  raw = input().split()
  command = raw[0]
  if command == 'delete': 
    value = raw[1]
    try:
      dll.remove(value)
    except ValueError as err:
      continue
  elif command == 'insert':
    value = raw[1]
    dll.appendleft(value)
  elif command == 'deleteFirst':
    try:
      dll.popleft()
    except IndexError as err:
      continue
  elif command == 'deleteLast':
    try:
      dll.pop()
    except IndexError as err:
      continue

print(" ".join(dll))
