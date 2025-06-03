N = int(input())
S = []
for _ in range(N):
    S.append(input())

import sys
from collections import Counter

count_dict = Counter(S)
most_freq = count_dict.most_common(1)[0][1]

words = []

for word, freq in sorted(count_dict.items(), key=lambda x: -x[1]):
    if freq == most_freq:
        words.append(word)

for word in sorted(words):
    print(word)
