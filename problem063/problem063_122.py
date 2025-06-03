import sys
txt = sys.stdin.read().lower()
for i in "abcdefghijklmnopqrstuvwxyz":
    print(i,":",txt.count(i))
