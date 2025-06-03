n = int(input())
li1 = list(map(int,input().split()))
m = int(input())
li2 = list(map(int,input().split()))
cnt = 0

for i in li2:
	if i in li1:
		cnt +=1
print(cnt)