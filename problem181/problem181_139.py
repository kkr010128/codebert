from _collections import deque
k = int(input())

l = [str(i) for i in range(1,10)]
que = deque(l)


while len(l) < k:
    seq = que.popleft()

    a = int(seq[-1])
    if a != 0:
        aa = seq + str(a-1)
        que.append(aa)
        l.append(aa)
    aa = seq + str(a)
    que.append(aa)
    l.append(aa)
    if a != 9:
        aa = seq + str(a+1)
        que.append(aa)
        l.append(aa)

print(l[k-1])

