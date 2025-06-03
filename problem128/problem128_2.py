x, n = map(int, input().split())
if n == 0:
    print(x)
else:
    a = [int(x) for x in input().split()]
    ans1 = x
    while ans1 in a :
        ans1 -= 1
    ans2 = x
    while ans2 in a :
        ans2 += 1
    if abs(x - ans1) <= abs(x - ans2):
        print(ans1)
    else:
        print(ans2)


    

