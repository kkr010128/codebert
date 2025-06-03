class Queue:
    def __init__(self, n):
        self.values = [None]*n
        self.n = n
        self.s = 0
        self.t = 0

    def next(self, p):
        ret = p+1
        if ret >= self.n:
            ret = 0
        return ret

    def enqueue(self, x):
        if self.next(self.s) == self.t:
            raise Exception("Overflow")
        self.values[self.s] = x
        self.s = self.next(self.s)

    def dequeue(self):
        if self.s == self.t:
            raise Exception("Underflow")
        ret = self.values[self.t]
        self.t = self.next(self.t)
        return ret

n, q = map(int, raw_input().split(' '))
queue = Queue(n+1)
for _ in range(n):
    name, time = raw_input().split(' ')
    time = int(time)
    queue.enqueue((name, time))

completed = []
cur = 0
while len(completed) < n:
    name, time = queue.dequeue()
    res = time-q
    if res <= 0:
        cur += time
        completed.append((name, cur))
    else:
        cur += q
        queue.enqueue((name, res))

for name, time in completed:
    print name, time