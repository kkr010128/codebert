#coding:utf-8

N = int(input())
taro = 0
hanako = 0
for i in range(N):
	strs = input().split()
	if strs[0] > strs[1]:
		taro += 3
	elif strs[0] < strs[1]:
		hanako += 3
	else:
		taro+=1
		hanako+=1

print(str(taro) + " " + str(hanako))