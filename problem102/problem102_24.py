n, k = map(int, input().split())

li_a = list(map(int, input().split()))

for idx, v in enumerate(li_a):
    if idx <= (k - 1):
        pass
    else:
        if v > li_a[idx - k]:
            print('Yes')
        else:
            print('No')
