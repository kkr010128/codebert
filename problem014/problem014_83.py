# -*- coding:utf-8 -*-

def bubble_sort(num_list):
    swap_count = 0
    for i in range(len(num_list)):
        for j in range(len(num_list)-1, i , -1):
            if num_list[j] < num_list[j-1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
                swap_count = swap_count + 1
    return num_list, swap_count

def show_list(list):
    i = 0;
    while(i < len(list)-1):
        print(list[i], end=" ")
        i = i + 1
    print(list[i])

num = int(input())
num_list = [int(x) for i, x in enumerate(input().split()) if i < num]
num_list, swap_count = bubble_sort(num_list)
show_list(num_list)
print(swap_count)