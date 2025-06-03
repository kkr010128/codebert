n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

max = 2000

def solve(x,y):
    if x==n:
        S[y] = 1
    else:
        solve(x+1,y)
        if y+A[x] < max+1:
            solve(x+1,y+A[x])
            
S = [0 for i in range(max+1)]

solve(0,0)
    
for i in range(m):
    if S[B[i]] == 1:
        print("yes")
    else:
        print("no")

