from collections import deque

n=int(input())
que=deque()

for i in range(n):
    command=input()

    if command=="deleteFirst":
        que.popleft()
    elif command=="deleteLast":
        que.pop()
    else:
        command,num=command.split()
        num=int(num)
        if command=="insert":
            que.appendleft(num)
        else:
            if num in que:
                que.remove(num)

print(*que,sep=" ")
