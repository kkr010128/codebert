X,Y=map(int,input().split())

def ans170(X:int, Y:int):
    if Y<=X*4 and Y>=X*2 and Y%2==0:
        return("Yes")
    else:
        return("No")

print(ans170(X,Y))