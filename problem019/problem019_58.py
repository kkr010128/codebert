class Process:
    def __init__(self, name_time):
        self.name = name_time[0]
        self.time = int(name_time[1])


process_amount, quontam = (int(i) for i in input().split(' '))

processes = [Process(input().split(' ')) for i in range(process_amount)]

i = 0
total_time = 0
while len(processes) != 0:
    process = processes[0]
    if process.time <= quontam:
        total_time += process.time
        print('{} {}'.format(process.name, total_time))
    else:
        total_time += quontam
        process.time -= quontam
        processes.append(process)

    processes.pop(0)

