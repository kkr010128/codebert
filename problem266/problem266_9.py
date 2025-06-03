x = int(input())

if x%100 == 0 or x%101 == 0 or x%102 == 0 or x%103 == 0 or x%104 == 0 or x%105 == 0:
    print (1)
else:
    for i in range(100000):
        if 100*i <= x <= 105*i:
            print (1)
            exit ()
    else:
        print (0)
