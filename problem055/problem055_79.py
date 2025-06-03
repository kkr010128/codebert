from collections import defaultdict
m = defaultdict(int)
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    m[(b, f, r)] += v
for b in range(1, 5):
    for f in range(1, 4):
        for r in range(1, 11):
            print("", m[(b, f, r)], end="")
        print("")
    if b < 4:
        print("####################")

