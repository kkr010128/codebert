import sys
input = sys.stdin.readline

# C - Subarray Sum
n, k, s = map(int, input().split())
ans = ''
str_s = str(s)

if s < pow(10, 9):
	str_another = str(s + 1)
else:
	str_another = '1'

for i in range(n):
	if i < k:
		ans += str_s + ' '
	else:
		ans += str_another + ' '

print(ans[:len(ans)-1])