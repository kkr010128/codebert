class Proc:
    def __init__(self, name, time):
        self.name = name
        self.time = time

n, q = map(int, input().split(' '))
procs = []

for i in range(0, n):
    name, time = input().split(' ')
    time = int(time)
    procs.append(Proc(name, time))

elapsed = 0
while len(procs) > 0:
    proc = procs.pop(0)
    if proc.time > q:
        proc.time -= q
        elapsed += q
        procs.append(proc)
    else:
        elapsed += proc.time
        print(proc.name, elapsed)