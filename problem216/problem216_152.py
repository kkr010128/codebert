a,b,c=sorted(list(map(int, input().split())))
print("Yes" if (a==b and b!=c) or (a!=b and b==c) else "No")