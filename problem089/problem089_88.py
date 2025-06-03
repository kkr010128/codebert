h,w,m = map(int,input().split())
bombX = [0]*h
bombY = [0]*w
bomb = set()
maxX = maxY = 0
for i in range(m):
    i,j = map(lambda x:int(x)-1, input().split())
    bomb.add((i,j))
    bombX[i] += 1
    bombY[j] += 1
    maxX = max(maxX,bombX[i])
    maxY = max(maxY,bombY[j])
maxX_index = list(i for i in range(h) if bombX[i] == maxX)
maxY_index = list(i for i in range(w) if bombY[i] == maxY)
for i in maxX_index:
    for j in maxY_index:
        if (i,j) in bomb: continue
        print(maxX+maxY)
        exit()
print(maxX+maxY-1)
