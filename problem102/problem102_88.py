a,b = map(int,(input().split()))
c = list(map(int,input().split()))
for i in range(a-b):
    print("Yes" if c[i] < c[i+b] else "No")