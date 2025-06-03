import collections
import sys
S = "".join([line for line in sys.stdin])
count = collections.Counter(S.lower())
for char in "abcdefghijklmnopqrstuvwxyz":
    print("{0:s} : {1:d}".format(char, count[char]))