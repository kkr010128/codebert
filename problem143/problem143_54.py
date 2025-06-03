k, s = open(0).read().split(maxsplit=2)
k = int(k)
if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")