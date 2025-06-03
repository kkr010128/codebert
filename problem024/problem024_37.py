N, K = map(int, input().split())
W = []

for i in range(N):
    W.append(int(input()))

def f(N, K, W, p):
    cnt = 0
    k = 1
    c_k = 0
    for w in W:
        if c_k + w <= p:
            c_k = c_k + w
            cnt = cnt + 1
        elif k < K and w <= p:
            k = k + 1
            c_k = w
            cnt = cnt + 1
        elif k < K and w > p:
            pass
        else:
            break
    return cnt

start = 0
end = 1000000000
while start != end:
    center = (start + end)//2
    if f(N, K, W, center) < N:
        start = center + 1
    else:
        end = center

print(start)
