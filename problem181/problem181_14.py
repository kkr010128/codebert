from collections import deque
K = int(input())
d = deque([1,2,3,4,5,6,7,8,9])
count = 0
while True:
    tag = d.popleft()
    tmp1 = tag % 10
    tmp2 = tmp1 + tag * 10
    if tmp1 == 9:
        d.append(tmp2 - 1)
        d.append(tmp2)
    elif tmp1 == 0:
        d.append(tmp2)
        d.append(tmp2 + 1)
    else:
        d.append(tmp2 - 1)
        d.append(tmp2)
        d.append(tmp2 + 1)
    count += 1
    if count == K:
        print(tag)
        break

