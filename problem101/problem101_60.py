import sys

a_b_c = list(map(int, input().split()))
r = a_b_c[0]
g = a_b_c[1]
b = a_b_c[2]
k = int(input())

while (g <= r and k >= 0):
    g *= 2
    k -= 1
while (b <= g and k >= 0):
    b *= 2
    k -= 1
if (k < 0):
    print("No")
else:
    print("Yes")