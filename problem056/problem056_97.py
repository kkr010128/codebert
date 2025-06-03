# coding:utf-8
array = map(int, raw_input().split())
n = array[0]
m = array[1]
a = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
answer = [0 for i in range(n)]
for i in range(n):
    a[i] = map(int, raw_input().split())
for j in range(m):
    b[j] = input()
for i in range(n):
    for j in range(m):
        answer[i] += a[i][j] * b[j]
for i in range(n):
    print answer[i]

