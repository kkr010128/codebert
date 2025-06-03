N,M = map(int, input().split())

AC = [0] * (N+1)
pl = [0] * (N+1)
cole = 0
pena = 0
for target_list in range(M):
    ans = input().split()
    problem = int(ans[0])
    result = ans[1]

    if AC[problem] == 0 and result == 'WA':
        pl[problem] += 1
    elif AC[problem] == 0 and result == 'AC':
        pena += pl[problem]
        cole += 1
        AC[problem] = 1

print(cole, pena)

