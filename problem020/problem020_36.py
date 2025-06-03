from collections import deque
n = int(input())
my_list = deque()
for t in range(n):
    i = input().split()
    if i[0] == "insert":
        my_list.appendleft(i[1])
    elif i[0] == "delete" and i[1] in my_list:
        my_list.remove(i[1])
    elif i[0] == "deleteFirst":
        my_list.popleft()
    elif i[0] == "deleteLast":
        my_list.pop()
print(" ".join(my_list))

