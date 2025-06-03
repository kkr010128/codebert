from sys import stdin

for line in stdin:
    H, W = map(int, line.rstrip().split(' '))
    if 0 == H == W:
        break

    print('#'*W)

    for i in range(H-2):
        print('#'+'.'*(W-2)+'#')

    print('#'*W)
    print()