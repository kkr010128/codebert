X,Y=map(int,input().split());m=4-min(X,Y)
if X==Y==1:print(10**6)
elif X<=3and Y<=3:print(((4-X)+(4-Y))*10**5)
else:print(m*10**5if m>=0else 0)