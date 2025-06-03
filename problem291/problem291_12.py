A,B = (int(a) for a in input().split())
ans = A - B * 2
print(max(0,ans))