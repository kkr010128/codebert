n = int(input())
c = list(input())
r = 0
w = 0
for i in range(len(c)):
    if(c[i]=="R"):
        r += 1
ans = max(r,w)
for i in range(len(c)):
    if(c[i]=="R"):
        r -= 1
    else:
        w += 1
    now = max(r,w)
    ans = min(ans,now)
print(ans)    