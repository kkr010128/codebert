from collections import deque
n=int(input())-10
q=deque(range(1,10))
while n>=0:
    a=str(q.popleft())
    a=int(a+a[-1])
    for i in range(a-1,a+2):
        if str(i)[-2]==str(a)[-1]:
            q.append(i)
            n-=1
print(q[n])
#print(q,n)