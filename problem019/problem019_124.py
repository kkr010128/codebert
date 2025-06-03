class Node:
    def __init__(self,v):
        self.v = v
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,v):
        self.size += 1
        n = Node(v)
        if self.tail == None:
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        if self.head == None:
            self.head = self.tail
    def dequeue(self):
        if self.size == 0:
            print 'underflow'
            exit()
        self.size -= 1
        v = self.head.v
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return v

#class Queue:
#    def __init__(self,l):
#        self.values = []
#        self.l = l
#        for _ in range(l):
#            self.values.append(None)
#        self.head = 0
#        self.tail = 0
#    def inc(self,n):
#        if n+1 >= self.l:
#            return 0
#        else:
#            return n+1
#    def enqueue(self,v):
#        if self.inc(self.head) == self.tail:
#            print 'overflow'
#            exit()
#        self.values[self.head] = v
#        self.head = self.inc(self.head)
#    def dequeue(self):
#        if self.head == self.tail:
#            print 'underflow'
#            exit()
#        v = self.values[self.tail]
#        self.tail = self.inc(self.tail)
#        return v
#    def size(self):
#        if self.head >= self.tail:
#            return self.head-self.tail
#        else:
#            self.head + (self.l-self.tail)

n,q = map(int,raw_input().split(' '))
queue = Queue()
for _ in range(n):
    n,t = raw_input().split(' ')
    t = int(t)
    queue.enqueue((n,t))

c = 0
while queue.size>0:
    n,t = queue.dequeue()
    if t <= q:
        c += t
        print n,c
    else:
        queue.enqueue((n,t-q))
        c += q