class process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def queue(q, ps):
    time = 0
    while len(ps) != 0:
        p = ps.pop(0)
        if p.time > q:
            p.time -= q
            time += q
            ps.append(p)
        else:
            time += p.time
            print p.name + " " + str(time)

if __name__ == "__main__":
    L = map(int, raw_input().split())
    N = L[0]
    q = L[1]
    processes = []
    for i in range(N):
        L = raw_input().split()
        processes.append(process(L[0], int(L[1])))
    queue(q, processes)