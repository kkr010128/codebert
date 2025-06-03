from __future__ import division, print_function
from sys import stdin
word = stdin.readline().rstrip().lower()
cnt = 0
for line in stdin:
    if line.startswith('END_OF_TEXT'):
        break
    cnt += line.lower().split().count(word)
print(cnt)