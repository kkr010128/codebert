import sys 
try:
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
except:
	pass

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr = list(enumerate(arr))
arr.sort(reverse = True, key = lambda x:(x[1]))
dp = [[0 for c in range(n+1)] for r in range(n+1)]
ans = 0
for r in range(n+1):
	st = r-1
	for c in range(n+1-r):
		if r==c==0:
			pass
		elif r-1<0:
			dp[r][c] = dp[r][c-1] + ( arr[st][1] * abs((arr[st][0]+1) - (n+1-c)) )

		elif c-1<0:
			dp[r][c] = dp[r-1][c] + ( arr[st][1] * abs((arr[st][0]+1) - r) )

		else:
			dp[r][c] = max( dp[r-1][c] + ( arr[st][1] * abs((arr[st][0]+1) - r) ), 
						dp[r][c-1] + ( arr[st][1] * abs((arr[st][0]+1) - (n+1-c)) )                           
						)
		ans = max(ans, dp[r][c])
		st += 1
print(ans)