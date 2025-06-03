X,Y=map(int,input().split())
if X==Y==1: print(10**6)
else: print((max(0,4-X)+max(0,4-Y))*10**5)