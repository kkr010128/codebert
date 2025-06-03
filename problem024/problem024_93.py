N, K = map(int, input().split())
w = [int(input()) for _ in range(N)]

def f(P):
    tmp_capacity = P
    num_used_truck = 1
    i = 0
    while i <= N-1:
        if w[i] > P:
            return i
        if w[i] > tmp_capacity:
            tmp_capacity = P
            num_used_truck += 1
            if num_used_truck >= K+1:
                return i

        tmp_capacity -= w[i]
        i += 1
    
    return i

left = 0
right = 1e9
mid = right
flag = 0
while right - left > 1:
    mid = (left + right)//2
    tmp = f(mid)
    if tmp >= N:
        right = mid
    elif tmp < N:
        left = mid
print(int(right))
