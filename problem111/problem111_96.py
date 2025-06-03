import math
n = int(input())
lst = list(map(int, input().split()))
sortlst = sorted(lst, reverse = True)
#print(sortlst)
ans = 0
for i in range(n - 1):
	point =sortlst[math.ceil(i / 2)]
#	print(point)
	ans += point

print(ans)	
