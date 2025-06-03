k, x = map(int, input().split())

ans = 'Yes'
if 500 * k < x:
    ans = 'No'

print(ans)