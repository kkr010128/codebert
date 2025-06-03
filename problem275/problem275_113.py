XY=list(map(int,input().split()))
prize=0
for xy in XY:
    if xy==1:
        prize+=300000
    elif xy==2:
        prize+=200000
    elif xy==3:
        prize+=100000
if sum(XY)==2:
    prize+=400000
print(prize)