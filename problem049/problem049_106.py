a = []
while True:
    l = list(map(int,input().split()))
    if l == [0,0]:
        break
    a.append(l)


for i in range(len(a)):
	H,W = a[i]
	for i in range(H):
		print("#"*W)
	print("")