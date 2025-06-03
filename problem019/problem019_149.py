class Queue:
    queue_list = []
    def enqueue(self, a):
        self.queue_list.append(a)
    def dequeue(self):
        return self.queue_list.pop(0)
    def isEmpty(self):
        return len(self.queue_list) == 0

n, q = list(map(lambda x: int(x), input().strip().split()))

queue = Queue()

for i in range(n):
    queue.enqueue(input().strip().split())


sum_time = 0
while not queue.isEmpty():
    name, time = queue.dequeue()
    if int(time) <= q:
        sum_time += int(time)
        print(name + ' ' + str(sum_time))
    else:
        queue.enqueue([name, str(int(time) - q)])
        sum_time += q

