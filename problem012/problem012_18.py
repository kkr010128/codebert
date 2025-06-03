x = int(input())

count = 0
for i in range(0, x):
    a =  int(input())
    for j in range ( 2,  a ):
        c = int(a)
        if a % j == 0:
            count += 1
            break;
        if j * j  > c:
            break;
        
print(x-count)
        

