import sys

while True:
    data = sys.stdin.readline().strip().split(' ')
    h = int(data[0])
    w = int(data[1])
    if h == 0 and w == 0:
        break
    
    for i in range(h):
        for j in range(w):
            print('#', end='')
        print('')
        
    print('')