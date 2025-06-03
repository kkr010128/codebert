import math

while True:
	cnt = int(input())
	if cnt == 0:
		break
	
	li = list(map(int, input().split()))

	ave = sum(li) / cnt
	n_var = 0.0
	
	for i in range(cnt):
		n_var += ( li[i] - ave )**2
	
	var = n_var / cnt
	
	print('{0:.8f}'.format(math.sqrt(var)))