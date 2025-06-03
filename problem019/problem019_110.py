n, q = map(int , input().split())
queue = []
for _ in range(n):
    line = input().split()
    queue.append([line[0], int(line[1])])

class my_queue:
    def __init__(self, queue):
        self.queue = queue
    def enqueue(self, item):
        self.queue = self.queue + [item]
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) != 0:
            item = self.queue[0]
            self.queue = self.queue[1:]
        else :
            item = None
        return item


time = 0
finish_task = []

while(len(queue) != 0):
    item = queue.pop(0)
    if item == None:
        break
    elif item[1] <= q:
        time += item[1]
        finish_task.append([item[0], time])
    else :
        time += q
        queue.append([item[0], item[1] - q])

for item in finish_task:
    print(item[0], item[1])