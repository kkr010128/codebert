while 1:
    a = list(map(int, input().split()))
    if a[0] or a[1]:
        print(min(a), max(a))
    else:
        break
