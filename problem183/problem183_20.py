from math import sqrt
from math import ceil
from math import floor

def divisors(n):
	count=0
	lis=[]
	for i in range(1,ceil(sqrt(n))+1):
		if n%i==0:
			if n//i==i:
				count+=1
				lis.append(i)
			else:
				lis.append(i)
				lis.append(n//i)
				count+=2
	lis=set(lis)
	lis.remove(1)
	return lis

def main():
	n=int(input())
	ol=n-1
	ans=0
	case1div=divisors(ol)
	case2div=divisors(n)
	for i in case2div:
		newn=n
		if newn%i==0:
			while newn%i==0:
				newn//=i
		if newn%i==1:
			ans+=1
	ans+=len(case1div)
	print(ans)
main()