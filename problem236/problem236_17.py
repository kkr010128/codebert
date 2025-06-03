h = int(input())
w = int(input())
n = int(input())

x = max(h, w)
cnt = 0
cur = 0

while cur < n:
	cur += x
	cnt+=1

print(cnt)