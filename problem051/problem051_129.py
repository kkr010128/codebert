while True:
    h,w = map(int,input().split())
    if h == w == 0:
        break
    for y in range(h):
        for x in range(w):
            if (y+x)%2 == 0:
                print('#',end="")
            if (y+x)%2 == 1:
                print('.',end="")
        print()
    print()