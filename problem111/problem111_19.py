#coding:utf-8
N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse = True)

k = N-2
index = 1
ans = A[0]

while k > 0:
    if k > 1:
        k -= 2
        ans += A[index] * 2
    elif k == 1:
        k -= 1
        ans += A[index]
    index += 1

print("{}".format(ans))