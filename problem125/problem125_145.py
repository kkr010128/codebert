X = int(input())
ans = 0
W = 360
while(True):
    W -= X
    ans += 1
    if W == 0:
        break
    if W < 0:
        W += 360
print(ans)