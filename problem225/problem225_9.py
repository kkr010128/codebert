h,a = map(int, input().split())
an, bn = divmod(h,a)
if bn == 0:
    print(an)
else:
    print(an+1)