from collections import deque
num = deque()
n = int(input())
for i in range(n):
    com = input().split()
    if com[0] == "deleteFirst":
        num.popleft()
    elif com[0] == "deleteLast":
        num.pop()
    elif com[0] == "insert":
        num.insert(0, com[1])
    elif com[0] == "delete":
        if num.count(com[1]):
            num.remove(com[1])
print(" ".join(num))
