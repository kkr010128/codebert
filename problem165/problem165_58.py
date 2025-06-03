import sys
from collections import Counter
N = int(input())
S = [str(s) for s in sys.stdin.read().split()]
items = list(dict.fromkeys(S))
print(len(items))