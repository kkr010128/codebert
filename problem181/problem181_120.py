from collections import deque
k=int(input())
que=deque()
for i in range(1,10):
    que.append(i)

for i in range(k):
    x=que.popleft()
    if list(str(x))[-1]=="0":
        que.append(x*10+int(list(str(x))[-1]))
        que.append(x*10+int(list(str(x))[-1])+1)
    elif list(str(x))[-1]=="9":
        que.append(x*10+(int(list(str(x))[-1])-1))
        que.append(x*10+int(list(str(x))[-1]))
    else:
        que.append(x*10+int(list(str(x))[-1])-1)
        que.append(x*10+int(list(str(x))[-1]))
        que.append(x*10+int(list(str(x))[-1])+1)

print(x)