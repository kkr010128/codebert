def roll(i):
    global u, s, e, w, n, d
    if i == 'N':
        u, s, n, d = s, d, u, n
    elif i == 'E':
        u, e, w, d = w, u, d, e
    elif i == 'S':
        u, s, n, d = n, u, d, s
    elif i == 'W':
        u, e, w, d = e, d, u, w

u, s, e, w, n, d = input().split()
q = int(input())
for i in range(q):
    u1, s1 = input().split()
    if u1 == s:
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