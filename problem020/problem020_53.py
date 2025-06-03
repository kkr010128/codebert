from collections import deque
n=int(input())
commands=[input().split() for i in range(n)]
    
List=deque()
for list_command in commands:
    if 'insert' in list_command:
        List.appendleft(list_command[1])
    elif 'delete' in list_command:
        try:
            List.remove(list_command[1])
        except:
            pass
    elif 'deleteFirst' in list_command:
        List.popleft()
    elif 'deleteLast' in list_command:
        List.pop()
  
print(*List)