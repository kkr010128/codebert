n, k = map(int, input().split())
A = list(map(int, input().split()))

bottom, top = 0, max(A)

def cut(x):
    cnt = 0
    for Length in A:
        if Length % x == 0:
            cnt += Length // x
        else:
            cnt += Length // x + 1
        cnt -= 1
    return cnt <= k

while top - bottom > 1:
    middle = (top + bottom) // 2
    if cut(middle):
        top = middle
    else:
        bottom = middle
    
print(top)