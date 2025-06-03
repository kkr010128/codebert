from collections import Counter

n = int(input())
S = [input() for i in range(n)]

counter = Counter(S)
print(len(counter.keys()))