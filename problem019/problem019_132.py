def robin(process, q):
    if int(process[0][1]) - q > 0:
        process[0][1] = int(process[0][1]) - q
        process.append([process[0][0],process[0][1]])
        process.pop(0)
        return process, q
    else:
        q = int(process[0][1])
        process.pop(0)
        return process, q


n, q = input().split()
n, q = int(n), int(q)
process = []
for i in range(n):
    process.append([i for i in input().split()])


time = 0
while len(process) != 0:
    length = len(process)
    name = process[0][0]
    process, process_time = robin(process, q)
    time += process_time
    if length > len(process):
        print(name,time)