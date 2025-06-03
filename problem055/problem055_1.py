floor = [[[0] * 10 for x in range(3)] for y in range(4)]

for c in range(int(input())):
    (b,f,r,v) = [int(x) for x in input().split()]

    floor[b-1][f-1][r-1] += v

for x in range(3 * 4):
    if x % 3 == 0 and not x == 0:
        print('#' * 20)
    print('',' '.join(str(y) for y in floor[int(x / 3)][x % 3]))