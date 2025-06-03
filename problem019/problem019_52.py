import queue

n, quantum = map(int, input().split())
q = queue.Queue()
for _ in range(n):
    name, time = input().split()
    q.put([name, int(time)])

spend_time = 0
while q.qsize() > 0:
    name, time = q.get()
    tmp = min(quantum, time)
    spend_time += tmp
    time -= tmp
    if time == 0:
        print('{} {}'.format(name, spend_time))
    else:
        q.put([name, time])

