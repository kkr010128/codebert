from collections import deque
x = deque()

for i in range(int(input())):
    com = input()
    if com == "deleteFirst":
        x.popleft()
    elif com == "deleteLast":
        x.pop()
    else:
        com,n = com.split()
        if com == "insert":
            x.appendleft(n)
        elif com == "delete":
            try:
                x.remove(n)
            except:
                pass
            
print(*x)
