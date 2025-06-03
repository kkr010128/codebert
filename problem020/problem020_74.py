from collections import deque

q = deque()

for i in range(int(input())):
  command_line = input().split(" ")
  command = command_line[0]
  arg = ""
  if len(command_line) > 1: arg = command_line[1]

  if command == "insert":
    q.appendleft(arg)
  elif command == "delete":
    try:
      q.remove(arg)
    except ValueError:
      pass
  elif command == "deleteFirst":
    q.popleft()
  else:
    q.pop()

print(" ".join(q))