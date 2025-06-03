rooms = [0] * (4*3*10)
count = int(input())
for i in range(count):
    b, f, r, v = [int(x) for x in input().split()]
    rooms[30*(b-1) + 10*(f-1) + (r-1)] += v
  
for i, room in enumerate(rooms, start=1):
    print('', room, end='')
    if i%10 == 0:
        print()
    if i%30 == 0 and i%120 != 0:
        print('#'*20)