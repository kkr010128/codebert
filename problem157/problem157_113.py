import collections
cc = collections.Counter()
count = 0
n = raw_input()
for i,e in enumerate(map(int, raw_input().split())):
	count += cc[e - i]
	cc[-e-  i] +=1
print count
