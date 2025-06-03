def check(k, p, w_list):
    i_w = 0
    for i_k in range(k):
        sum_w = 0
        while True:
            if i_w >= len(w_list):
                return len(w_list)
            if sum_w + w_list[i_w] > p:
                break
            sum_w += w_list[i_w]
            i_w += 1
    return i_w

n, k = list(map(int, input().split()))
w_list = list()

for _ in range(n):
    w = int(input())
    w_list.append(w)

left = 0
right = 100000 * 10000
mid = None

while left < right:
    mid = (left + right) // 2
    v = check(k, mid, w_list)
    if v >= n:
        right = mid
    else:
        left = mid + 1

print(right)