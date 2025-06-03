n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

def solve2(x,y):
    if x==n:
        S[y] = 1
    else:
        solve2(x+1,y)
        if y+A[x] < 2001:
            solve2(x+1,y+A[x])
            
S = [0 for i in range(2001)]

solve2(0,0)

def solve(x,y):
    if y<0:
        return False
    elif y==0:
        return True
    elif x==n:
        return False
    else:
        return solve(x+1,y) or solve(x+1,y-A[x])
    
for i in range(m):
    if (i>50 and (S[B[i]] == 1)):
        print("yes")
    elif (i>50 and (S[B[i]] == 0)):
        print("no")
    else:
        if solve(0,B[i]):
            print("yes")
        else:
            print("no")
