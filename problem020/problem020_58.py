# ALDS1_3_C: Doubly Linked List
# collections.deque
# https://docs.python.org/3.8/library/collections.html#collections.deque

#n = 7
#A = [('insert', 5), ('insert', 2), ('insert', 3), ('insert', 1), 
#     ('delete', 3), ('insert', 6), ('delete', 5),]
from collections import deque

n = int(input())
mylist = deque()
for i in range(n):
    myinput = input().split()
    if len(myinput) == 1:
        order = myinput[0]
        x = 0
    else:
        order, x = myinput

    #print(order, x)
    if order == 'insert': 
        mylist.appendleft(x)
    elif order == 'delete':
        try:
            mylist.remove(x)
        except:
            pass
    elif order == 'deleteFirst':
        #mylist.remove(mylist[0])
        mylist.popleft()
    elif order == 'deleteLast':
        mylist.pop()
    #print(mylist)
print(" ".join(map(str, mylist)))
