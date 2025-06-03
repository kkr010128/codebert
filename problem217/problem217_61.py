n = int(input())
list01 = input().split()
x = 0
for i in list01:
    if int(i) % 2 != 0:
        pass
    elif int(i) % 3 == 0:
        pass
    elif int(i) % 5 == 0:
        pass
    else:
        x += 1
        break

if x == 1:
    print('DENIED')
else:
    print('APPROVED')