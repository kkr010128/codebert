data = [
        [[0 for k in range(10)] for j in range(3)] for i in range(4)
        ]

count = int(input())

for x in range(count):
   (b,f,r,v) = [int(i) for i in input().split()]
   data[b - 1][f - 1][r - 1] += v

for b in range(4):
    for f in range(3):
        print(' ',end='')
        for r in range(10):
            if r == 9:
                print(data[b][f][r], end='')
            else:
                print(data[b][f][r], '', end='')
        print()

    if b == 3:
        break
    for x in range(20):
        print('#',end='')
    print()