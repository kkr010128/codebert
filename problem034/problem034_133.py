def roll(inst):
    global u, s, e, w, n, d
    if inst == 'N':
        u, s, n, d = s, d, u, n
    elif inst == 'E':
        u, e, w, d = w, u, d, e
    elif inst == 'S':
        u, s, n, d = n, u, d, s
    elif inst == 'W':
        u, e, w, d = e, d, u, w

u, s, e, w, n, d = map(int, input().split())
q = int(input())
for i in range(q):
    u1, s1 = map(int, input().split())
    if u1 == u:
        pass
    elif u1 == s:
        roll('N')
    elif u1 == e:
        roll('W')
    elif u1 == w:
        roll('E')
    elif u1 == n:
        roll('S')
    elif u1 == d:
        roll('N')
        roll('N')
    if s1 == s:
        print(e)
    elif s1 == e:
        print(n)
    elif s1 == n:
        print(w)
    elif s1 == w:
        print(s)