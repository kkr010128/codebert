# coding: utf-8
from collections import deque
n, quantum = [int(i) for i in input().split()]
dq = deque()
for i in range(n):
    p, time = [str(i) for i in input().split()]
    dq.append([p, int(time)])
time = 0
while(len(dq) != 0):
    #引き算処理
    #処理が終了しない場合
    if dq[0][1] > quantum:
        dq[0][1] -= quantum
        dq.rotate(-1)
        time += quantum
    #処理が終了する場合
    else:
        time += dq[0][1]
        print("{} {}".format(dq[0][0], time))
        dq.popleft()