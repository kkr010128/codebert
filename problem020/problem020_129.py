from collections import deque

que = deque()
n = int(input())

for loop in range(n):
    input_command = input()
    
    if input_command == 'deleteFirst':
        que.popleft()
    
    elif input_command == 'deleteLast':
        que.pop()
    
    else:
        command, x = input_command.split()
        
        if command == 'insert':
            que.appendleft(x)
        elif command == 'delete':
            try:
                que.remove(x)
            except:
                pass

print(' '.join(que))
