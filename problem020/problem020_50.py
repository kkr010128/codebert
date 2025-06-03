# -*- coding:utf-8 -*-
import collections
n = int(input())
command = [input().split() for i in range(n)]
ans = collections.deque()

for i in range(n):
    if command[i][0] == "insert":
        ans.appendleft(command[i][1])
    elif ans == []:
        continue
    elif command[i][0] == "delete":
        try:
            ans.remove(command[i][1])
        except:
            continue
    elif command[i][0] == "deleteFirst":
        ans.popleft()
    else:
        ans.pop()

print (' '.join(ans))