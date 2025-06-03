a, b, c = map(int, input().split())
piyo = (c - a - b) ** 2 
hoge = 4 * a * b
print("Yes" if hoge < piyo and c-a-b > 0 else "No")