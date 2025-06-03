x,y = map(int,input().split())
ans = 'No'
for crane in range(x + 1):
    turtle = x - crane
    if 2 * crane + 4 * turtle == y:
        ans = 'Yes'
print(ans)