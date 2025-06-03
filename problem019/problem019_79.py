class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        res = self.data.pop(0)
        return res

    def getLength(self):
        return len(self.data)

n, q = map(int, input().split())
time = 0
processes = Queue()

for i in range(n):
    name, cost = input().split()
    processes.enqueue([name, int(cost)])

while processes.getLength() > 0:
    currentProcess = processes.dequeue()
    processName = currentProcess[0]
    processCost = currentProcess[1]

    if processCost <= q:
        time += processCost
        print(' '.join([processName, str(time)]))
        continue

    time += q
    processes.enqueue([processName, processCost - q])