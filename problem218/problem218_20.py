n = int(input())
d = {}
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
m = max(d.values())
for s in sorted(s for s in d if d[s] == m):
    print(s)
