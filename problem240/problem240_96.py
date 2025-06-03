def abc151c_welcome_to_at_coder():
    n, m = map(int, input().split())
    penalty = [0] * n
    sum_penalty = 0
    ac = [0] * n
    for i in range(m):
        p, s = input().split()
        if ac[int(p) - 1] == 0:
            if s == 'WA':
                penalty[int(p) - 1] += 1
            else:
                ac[int(p) - 1] = 1
                sum_penalty += penalty[int(p) - 1]
    print(sum(ac), sum_penalty)


abc151c_welcome_to_at_coder()