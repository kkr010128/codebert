from collections import deque
n = int(input())
dlist = deque()
for i in range(n):
    code = input().split()
    if code[0] == "insert":
        dlist.insert(0,code[1])
    if code[0] == "delete":
        try:
            dlist.remove(code[1])
        except:
            continue
    if code[0] == "deleteFirst":
        dlist.popleft()
    if code[0] == "deleteLast":
        dlist.pop()
print(*dlist,sep=" ")