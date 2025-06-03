from collections import deque

n = int(input())
q = deque(["a"])

# 最後に最新の文字数のセットだけ拾う
for i in range(n - 1):
    next_q = deque()
    for curr in q:
        suffix = ord(max(curr)) + 1
        for x in range(ord("a"), suffix + 1):
            next_q.append(curr + chr(x))
    q = next_q

print(*q, sep="\n")