class Queue:
    def __init__(self, limit):
        self.Q = [None]*limit
        self.head = 0
        self.tail = 0
        self.limit = limit

    def initialize(self):
        self.head = 0
        self.tail = 0

    def enqueue(self,x):
        self.Q[self.tail] = x
        self.tail = (self.tail+1) % self.limit

    def dequeue(self):
        if self.isEmpty():
            print('error')
        else:
            self.head = (self.head+1) % self.limit
            return self.Q[self.head-1]

    def isEmpty(self):
        return self.head == self.tail

if __name__ == '__main__':

    n,q = map(int, input().split(' '))

    Q = Queue(n+10)

    for i in range(n):
        name, time = input().split(' ')
        time = int(time)
        Q.enqueue([name,time])

    c = 0

    while Q.head != Q.tail:
        proc = Q.dequeue()
        if proc[1]-q > 0:
            Q.enqueue([proc[0],proc[1]-q])
            c += q
        else:
            c += proc[1]
            print(proc[0],c)