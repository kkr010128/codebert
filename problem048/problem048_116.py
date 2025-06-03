n = int(raw_input())
list_ = map(int, raw_input().split())
sum = 0
for x in list_:
	sum += x
print min(list_), max(list_), sum