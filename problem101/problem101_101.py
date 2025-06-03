"""
b > g > r

"""

r, g, b = list(map(int, input().split()))
k = int(input())
flag = False
for i in range(k):
    if r >= b and b > 2 * g :
        g *= 2
    elif r >= g and b > 2 * g:
        g *= 2
    else:
        b *= 2

if r < g < b:
    flag = True
print("Yes") if flag else print("No")