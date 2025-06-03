n = int(input())
y = 1

while y <= n :
    if(y % 3 == 0):
        print(' %d'%y,end='')
    else:
        p = y
        while(p != 0):
            if(p % 10 == 3):
                print(' %d'%y,end='')
                break
            p //= 10
    y+=1
print()

