def abc154d_dice_in_line():
    n, k = map(int, input().split())
    p = list(map(lambda x: (int(x)+1)*(int(x)/2)/int(x), input().split()))
    ans = sum(p[0:k])
    val = ans
    for i in range(k, len(p)):
        val = val - p[i-k] + p[i]
        ans = max(ans, val)
    print(ans)
abc154d_dice_in_line()