#coding:utf-8
#1_5_B
def merge_sort(array):
    if len(array) > 1:
        L, countL = merge_sort(array[0:len(array)//2])
        R, countR = merge_sort(array[len(array)//2:])
        return merge(L, R, countL+countR)

    if len(array) == 1:
        return [array, 0]

def merge(L, R, count=0):
    L.append(10**9+1)
    R.append(10**9+1)
    response = []
    i = 0
    j = 0
    for k in range(len(L)-1 + len(R)-1):
        if L[i] <= R[j]:
            response.append(L[i])
            i += 1
            count += 1
        else:
            response.append(R[j])
            j += 1
            count += 1
    return [response, count]

n = int(input())
S = list(map(int, input().split()))
numbers, count = merge_sort(S)
print(*numbers)
print(count)