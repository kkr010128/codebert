
from math import sqrt

while True:
	input_data =[] # ????´??????????
	alpha = 0 # ??????
	num = int(input())
	if num == 0:
		break
	input_data = [float(i) for i in input().split()]
	m = sum(input_data) / float(num)
	for i in range(num):
		alpha += (input_data[i] - m)**2
	print(sqrt(alpha/num))