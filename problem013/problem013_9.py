n = int(raw_input())
r = []
for i in range(n):
    r.append(int(raw_input()))

min_v = r[0]
max_profit = -1000000000000
for i in range(1,n):
    if max_profit < r[i] - min_v:
        max_profit = r[i]-min_v
    if r[i] < min_v:
        min_v = r[i]

print max_profit