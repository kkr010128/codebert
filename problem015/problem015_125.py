#coding:utf-8
n = int(input())
numbers = list(map(int, input().split()))

def selectionSort(ary):
    count = 0
    for i in range(len(ary)):
        minj = i
        for j in range(i, len(ary)):
            if ary[minj] > ary[j]:
                minj = j
        if minj != i:
            ary[minj], ary[i] = ary[i], ary[minj]
            count += 1
    return (ary, count)

result = selectionSort(numbers)
print(*result[0])
print(result[1])