def call2(n):
    for i in range(1,n+1):
        x = i
        if i%3 == 0:
            print(' {}'.format(i), end='')
        else:
            while x:
                if x%10 ==3:
                    print(' {}'.format(i), end='')
                    break
                x = x//10
    print()

call2(int(input()))