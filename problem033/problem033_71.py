u, s, e, w, n, d = input().split()
insts = input()
for inst in insts:
    if inst == 'N':
        u, s, n, d = s, d, u, n
    elif inst == 'E':
        u, e, w, d = w, u, d, e
    elif inst == 'S':
        u, s, n, d = n, u, d, s
    elif inst == 'W':
        u, e, w, d = e, d, u, w
print(u)