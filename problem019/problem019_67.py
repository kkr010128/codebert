n, q = map(int, input().split())
process = []
for _ in range(n):
    name, time = input().split()
    process.append([name, int(time)])
process.append([])

def reduce(index):
    left_time = process[index][1] - q
    return [process[index][0], left_time]

head = 0
tail = n
quene_len = len(process)
elapsed_time = 0

while head != tail:
    if process[head][1] > q:
        process[tail] = reduce(head)
        elapsed_time += q
        head = (head+1)%quene_len
        tail = (tail+1)%quene_len
    else:
        elapsed_time += process[head][1]
        print(process[head][0], elapsed_time)
        head = (head+1)%quene_len
