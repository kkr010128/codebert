n = int(input())
d = {}
for i in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
m = max(d.values())

ans = [_ for _ in d if d[_] == m]
ans.sort()
[print(_) for _ in ans]
