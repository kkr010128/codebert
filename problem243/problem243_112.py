N = int(input())
List = [list(map(str, input().split())) for i in range(0,N)]
X = str(input())

yoroshiosu = 0
samu = 0

for i in range (0, N):
	if X == List[i][0]:
		yoroshiosu =1
	elif yoroshiosu == 0:
		continue
	else:
		samu+=int(List[i][1])
        
print(samu)
