x = int(input())
cnt = x//100
if x < 100 :
    print("0")
else :
    for i in range(cnt) :
        if 100*cnt <= x <= 105*cnt :
            print("1")
            break
    else :
        print("0")
