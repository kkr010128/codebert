a, b, c = map(int, input().split())
ans = 'Yes' if (c - a - b)**2 > 4*(a*b) and c - a - b > 0 else 'No'
print(ans)