def eighty_one(a):
    for n in range(9, 0, -1):
        if a % n == 0:
            if a // n > 9:
                return False
            else:
                return True
    return False

n = int(input())
if eighty_one(n):
    print('Yes')
else:
    print('No')