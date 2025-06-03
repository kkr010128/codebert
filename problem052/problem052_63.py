n = int(input())
for i in range(3,n + 1):
    if(i % 3 == 0):
        print('',i,end = '')
    elif(i >= 10 and i % 10 == 3):
        print('',i,end = '')
    elif(i > 10):
        x = i
        while(x > 0):
            x = int(x / 10)
            if(x % 10 == 3):
                print('',i,end = '')
                break
print('')