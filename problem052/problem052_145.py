n = int(input())
for i in range(1,n+1):
    x = i
    if x%3 == 0:
        print(' ',i,sep='',end='')
    else:
        while x != 0:
            if(x % 10 == 3):
                print(' ',i,sep='',end='')
                break
            else:
                x //= 10
print()