x, y = map(int,input().split())
leg = 2*x
if y==leg:
    print('Yes')
    exit()
for i in range(1,x+1):
    leg += 2
    if y==leg:
        print('Yes')
        exit()
print('No')