def resolve():
    N = input()
    heights = [int(x) for x in input().split(" ")]

    max_heights = 0
    s = 0

    for h in heights:
        if h < max_heights:
            s += max_heights - h
        else:
            max_heights = h
    print(s)
    
resolve()