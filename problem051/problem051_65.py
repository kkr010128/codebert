import sys

for i in sys.stdin.readlines()[:-1]:
    h,w = map(int,i.strip().split())
    for i in range(h):
        for j in range(w):
            print('#' if (i+j) % 2 == 0 else '.',end='')
        print()
    print()