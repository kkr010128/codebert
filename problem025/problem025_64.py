n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(input().split())
for i in range(m):
    B[i] = int(B[i])

def solve(x,y):
    if x==n:
        S[y] = 1
    else:
        solve(x+1,y)
        if y+A[x] < 2001:
            solve(x+1,y+A[x])
            
S = [0 for i in range(2001)]

solve(0,0)
    
for i in range(m):
    if S[B[i]] == 1:
        print("yes")
    else:
        print("no")

