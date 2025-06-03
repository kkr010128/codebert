X = int(input())
cnt = 1
deg = X
while deg%360!=0:
    deg += X 
    cnt += 1
print(cnt)
