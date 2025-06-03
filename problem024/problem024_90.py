def is_ok(W, truck, middle):
    loaded = 0
    for t in range(truck):
        this_total = 0
        while this_total + W[loaded] <= middle:
            this_total += W[loaded]
            loaded += 1
            if loaded == len(W):
                return True
    return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(w, k, mid):
            ok = mid
        else:
            ng = mid
    return ok

n, k = map(int,input().split())

w = [0]*n
for i in range(n):
    w[i] = int(input())

ans = meguru_bisect(-1,10**10+1)
print(ans)
