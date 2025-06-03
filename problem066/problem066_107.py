while True:
    x = input()
    if x == '-' :
        break
    m = int(input())
    
    for i in range(m):
        h = int(input())
        y = x[0:h]
        z = x[h:len(x)+1]
        x = list(z+y)
    x = ''.join(x)
    print(x)
