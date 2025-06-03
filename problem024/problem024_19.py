n, k = map(int,input().split())
w_in = list()

for i in range(n):
    w_in.append(int(input()))


def alloc(p):
    load = 0
    track = 1
    for w in w_in:
        if w > p:
            return False
        if load + w <= p:
           load += w
        else:
            load = w
            track += 1
            if track > k:
                return False
    return True


def binsearch():
    upper = sum(w_in)
    lower = max(w_in)
    while(upper != lower):
        mid = int((upper + lower) / 2)
        if alloc(mid):
            upper = mid
        else:
            lower = mid + 1
    return upper
print(binsearch())