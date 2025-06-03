n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]


def binarysearch(start, end):
    left = start
    right = end
    mid = 0

    while left < right:
        mid = (left + right)//2
        # print(mid)
        if simulate(mid, w, k):
            right = mid
            # print("ok")
        else:
            mid += 1
            left = mid
    return mid


def simulate(prb, wei, dai):
    cnt = 1
    tmp = 0
    for j in wei:
        tmp += j
        if tmp > prb:
            tmp = j
            cnt += 1
            if cnt > dai:
                return False
    return True

print(binarysearch(max(w), sum(w)))