from collections import deque

n = int(input())
dll = deque()
for i in range(n):
    command = input().split()
    if command[0] == 'insert':
        dll.appendleft(command[1])
    elif command[0] == 'delete':
        try:
            dll.remove(command[1])
        except:
            pass
    elif command[0] == 'deleteFirst':
        dll.popleft()
    else:
        dll.pop()
print(*dll)