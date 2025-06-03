while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    print('#'*W)
    for _ in range(H-2):
        print('#'+'.'*(W-2)+'#')
    print('#'*W, end='\n\n')

