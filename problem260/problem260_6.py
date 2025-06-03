a1, a2, a3 = map(int, input().split())
ans = 'bust' if a1 + a2 + a3 >= 22 else 'win'
print(ans)