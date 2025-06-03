from collections import deque

def pr(a):
    for i in range(len(a)):
        if i == len(a)-1:
            print(a[i])
        else:
            print(a[i],end = " ")

n = int(input())
q = deque()
for i in range(n):
    x = input()
    l = len(x)
    if x[0] == "i":
        q.insert(0,x[7:])
    elif x[6] == " ":
        try:
            q.remove(x[7:])
        except:
            pass
    elif l > 10:
        q.popleft()
    elif l > 6:
        q.pop()

print(*q)
