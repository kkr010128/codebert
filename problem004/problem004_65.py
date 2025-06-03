for i in range(int(input())):
    temp = [int(x) for x in input().split()]
    stemp = sorted(temp)
    if stemp[2]**2 == stemp[1]**2 + stemp[0]**2:
        print('YES')
    else:
        print('NO')

