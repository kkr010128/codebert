H, A = map(int, input().split())

ans = (H // A) + ( 1 if (H % A) != 0 else 0)
print(ans)