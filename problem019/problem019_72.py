#getting input
statements = []
while True:
    try:
        line = str(input())
    except EOFError:
        break
    statements.append(line)

pair = statements.pop(0).split()
amount = int(pair[0])
quantum = int(pair[1])

#process input
queue = []
for state in statements:
    pair = state.split()
    name = pair[0]
    time = int(pair[1])
    queue.append([name,time])

#processing queue

done_list = list()
time_spend = 0
while True:
    if not len(queue) > 0:
        break
    task = queue[0]


    if task[1] >= quantum: #time left
        time_spend += quantum
        task[1] = task[1] - quantum
    else:
        time_spend += task[1]
        task[1] = 0

    if task[1] <= 0: #finished
        task.append(time_spend)   #name,left_time, finished time
        done_list.append((task[0],task[2])) #name and finished time
        queue.remove(task)
    else:
        temp = task
        queue.remove(task)
        queue.append(temp)

for result in done_list:
    print(result[0],end=' ')
    print(result[1])
