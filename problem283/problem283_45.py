a = int(input())

a-=1
cnt = 0
for i in range(1,a):
	if i < a:
		a -= 1
		cnt += 1
	else :
		break

print (cnt)