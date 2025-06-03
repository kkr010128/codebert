n = input()
line = raw_input().split()
val = [int(line[i]) for i in range(n)]
print '%d %d %d' % (min(val), max(val), sum(val))