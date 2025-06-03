from collections import deque


def run_process(processes, slot):
    """Simulate the round-robin scheduler.
    Returns a list of (process, elapsed_time).

    >>> ps = [('p1', 150), ('p2', 80), ('p3', 200), ('p4', 350), ('p5', 20)]
    >>> run_process(ps, 100)
    [('p2', 180), ('p5', 400), ('p1', 450), ('p3', 550), ('p4', 800)]
    """
    ps = deque(processes)
    tot = 0
    finish = []

    while len(ps) > 0:
        p, t = ps.popleft()
        dt = min(t, slot)
        if dt == t:
            finish.append((p, tot+dt))
        else:
            ps.append((p, t-dt))

        tot += dt

    return finish


def run():
    count, slot = [int(i) for i in input().split()]
    ps = []

    for _ in range(count):
        p, t = input().split()
        ps.append((p, int(t)))

    for p, t in run_process(ps, slot):
        print(p, t)


if __name__ == '__main__':
    run()

