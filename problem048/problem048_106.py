S = int(input())
N = list(map(int, input().split(' ')))
N.sort()
sum = 0
for i in range(S):
	sum += N[i]
	
print(N[0], N[-1], sum)