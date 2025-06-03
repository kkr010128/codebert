#alds13c
from collections import deque
class DoubleLinkyList:
    def __init__(self):
        self.lst=[]
    def insert(self,x):
        self.lst.insert(0,x)
    def delete_x(self,x):
        if x in self.lst:
            self.lst.pop(self.lst.index(x))
    def deleteFirst(self):
        self.lst.pop(0)
    def deleteLast(self):
        self.lst.pop(-1)
        
n = int(input())
dll = deque()

for i in range(n):
    A = input().split(" ")
    if A[0] == "insert":
        dll.appendleft((A[1]))
        #continue
    if A[0] == "delete" and A[1] in dll:
        dll.remove((A[1]))
    if A[0]=="deleteFirst":
        dll.popleft()
    if A[0]=="deleteLast":
        dll.pop()

result = list(dll)
print(" ".join(result))
#print(dll)
