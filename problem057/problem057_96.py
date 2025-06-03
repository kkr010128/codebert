from sys import stdin
for line in stdin:
    mid, final, make = map(int, line.split())
    if mid == -1 and final == -1 and make == -1:
        break
    elif mid == -1 or final == -1:
        print('F')
    elif mid + final >= 80:
        print('A')
    elif mid + final >= 65:
        print('B')
    elif mid + final >= 50:
        print('C')
    elif mid + final >= 30:
        if make >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')
