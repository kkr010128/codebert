n = int(input())
a = list(map(int, input().split(' ')))
q = int(input())
M = list(map(int, input().split(' ')))
minA = min(a)
sumA = 0
for i in a:
    sumA += i


def solve(i, m):
    if m==0 :
        return True
    if i>=n:
        return False
    res = solve(i+1, m) or solve(i+1, m-a[i])
    return res

for j in M:
    if j < minA or j > sumA:
        print('no')
    else:
        if solve(0, j):
            print('yes')
        else:
            print('no')

