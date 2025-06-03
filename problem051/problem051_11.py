list = []

while True:
    H, W = [int(i) for i in input().split()]
    if H == 0 and W == 0:
        break
    list.append([H, W])

for i in range(len(list)):
    for j in range(list[i][0]):
        for k in range(list[i][1]):
            if j % 2 == 1:
                print('#',end='') if k % 2 == 1 else print('.',end='')
            else:
                print ('#',end='') if k % 2 == 0 else print('.',end='')
        print()
    print()