while True:
    a, b = map(int,raw_input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print str(b) +" "+ str(a)
    else:
        print str(a) +" "+ str(b)