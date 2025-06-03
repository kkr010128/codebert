num=int(input())
num2=[10, 9 ,8]



def multi(x):
	y=x**num
	return y


a, b, c=map(multi, num2)
print((a-2*b+c)%(int(1e9+7)))