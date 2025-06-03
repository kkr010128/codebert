H,N=map(int,input().split())
deathblows=map(int,input().split())
if sum(deathblows) >= H:
    print('Yes')
else:
    print('No')