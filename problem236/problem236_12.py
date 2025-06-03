h = int(input())
w = int(input())
n = int(input())

if n % max(h, w) == 0:
	print(n // max(h,w))
elif n % max(h,w) !=0 :
	print(n // max(h, w) + 1)