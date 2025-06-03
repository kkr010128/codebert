n, k = map(int, input().split())
T = [int(input()) for i in range(n)]

def update(P):

    i=0
    for j in range(k):
        s=0
        while s + T[i] <= P:
            s += T[i]
            i += 1
            if(i == n):
                return n

    return i

left = 0
right = 1e+9

while right - left > 1:
    mid = int((left+right)/2)

    v = update(mid)
    if(v >= n):
        right = mid
    else:
            left = mid

print(right)
