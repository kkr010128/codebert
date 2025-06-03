a=["#." * (300//2),".#" * (300//2)]*(300//2)
while True:
    [h,w] = map(int, input().split())
    if h==0 and w==0:
        break
    t = map(lambda x: x[0:w], (a[0:h]))
    for i in t:
        print(i)
    print()