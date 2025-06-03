n=int(input())
A=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))

def solve(x,y):
    global n
    global A
    if y==0:
        return True
    if x>=n:
        return False
    if sum(A[x:])<y:
        return False
    return solve(x+1,y) or solve(x+1,y-A[x])
for i in m:
    if solve(0,i):
        print("yes")
    else:
        print("no")
