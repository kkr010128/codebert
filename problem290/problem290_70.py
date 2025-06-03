n, k = map(int, input().split())
a_list = [int(i) for i in input().split()]
f_list = [int(i) for i in input().split()]
a_list.sort(reverse=True)
f_list.sort()

if k >= sum(a_list):
    print(0)
    exit()

point = []
for i in range(n):
    point.append(a_list[i] * f_list[i])

import math
def binary_search(point, k):
    left = 0
    right = 10 ** 12
    while left + 1< right:
        ans = 0
        center = (left + right) // 2
        for i in range(n):
            if point[i] > center:
                ans += a_list[i] - (center // f_list[i])
        if ans <= k:
            right = center
        else:
            left = center
    return left
    
value = binary_search(point, k)
print(value + 1)
