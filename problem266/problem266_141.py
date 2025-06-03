x = int(input())

if x//100 > 19:
    print(1)
else:
    tmp1 = x%100
    tmp2 = x//100
    if 5*tmp2<tmp1:
        print(0)
    else:
        print(1)
