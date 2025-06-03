Flag = True
data = []
while Flag:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        Flag = False
    else:
      data.append((H, W))
#print(type(W))
for (H, W) in data:
    for i in range(H):
        if i == 0 or i == H-1:
            print('#' * W)
        else:
            print('#' + '.' * (W-2) + '#')
    print('\n', end="")
