import sys
input = sys.stdin.buffer.readline
import numpy as np

D = int(input())
c = np.array(input().split(), dtype=np.int32)
s = np.array([input().split() for _ in range(D)], dtype=np.int32)
last = np.zeros(26, dtype=np.int32)


ans = []
point = 0
for i in range(D):
    down = (i+1-last)*c
    loss = down * 3 + s[i,:]
    idx = np.argmax(loss)
    ans.append(idx+1)
    point += s[i, idx] - down.sum()
    last[idx] = i+1


for i in range(D):
    print(ans[i])