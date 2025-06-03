import sys

for v in iter(sys.stdin.readline,''):
    h,w = map(int,v.split())

    if h == 0 and w == 0:
        break

    print('#'*w)

    for i in range(h-2):
        print('#'+('.'*(w-2))+'#')

    print('#'*w)
    print('')