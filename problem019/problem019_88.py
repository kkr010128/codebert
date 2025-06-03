n, q = [int(i) for i in input().split()]
process = []
for i in range(n):
    name, time = input().split()
    process.append([name, int(time)])

count = 0
while True:
    if len(process) == 0: break
    if process[0][1] <= q:
        count += process[0][1]
        print(process[0][0], count)
        process[0][1] = process[0][1] - q
        process.pop(0)
    else:
        count += q
        process[0][1] = process[0][1] - q
        process.append(process.pop(0))