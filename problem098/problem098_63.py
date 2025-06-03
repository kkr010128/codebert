N = int(input())
S = input()
from collections import Counter
d = Counter(list(S))
allr = d["R"]
leftd = Counter(list(S[:allr]))
leftr = leftd["R"]
print(allr-leftr)