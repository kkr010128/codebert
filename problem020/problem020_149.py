from collections import deque
q=deque()
n=int(input())

for i in range(n):
    cmd=input()
    if cmd=="deleteFirst":
        try:
            q.popleft()
        except:
            pass
        
    elif cmd=="deleteLast":
        try:
            q.pop()
        except:
            pass
        
    else:
        cmd,number=cmd.split()
        if cmd=="delete":
            try:
                q.remove(number)
            except:
                pass
            
        elif cmd=="insert":
            q.appendleft(number)
        
print(*q)
