
n = int(raw_input())
S = []
S = map(int, raw_input().split())

q = int(raw_input())
T = []
T = map(int, raw_input().split())

count = 0

for i in T:
	if i in S:
		count += 1

print count