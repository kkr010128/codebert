from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
data = Counter(s)
print(len(data.keys()))