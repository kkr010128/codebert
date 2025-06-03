n = int(input())
c = input()
left, right = 0, n - 1
cnt = 0
while left <= right:
    while left < n and c[left] == 'R':
        left += 1
    while right > -1 and c[right] == 'W':
        right -= 1
    if left == n or right == -1 or left >= right: break
    left += 1
    right -= 1
    cnt += 1
print(cnt)