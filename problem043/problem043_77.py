while 1:
    x, y = map(int, raw_input().split())
    if x == 0 and y == 0:
        break
    print min(x, y), 
    print max(x, y)