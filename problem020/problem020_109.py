from collections import deque

d=deque()

N=int(input())

for n in range(N):
    a=input()
    if a=="deleteFirst":
        d.popleft()
    elif a=="deleteLast":
        d.pop()
    else:
        a,b=a.split()
        if a=="insert":
            d.appendleft(b)
        elif a=="delete":
            if d.count(b):
                d.remove(b)
                
print(' '.join(list(d)))

