while True:
    y,x = [int(i) for i in input().split()]
    if y==x==0:
        break
    print('#'*x)
    for i in range(y-2):
        print('#'+'.'*(x-2)+'#')
    if y > 1:
        print('#'*x)
    print()