h, n = map(int,input().split())
a = list(map(int,input().split()))
atack = sum(a)
can = h <= atack
print("Yes" if can else "No")