def p_is_smaller(p):
    total = 0
    number_of_track = 1
    for w in W:
        total += w
        if total > p:
            number_of_track += 1
            if number_of_track > k:
                return 1
            total = w
    return 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    W = [int(input()) for _ in range(n)]
    left, right = max(W), sum(W)
    while right > left:
        mid = (left + right) // 2
        if p_is_smaller(mid):
            left = mid + 1
        else:
            right = mid
    print(right)
