from collections import deque

N = int(input())
L = deque()

for i in range(N):
    C= input().split()

    if C[0] == "insert":
        L.appendleft(C[1])

    elif C[0] == "delete":
        try:
            L.remove(C[1])
        except ValueError:
                pass
    elif C[0] == "deleteFirst":
        L.popleft()
    elif C[0] == "deleteLast":
        L.pop()
    
print(" ".join(L))

