from collections import deque

n = int(input())

answer = deque()
for i in range(n):
    command = input()
    if " " in command:
        command, key = command.split()
    
    if command == "insert":
        answer.appendleft(key)
    elif command == "delete":
        if key in answer:
            answer.remove(key)
    elif command == "deleteFirst":
        answer.popleft()
    elif command == "deleteLast":
        answer.pop()

print(*answer)
