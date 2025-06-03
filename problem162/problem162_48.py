import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

n, m = map(int, input().split())
if n % 2 == 0:
    n -= 1
ans = []
left_range = n//2
right_range = n//2 - 1
left1 = 1
right1 = 1 + left_range
left2 = right1 + 1
right2 = left2 + right_range

while True:
    if left1 >= right1:
        break
    ans.append([left1, right1])
    left1 += 1
    right1 -= 1

while True:
    if left2 >= right2:
        break
    ans.append([left2, right2])
    left2 += 1
    right2 -= 1
    
for i in range(m):
    print(*ans[i])    


