N = int(input())
L = list(map(int, input().split()))

L = sorted(L)

import bisect

count = 0
for i in range (0, len(L)-2):
	for j in range (i+1, len(L)-1):
		count+= bisect.bisect_left(L[j+1:], L[i]+L[j])

print(count)