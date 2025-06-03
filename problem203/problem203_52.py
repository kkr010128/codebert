a, b = map(int, input().split())
for price in range(0,1010) :
    if int(price*0.08) == a and int(price*0.10) == b :
        print(price)
        break
else :
    print("-1")
