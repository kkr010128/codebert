from collections import Counter

N = int(input())
s = [input() for _ in range(N)]
c = Counter(s)
print(f'AC x {c["AC"] if c["AC"] else 0}')
print(f'WA x {c["WA"] if c["WA"] else 0}')
print(f'TLE x {c["TLE"] if c["TLE"] else 0}')
print(f'RE x {c["RE"] if c["RE"] else 0}')