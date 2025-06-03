a, b = map(int, input().split())
ans = a - b*2
print(ans if ans > 0 else 0)