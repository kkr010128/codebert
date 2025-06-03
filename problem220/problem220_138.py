st = input().split()
ab = map(int, input().split())
rb = input()

di = dict(zip(st, ab))
di[rb] -= 1
print(*list(di.values()))