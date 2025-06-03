n = int(input())
li = list(map(int, input().split()))
cnt = 0

flag = True

while flag:
	flag = False
	for i in range(n-1,0,-1):
		if li[i] < li[i-1]:
			li[i], li[i-1] = li[i-1], li[i]
			flag = True
			cnt +=1

print(*li)
print(cnt)