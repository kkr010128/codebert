import sys
num = []
for i in sys.stdin:
    H, W = i.split()
    if H == W == '0':
        break
    num.append((int(H), int(W)))

for cnt in range(len(num)):
    for h in range(num[cnt][0]):
        for w in range(num[cnt][1]):
            if w == 0 or w == num[cnt][1] - 1 or h == 0 or h == num[cnt][0] - 1:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()