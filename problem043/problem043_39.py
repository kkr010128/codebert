import sys

while 1:
    x = sys.stdin.readline().strip()
    x_list = list(map(int,x.split(" ")))
    
    if x_list[0] == 0 and x_list[1] == 0 :
        break
    
    x_list.sort()
    print(x_list[0],x_list[1])