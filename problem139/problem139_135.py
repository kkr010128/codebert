a, b, c, d, K = map(int, input().split())

hour = (c-a) * 60
min = d - b
ans = hour + min - K
print(ans) 
