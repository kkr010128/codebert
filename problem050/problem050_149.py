while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    for i in range(w):
        if i==0 or i == w-1: print('#'*h)
        else: print('#'+'.'*(h-2)+'#')
    print()

