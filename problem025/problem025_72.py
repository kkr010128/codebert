from sys import stdin

n = int(input())
A = list(map(int, stdin.readline().split()))
q = int(input())
m = list(map(int, stdin.readline().split()))

def solve(i,m):
    '''
    i番目以降の要素を使用してmを作れる場合、trueを返す
    '''
    if m == 0:
        return True
    if sum(A[i:]) < m:
        return False
    if i >= n:
        return False
    res = solve(i+1,m) or solve(i+1,m-A[i])
    return res

for a in m:
    if solve(0,a):
        print("yes")
    else:
        print("no")

