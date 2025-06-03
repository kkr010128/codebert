while True:
    line = list(map(int,input().split()))
    if line==[0,0]: break
    for i in range(line[0]):
        if i==0 or i==line[0]-1: print('#'*line[1])
        else: print('#'+'.'*(line[1]-2)+'#')
    print()