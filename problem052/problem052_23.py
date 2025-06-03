def Check_Num(n):

    for i in range(1,n + 1):
        x = i
        if (x % 3 == 0):
            print(' {}'.format(i),end = '')
            continue
        elif (x % 10 == 3):
            print(' {}'.format(i),end = '')
            continue
        x //= 10
        while (x > 0):
            if (x % 10 == 3):
                print(' {}'.format(i),end = '')
                break
            x //= 10
    print()
if __name__ == '__main__':
    n = int(input())
    Check_Num(n)
