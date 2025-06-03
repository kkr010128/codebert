from sys import stdin

n = int(stdin.readline().rstrip())
ai = [int(x) for x in stdin.readline().rstrip().split()]
ai.sort()
print("%d %d %d" % (ai[0], ai[n-1], sum(ai)))
