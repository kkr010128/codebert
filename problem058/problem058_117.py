def get_num(n, x):
    ans = 0
    for n3 in xrange(min(n, x - 3), (x + 2) / 3, -1):
        for n2 in xrange(min(n3 - 1, x - n3 - 1), (x - n3) / 2, -1):
            if n3 + min(n2 - 1, x - n3 - n2):
                ans += 1
    return ans


data = []
while True:
    [n, x] = [int(m) for m in raw_input().split()]
    if [n, x] == [0, 0]:
        break
    # if x < 3:
    #     print(0)
    # else:
    print(get_num(n, x))