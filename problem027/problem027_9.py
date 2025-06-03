def koch(n, p1, p2):
    if n == 0:
        return

    s_x = p1[0] * 2/3 + p2[0] * 1/3
    s_y = p1[1] * 2/3 + p2[1] * 1/3

    t_x = p1[0] * 1/3 + p2[0] * 2/3
    t_y = p1[1] * 1/3 + p2[1] * 2/3

    u_x = (t_x - s_x) * 1/2 - (t_y - s_y) * 3 ** 0.5 / 2 + s_x
    u_y = (t_x - s_x) * 3 ** 0.5 / 2 + (t_y - s_y) / 2 + s_y

    s, t, u = (s_x, s_y), (t_x, t_y), (u_x, u_y)
    
    koch(n - 1, p1, s)
    print(' '.join(str(i) for i in s))
    koch(n - 1, s, u)
    print(' '.join(str(i) for i in u))
    koch(n - 1, u, t)
    print(' '.join(str(i) for i in t))
    koch(n - 1, t, p2)
    
    
S, G = (0, 0), (100, 0)
print(' '.join(str(i) for i in S))
koch(int(input()), S, G)
print(' '.join(str(i) for i in G))

