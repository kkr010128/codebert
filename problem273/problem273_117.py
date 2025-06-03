import numpy as np
from queue import Queue
n,k = map(int,input().split())
A = [a-1 for a in list(map(int,input().split()))]
A = np.cumsum(+np.array([0]+A))%k

dic = {}
ans = 0
Q = Queue()
for a in A:
    Q.put(a)
    if a in dic:
        ans += dic[a]
        dic[a] += 1
    else:
        dic[a] = 1
    if Q.qsize() == k:
        q = Q.get()
        dic[q] -= 1
    # print(dic)
print(ans)