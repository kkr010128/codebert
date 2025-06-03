from collections import deque
lis = deque()
num = int(input())
for _ in range(num):
  command = input().split()
  if command[0]=='deleteFirst':
    lis.popleft()
  elif command[0]=='deleteLast':
    lis.pop()
  elif command[0]=='insert':
    lis.insert(0, command[1])
  elif command[0]=='delete':
    try:
        lis.remove(command[1])
    except:
        pass
print(' '.join(lis))
