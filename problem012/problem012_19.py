import math
def prime_array(n=1000):
	List = [2]
	i = 3
	while i <= n:
		judge = True
		for k in List :
			if math.sqrt(i) < k :
				break
			if i%k == 0:
				judge = False
				break
		if judge :
			List.append(i)
		i += 2
	return List
def main():
	cnt=0
	prime_List=prime_array(10**4)
	n=input()
	for i in range(n):
		a=input()
		if a<=10**4:
			for j in prime_List:
				if a==j:
					cnt+=1
					break
		else:
			judge=True
			for j in prime_List:
				if a%j==0:
					judge=False
					break
			if judge:
				cnt+=1
	print('%d' % cnt)
if __name__=='__main__':
	main()