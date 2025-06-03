n,k = map(int,input().split())
w = [int(input()) for i in range(n)]
def f(x):
    i = 0
    for j in range(k):
        s = 0
        while s+w[i] <= x:
            s += w[i]
            i+=1
            if i == n:
                return n
    return i

def bin_search(left,right):
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) == n:
            right = mid
        else:
            left = mid
    return right

print(bin_search(0,10**9))
