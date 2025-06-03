N = int(input())
c = list(input())

ans = 0
left = 0
right = N-1
while left < right:
    if c[left] != c[right]:
        if c[left] == 'W' and c[right] == 'R':
            ans += 1
        left += 1
        right -=1
        
    if c[left] == 'R' and c[right] == 'R':
        left += 1
    if c[left] == 'W' and c[right] == 'W':
        right -=1
        
print(ans)