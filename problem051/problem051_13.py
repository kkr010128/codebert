while True:
    a,b = map(int,input().split())
    if(a==0 and b==0):
        break;
    for i in range(a):
        for j in range(b):
            type='#'
            if(i%2 == 0):
                if(j%2 == 0):
                   print('#',end='')
                else:
                    print('.',end='')
            elif(i%2 == 1):
                if(j%2 == 0):
                   print('.',end='')
                else:
                    print('#',end='')
        print()
    print()

