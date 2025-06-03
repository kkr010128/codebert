x = list(map(int,input().split()))
ans = 0
for y in x:
    if y == 1:
        ans+=3
    elif y == 2:
        ans+=2
    elif y == 3:
        ans+=1
if sum(x)==2:
    ans += 4
print(ans * 100000)