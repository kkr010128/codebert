n, q = map(int, input().split())

processes = [[li[0], int(li[1])] for li in [input().split() for _ in range(n)]]


elapsed_time = 0
while len(processes):
    process = processes.pop(0)
    if process[1] > q:
        process[1] -= q
        processes.append(process)
        elapsed_time += q
    else:
        elapsed_time += process[1]
        print(process[0], elapsed_time)