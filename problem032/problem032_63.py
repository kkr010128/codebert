import math
n = int(input())
x = [int(i) for i in input().split()]
y = [int(j) for j in input().split()]
p_1 = p_2 = p_3 = p_m = 0

for i in range(n):
	diff = math.fabs(x[i]-y[i])
	p_1 += diff
	p_2 += diff*diff
	p_3 += diff*diff*diff
	if p_m < diff:
		p_m = diff
	
p_2 = math.sqrt(p_2) 
p_3 = math.pow(p_3, 1/3)

print('%.5f\n%.5f\n%.5f\n%.5f'% (p_1, p_2, p_3, p_m))