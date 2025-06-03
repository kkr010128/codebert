# coding: utf-8
# Here your code !
import collections
s=int(input())
deq =collections.deque()

for i in range(s):
    n=input().split()
    if n[0]=="insert":
        deq.appendleft(n[1])
    elif n[0]=="delete":
        try:
            deq.remove(n[1])
        except ValueError:
            pass
    elif n[0]=="deleteFirst":
        deq.popleft()
    elif n[0]=="deleteLast":
        deq.pop()
        
print(" ".join(list(deq)))