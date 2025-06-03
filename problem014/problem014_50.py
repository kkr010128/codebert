# -*- coding: utf-8 -*-

def bubbleSort(num_list):
    flag = True
    length = len(num_list)
    count = 0
    while flag:
        flag = False
        for j in range(length-1, 0, -1):
            if num_list[j] < num_list[j-1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
                flag = True
                count += 1
    return num_list, count


input_num = int(input())
num_list = [int(i) for i in input().split()]

bubble_list, swap_num = bubbleSort(num_list)
for i in range(len(num_list)):
    if i > 0:
        print(" ", end="")
    print(num_list[i], end="")
print()
print(swap_num)