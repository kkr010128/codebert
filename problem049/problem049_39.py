Flag = True
data = []
while Flag:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        Flag = False
    else:
      data.append((H, W))
#print(data)

for (H, W) in data:
    for i in range(H):
        print('#' * W)
    print('\n', end="")
