n, q = map(int, input().split(' '))
p = []
time = 0
counter = 0
for i in range(n):
    tmp_n, tmp_p = input().split(' ')
    tmp_p = int(tmp_p)
    p.append((tmp_n, tmp_p))

while len(p) > 0:
    task = p.pop(0)
    tmp_p = task[1] - q
    if( tmp_p > 0):
        time += q
        p.append((task[0], tmp_p))
    elif( tmp_p <= 0):
        time += task[1]
        print('{} {}'.format(task[0], time))
