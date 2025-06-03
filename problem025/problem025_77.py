# coding: utf-8
# Your code here!

n = int(input())
A = [int(e) for e in input().split()]
q = int(input())
M = [int(e) for e in input().split()]

def solve(i,m):
    if m == 0:
        return True
    if i >= n:
        return False
    if m > sum(A[i:]):
        return False
    res = solve(i + 1,m) or solve(i + 1,m - A[i])
    return res
    
for m in M:
    if(solve(0,m)):
        print("yes")
    else:
        print("no")
