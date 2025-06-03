from collections import deque

DLL = deque()

n = int(input())

for i in range(n):
    Line = input().split()
    
    if Line[0] == "insert":
        DLL.appendleft(Line[1])
        
    elif Line[0] == "delete":
        try:
            DLL.remove(Line[1])
        except ValueError:
            None
    elif Line[0] == "deleteFirst":
        DLL.popleft()
    elif Line[0] == "deleteLast":
        DLL.pop()

print(" ".join(DLL))
