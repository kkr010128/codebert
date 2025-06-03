n = input()
x =map(int,raw_input().split())
y =map(int,raw_input().split())
sum_1,sum_2,sum_3  = [0,0,0]
sum_end = []
for i in range(n):
	if x[i] > y[i]:
		sum_1 += x[i]-y[i]
		sum_2 += (x[i]-y[i])**2
		sum_3 += (x[i]-y[i])**3
		sum_end.append(x[i]-y[i])
	else :
		sum_1 += y[i]-x[i]
		sum_2 += (y[i]-x[i])**2
		sum_3 += (y[i]-x[i])**3
		sum_end.append(y[i]-x[i])
print(sum_1)
print(pow(sum_2,0.5))
print(pow(sum_3,1.0/3.0))
sum_end.sort()
print(sum_end[len(sum_end)-1])