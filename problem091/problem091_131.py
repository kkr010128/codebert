N = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
#l = list(set(l))
l.sort(reverse=True)
num = 0
for i in range(len(l) - 2):
	for j in range(i + 1, len(l) - 1):
		if l[i] == l[j]:
			continue

		for k in range(j + 1, len(l)):
			if l[j] == l[k]:
				continue

			if l[i] < (l[j] + l[k]):
				num += 1

print(num)
