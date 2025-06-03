from collections import deque
K = int(input())
que = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(K):
    num = que.popleft()
    if i == K-1:
        print(num)
        break
    if num%10 == 0:
        que.append(num*10 + num%10)
        que.append(num*10 + num%10 + 1)
    elif num%10 == 9:
        que.append(num*10 + num%10 - 1)
        que.append(num*10 + num%10)
    else:
        que.append(num*10 + num%10 - 1)
        que.append(num*10 + num%10)
        que.append(num*10 + num%10 + 1)
