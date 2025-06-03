N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())


ans = 0
commands = [''] * N
for i, t in enumerate(T):
    if t == 'r':
        command = 'p'
        point = P

    elif t == 's':
        command = 'r'
        point = R

    elif t == 'p':
        command = 's'
        point = S

    if (i - K >= 0) and (commands[i -  K] == command):
        command = ''
        point = 0

    ans += point
    commands[i] = command

print(ans)