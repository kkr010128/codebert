# coding: utf-8
import sys

def func(num_list):
    count = 0
    for i in range(2):
        while(True):
            # print(num_list[i], num_list[i+1])
            if num_list[i] < num_list[i+1]:
                break
            else:
                num_list[i+1] = num_list[i+1] * 2 
                count = count + 1
    return count


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    
    tmp = lines[0].split(' ')
    num_list = []
    for n in tmp:
        num_list.append(int(n))

    count = func(num_list)
    if count <= int(lines[1]):
        print("Yes")
    else:
        print("No")
