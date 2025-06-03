from collections import deque
N = int(input())
que = deque(['a'])

while len(que) > 0:
    s = que.popleft()
    if len(s) == N:
        print(s)
    else:
        for i in range(ord(sorted(s)[-1]) - 95):
            que.append(s + chr(97 + i))