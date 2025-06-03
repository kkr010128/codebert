n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

journey = [1]

for i in range(n):
    journey.append(a[journey[i]])

if k <= n:
    print(journey[k])
    exit()

cycle_end = n
cycle_start = n - 1

while journey[cycle_start] != journey[cycle_end]:
    cycle_start -= 1

cycle_range = cycle_end - cycle_start

cycle_cnt = (k - n) // cycle_range
extra = (k - n) - (cycle_range * cycle_cnt)

for i in range(extra):
    journey.append(a[journey[i + n]])    

print(journey[-1])