N = int(input())

if N%2==1:
    print(0)
else:
    counter = 0
    tmp = 1
    while True:
        tmp *= 5
        
        if tmp>N:
            print(counter)
            break
        counter += N//(tmp*2)