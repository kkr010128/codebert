class Queue():
    def __init__(self):
        self.size = 0
        self.Max = 100000
        self.queue = [None]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size >= self.Max

    def enqueue(self, x):
        if self.isFull():
            print("Queue overflow!")
        else:
            self.queue.append(x)
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue underflow!")
        else:
            self.size -= 1
            return self.queue.pop(1)

p_queue = Queue()
e_time = 0

n, q = map(int, input().split())

for i in range(n):
    process = input().split()
    process[1] = int(process[1])
    p_queue.enqueue(process)

while not p_queue.isEmpty():
    process = p_queue.dequeue()
    if process[1] <= q:
        e_time += process[1]
        print(process[0], e_time)
    else:
        e_time += q
        process[1] -= q
        p_queue.enqueue(process)