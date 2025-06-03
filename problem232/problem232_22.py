a, b = map(str, input().split())
ans = [a] * int(b) if int(a)<=int(b) else [b] * int(a)
print(''.join(ans))