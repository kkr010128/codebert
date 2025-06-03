n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))
sumA = sum(A)
def solve(i,m):
    if m == 0:
        return 1
    if i >= n:
        return 0
    rec =  solve(i+1,m) or solve(i+1, m - A[i])
    return rec
for i in m:
    if i >= sumA:
        print("no")
    else:
        if solve(0,i):
            print("yes")
        else:
            print("no")
