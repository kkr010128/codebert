while True:
    s = input().split()
    h = int(s[0])
    w = int(s[1])
    if h == 0 and w == 0:
        break
    
    for i in range(h):
        print("#"*w)
        
    print()
