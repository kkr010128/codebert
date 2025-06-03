n = int(raw_input())
a = map(int, raw_input().split())

a_ = sorted(a)
sum = 0

for e in a_:
	sum += e

print "%d %d %d" %(a_[0], a_[-1], sum)