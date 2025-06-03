x,y = map(int,input().split())
k = [0,3,2,1] + [0]*1000
ans = k[x]+k[y]
if x == y == 1:
    ans += 4
print(ans*100000)