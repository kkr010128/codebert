def power_set(A, s):
	if len(A) == 0:
		return {s}
	else:
		return power_set(A[1:], s) | power_set(A[1:], s+A[0])

def main():
	n = int(input())
	A = input()
	#print(n)
	A = list(map(int, A.split()))
	q = int(input())
	m = input()
	ms = list(map(int, m.split()))
	powerset = power_set(A, 0)
	
	for m in ms:
		if m in powerset:
			print('yes')
		else:
			print('no')

if __name__ == '__main__':
	main()