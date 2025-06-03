N,K = map(int, raw_input().split())
W = [int(raw_input()) for _ in range(N)]

if N == 1:
    print W[0]
    exit()

def check(p):
    k = 1
    wt = 0
    for w in W:
        #print wt,
        if wt + w <= mid:
            wt += w
        else:
            if w <= mid:
                wt = w
                k += 1
            else:
                #print "error"
                return False
    #print k
    return k <= K

left = min(W)
right = sum(W)
mid = 0
while left < right:
    #print left, right
    mid = int((left + right) / 2)
    #print mid,
    if check(mid):
        right = mid
    else:
        left = mid + 1

print left

