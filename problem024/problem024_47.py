import time
n, k = map(int, input().split())
w = [0] * n
for i in range(n):
    w[i] = int(input())


def check(p):
    remain_track = k - 1
    remain_p = p
    for a in range(n):
        if w[a] > p:
            return False
        if remain_p >= w[a]:
            remain_p -= w[a]
        else:
            if remain_track == 0:
                return False
            else:
                remain_track -= 1
                remain_p = p - w[a]
        # print(a, w[a], remain_p, remain_track)
    return True


next = 10 ** 9
prev = next


for i in range(200):
    if check(next):
        prev = next
        next = next // 2
    else:
        next = (next + prev) // 2
print(prev)
