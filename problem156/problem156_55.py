x = int(input())

min_x = -int(pow(x,0.2))-1
for a in range(x):
    for b in range(min_x,x):
        test = pow(a,5) - pow(b,5)
        if b > 0 and test < x:
            break
        if test == x:
            print(a,b)
            exit()