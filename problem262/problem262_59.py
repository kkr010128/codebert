import itertools
n = int(input())

answers = []
for i in range(n):
	a = int(input())
	answers.append((i, []))
	for j in range(a):
		(x, y) = [int(k) for k in input().split()]
		answers[i][1].append((x, y))

lst = []
combi_lst = [i for i in range(n)]
for i in range(n, -1, -1):
	for balls in itertools.combinations(combi_lst, i):
		lst = [True if j in balls else False for j in range(n)]
		success = True
		for i, ans in enumerate(answers):
			if lst[i] == False:
				continue
			for x, y in ans[1]:
				if y == 1 and lst[x - 1] == False:
					success = False
				if y == 0 and lst[x - 1] == True:
					success = False
		if success:
			print(sum(lst))
			exit()