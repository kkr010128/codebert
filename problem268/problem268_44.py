import sys
input = sys.stdin.readline

mod = 1000000007
N = int(input())
AA = list(map(int, input().split()))

num = [0,0,0]
ans = 1
for i in AA:
	f = False
	cnt = 0
	for j in range(3):
		if(num[j] == i):
			if f==False : 
				num[j] += 1
				f=True
			cnt += 1
	ans = (ans * cnt) % mod
print(ans)