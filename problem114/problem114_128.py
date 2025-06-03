N = 26
D = int(input())

c_list = list(map(int, input().split()))

s_table = []
for _ in range(D):
	s_table.append(list(map(int, input().split())))

data = []
for _ in range(D):
	data.append(int(input()) - 1)

def calc(data):
	last = [-1] * N
	satisfaction = 0
	for i in range(D):
		j = data[i]
		satisfaction += s_table[i][j]
		last[j] = i
		for k in range(N):
			satisfaction -= c_list[k] * (i - last[k])
		print(satisfaction)
	return satisfaction

calc(data)
