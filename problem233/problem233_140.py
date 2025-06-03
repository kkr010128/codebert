def abc152c_low_elements():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 1
    min_val = p[0]
    for i in range(1, n):
        if min_val > p[i]:
            cnt += 1
            min_val = min(min_val, p[i])
    print(cnt)
abc152c_low_elements()