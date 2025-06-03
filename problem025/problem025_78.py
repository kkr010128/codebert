from itertools import chain, combinations

def power_set(x):
	return chain.from_iterable(combinations(x, r) for r in range(len(x)+1))

def main():
	n = int(input())
	A = input()
	#print(n)
	A = list(map(int, A.split()))
	q = int(input())
	m = input()
	ms = list(map(int, m.split()))
	powerset = power_set(A)
	sum_set = [sum(s) for s in powerset if len(s)!=0]
	
	for m in ms:
		if m in sum_set:
			print('yes')
		else:
			print('no')

if __name__ == '__main__':
	main()