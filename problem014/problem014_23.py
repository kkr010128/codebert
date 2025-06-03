#coding:utf-8
#1_2_A
def bubble_sort(ary, n):
    count = 0
    flag = 1
    i = 0
    while flag:
        flag = 0
        for j in reversed(range(i+1, n)):
            if ary[j] < ary[j-1]:
                ary[j], ary[j-1] = ary[j-1], ary[j]
                count += 1
                flag = 1
        i += 1

    print(' '.join(map(str, ary)))
    print(count)

n = int(input())
numbers = list(map(int, input().split()))
bubble_sort(numbers, n)