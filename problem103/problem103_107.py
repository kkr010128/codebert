N = int(input())
a = list(map(int,input().split()))
S = 1000
K = 0
b = 1
last = 0
			
for i in range(N):
	if i != N-1:
		if a[i]<=a[i+1]:
			S += a[i]*K
			K = S // a[i]
			S -= K*a[i]

		else:
			S += a[i]*K
			K = 0
	else:

		S += a[i]*K
print(S)
