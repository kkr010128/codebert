from collections import deque

process = deque(maxlen=100000)
n, q = [int(x) for x in input().split(' ')]

for i in range(n):
    name, time = input().split(' ')
    process.append([name, int(time)])

total_time = 0

while process:
    p_q = process.popleft()
    if p_q[1] > q:
        total_time += q
        p_q[1] -= q
        process.append(p_q)
    else:
        total_time += p_q[1]
        print('{} {}'.format(p_q[0], total_time))