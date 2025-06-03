def odd(num):
	return num//2+num%2

N=int(input())

num = odd(N)/N
print("{:.10f}".format(num))