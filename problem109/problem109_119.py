from collections import Counter
n = int(input())
verdicts = Counter([input() for i in range(n)])
for verdict in ["AC", "WA", "TLE", "RE"]:
    print(f"{verdict} x {verdicts[verdict]}")