def Queue(l, nowtime, sec):
	if len(l) == 1:
		print(l[0][0], nowtime + l[0][1])
		return [], 0

	else:
		tl = l.pop(0)

		if tl[1] <= sec:
			nowtime += tl[1]
			print(tl[0], nowtime)
			return l, nowtime

		else:
			nowtime += sec
			l.append([tl[0], tl[1] - sec])
			return l, nowtime



if __name__ == '__main__':
	N, sec = input().split()
	N, sec = int(N), int(sec)
	lists = list()

	for i in range(N):
		obj, times = input().split()
		lists.append([obj, int(times)])

	now = 0
	while lists:
		lists, now = Queue(lists, now, sec)
