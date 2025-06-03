
A, B = map(int, input().split())

lb_a = int(-(-A // 0.08))
ub_a = int(-(-(A + 1) // 0.08) - 1)

lb_b = int(-(-B // 0.1))
ub_b = int(-(-(B + 1) // 0.1) - 1)

if ub_b < lb_a or ub_a < lb_b:
    print(-1)
else:
    print(max(lb_a, lb_b))
