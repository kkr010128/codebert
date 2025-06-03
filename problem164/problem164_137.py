a, b, c, d = map(int, input().split())

t_death = a // d + 1 if a % d else a // d
a_death = c // b + 1 if c % b else c // b

if t_death >= a_death:
    print('Yes')
else:
    print('No')