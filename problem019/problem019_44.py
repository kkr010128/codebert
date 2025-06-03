n, quantum = list(map(int, input().split()))
queue = []
sumOfTime = 0

for _ in range(n):
    name, time = input().split()
    queue.append([name, int(time)])

while len(queue) > 0:
    name, time = queue.pop(0)
    if time > quantum:
        sumOfTime += quantum
        queue.append([name, time - quantum])
    else:
        sumOfTime += time
        print(name, sumOfTime)

