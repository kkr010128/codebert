# -*- coding: utf-8 -*-

def selection_sort(a, n):
    count = 0
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
        if a[i] != a[minj]:
            count += 1
    return a, count

def main():
    input_num = int(input())
    input_list = [int(i) for i in input().split()]

    ans_list, count = selection_sort(input_list, input_num)
    for i in range(input_num):
        if i != 0:
            print(" ", end="")
        print(ans_list[i], end='')
    print()
    print(count)

if __name__ == '__main__':
    main()