
bil_date = []
flag = 0
for i in range(4):
    bil_date.append([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
all_date_amo = int(input())
for i in range(all_date_amo):
    date = [int(indate) for indate in input().split()]
    bil_date[date[0]-1][date[1]-1][date[2]-1] = bil_date[date[0]-1][date[1]-1][date[2]-1] + date[3]
    if bil_date[date[0]-1][date[1]-1][date[2]-1] < 0:
        bil_date[date[0]-1][date[1]-1][date[2]-1] = 0
    if bil_date[date[0]-1][date[1]-1][date[2]-1] > 9:
        bil_date[date[0]-1][date[1]-1][date[2]-1] = 9
        
for bil in bil_date:
    for flo in bil:
        for room in flo:
            print(' {}'.format(room),end='')
        print('')
    if flag == 3:
        pass
    else:
        for i in range(20):
            print('#',end='')
        print('')
    flag = flag + 1

