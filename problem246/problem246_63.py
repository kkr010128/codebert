from collections import deque

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

dic = []
que = deque()
for i in range(1, N+1):
    que.append([i])

while que:
    seq = que.popleft()
    if len(seq) == N:
        dic.append(seq)
        continue
    else:
        for i in range(1, N+1):
            if i in seq:
                continue
            seq_next = seq + [i]
            que.append(seq_next)

for i in range(len(dic)):
    if P == dic[i]:
        a = i
    if Q == dic[i]:
        b = i
print(abs(a-b))