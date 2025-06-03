xy = [map(int,input().split()) for i in range(2)]
x,y = [list(j) for j in zip(*xy)]
if (y[0] + 1) == y[1] :
    ans = 0
else:
    ans = 1
print(ans)