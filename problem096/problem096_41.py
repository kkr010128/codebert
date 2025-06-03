[N,D],*li = [list(map(int,i.split())) for i in open(0)]

D = D**2
ans = 0
for x,y in li:
    if x**2 + y**2 <= D:ans += 1
print(ans)