#-------------------- fast io --------------------
import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin

ns = lambda: stdin.readline().strip()
na = lambda: list(map(int, stdin.readline().split()))
ni = lambda: int(ns())

m = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
n = ni()
for i in range(n):
    m[ns()] += 1

print(f"AC x {m['AC']}")
print(f"WA x {m['WA']}")
print(f"TLE x {m['TLE']}")
print(f"RE x {m['RE']}")
