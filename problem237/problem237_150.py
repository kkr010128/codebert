n = int(raw_input())
intervals = [[u-l,u+l] for u,l in [map(int, raw_input().split()) for _ in range(n)] ]
intervals.sort(key = lambda x:x[1])

count = 1
i = 1
cur= intervals[0]
while(i < len(intervals)):
	while(i < len(intervals) and cur[1] > intervals[i][0]): i += 1
	if i < len(intervals):
		cur = intervals[i]
		count +=1


print count