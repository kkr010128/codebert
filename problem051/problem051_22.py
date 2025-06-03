import sys

for i in sys.stdin:
    h,w = map(int,i.strip().split())

    if h==0 and w==0:
        break

    for i in range(h):
        for j in range(w):
            if (i+j) % 2 == 0:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()