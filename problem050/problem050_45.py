y,x = [int(x) for x in input().split()]
while(x > 0 or y > 0):
    print('#' * x)
    st  = '#' 
    st += '.' * (x-2)
    st += '#'
    for i in range(1, y-1):
        print(st)
        
    print('#' * x)
    print()
    y,x = [int(x) for x in input().split()]