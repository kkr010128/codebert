class Queue:
    queue_list = []
    start = 0
    def enqueue(self, a):
        self.queue_list.append(a)
    def dequeue(self):
        assert self.start != len(self.queue_list), "オーバーフローが発生しました。"
        self.start += 1
        return self.queue_list[self.start - 1]
    def isEmpty(self):
        return self.start == len(self.queue_list)

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
