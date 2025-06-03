import collections
K = int(input())

if K < 10:
    print(K)
    exit()

q = collections.deque()
for i in range(1, 10):
    q.append(i)
i = 9
while True:
    x = q.popleft()
    lsk = x % 10
    shifted = x * 10
    if lsk != 0:
        q.append(shifted + lsk - 1)
        i += 1
        if i == K:
            print(shifted + lsk - 1)
            break
    q.append(shifted + lsk)
    i += 1
    if i == K:
        print(shifted + lsk)
        break
    if lsk != 9:
        q.append(shifted + lsk + 1)
        i += 1
        if i == K:
            print(shifted + lsk + 1)
            break
