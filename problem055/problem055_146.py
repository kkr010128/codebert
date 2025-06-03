room = [0 for i in range(120)]
c = int(input())
for i in range(c):
    b, f, r, v = [int(s) for s in input().split()]
    index = (30 * (b - 1)) + (10 * (f - 1)) + (r - 1)
    room[index] += v

for i in range(12):
    if (i != 0) and (i % 3 == 0):
        print('#' * 20)
    print(' ' + ' '.join([str(v) for v in room[i*10:i*10+10]]))