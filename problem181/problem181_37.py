from collections import deque
k = int(input())
count = 0
que = deque([1,2,3,4,5,6,7,8,9])
while que:
    q = que.popleft()
    count +=1
    if count == k:
        print(q)
        exit()
    tmp = q%10
    if tmp == 0:
        for i in range(0,2):
            nq = q*10+i
            que.append(nq)
    elif tmp == 9:
        for i in range(8,10):
            nq = q*10+i
            que.append(nq)
    else:
        for i in range(tmp-1, tmp+2):
            nq = q * 10 + i
            que.append(nq)