n = input()
a = list(map(int, raw_input().split(" ")))
print("%d %d %d" % (min(a), max(a), sum(a)))