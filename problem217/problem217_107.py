N = int(input())
A = list(map(int, input().split()))
B = [i for i in A if i % 2 == 0]
o = 'APPROVED'
for i in B:
	if i % 3 != 0 and i % 5 != 0:
		o = 'DENIED'
		break
print(o)