for i in range(int(raw_input())):
    a, b, c = [int(j) ** 2 for j in raw_input().split()]
    if a+b==c or a+c==b or b+c==a:
        print 'YES'
    else:
        print 'NO'