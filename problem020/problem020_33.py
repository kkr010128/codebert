from sys import stdin

class DList:
    class Cell:
        def __init__(self, k):
            self.key  = k
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = DList.Cell(None)
        self.last = DList.Cell(None)
        self.head.next = self.last
        self.last.prev = self.head

    def insert(self, x):
        c = DList.Cell(x)
        c.prev = self.head
        c.next = self.head.next
        c.next.prev = c
        self.head.next = c

    def delete(self, x):
        c = self.__find(x)
        if c != None:
            self.__delete(c)

    def __delete(self, c):
        c.prev.next = c.next
        c.next.prev = c.prev

    def __find(self, x):
        c = self.head.next
        while c != None and c.key != x:
            c = c.next
        return c

    def deleteFirst(self):
        self.__delete(self.head.next)
    def deleteLast(self):
        self.__delete(self.last.prev)

    def __iter__(self):
        self.it = self.head.next
        return self
    def __next__(self):
        if self.it == self.last:
            raise StopIteration
        k = self.it.key
        self.it = self.it.next
        return k

dlist = DList()

n = int(stdin.readline())
for i in range(n):
    cmd = stdin.readline()
    if   cmd.startswith('insert'):
        dlist.insert(cmd[7:-1])
    elif cmd.startswith('deleteFirst'):
        dlist.deleteFirst()
    elif cmd.startswith('deleteLast'):
        dlist.deleteLast()
    elif cmd.startswith('delete'):
        dlist.delete(cmd[7:-1])

print(' '.join(dlist))

