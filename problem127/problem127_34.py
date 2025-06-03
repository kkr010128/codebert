x,y=map(int,input().split())
print(('No','Yes')[2*x<=y<=4*x and -~y%2])