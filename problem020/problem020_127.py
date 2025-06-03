from collections import deque
n =  int(input())

mylist = deque()


for i in range(n):
    a = input()
    if a == "deleteFirst":
        mylist.popleft()
    elif a == "deleteLast":
        mylist.pop()
    else:
        a,key = a.split()
        if a == "insert":
            mylist.appendleft(key)
        else:
            try:
                mylist.remove(key)
            except:
                pass

print(' '.join(mylist))

