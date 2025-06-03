x,y = list(map(int, input().split()))

ans=0
prize=[0, 300000, 200000, 100000, 0]
if x ==1 and y == 1:
    print(1000000)
else:
    print(prize[min(x,4)] + prize[min(y,4)])