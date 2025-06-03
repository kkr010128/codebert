#coding:utf-8
#1_4_A
def isFound(array, x):
    """ linear search """
    array.append(x)
    i = 0
    while array[i] != x:
        i += 1
    if i == len(array)-1:
        return False
    return True

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
count = 0

for i in range(q):
    if isFound(S, T[i]):
        count += 1

print(count)