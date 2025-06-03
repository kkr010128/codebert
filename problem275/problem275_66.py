x, y = map(int, input().split())
ans = 4 if x == 1 and y == 1 else 0
ans += max(0, 4-x)+max(0, 4-y)
print(ans*100000)
