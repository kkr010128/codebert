first_place, K, Distance = map(int, input().split())
first_place = abs(first_place)
test = first_place
if first_place - Distance*K > 0:
    print(first_place -Distance*K)
else:
    for i in range(1,K+1):
        test -= Distance
        if test <= 0:
            a = i
            #print(a)
            break
    if (K-a)%2 == 0 or K-a == 0:
        print(abs(first_place - Distance*a))
    else:
        print(abs(first_place - Distance*(a-1)))
