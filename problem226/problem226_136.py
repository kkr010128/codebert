a,b = map(int,input().split())
lis = list(map(int,input().split()))
c = sum(lis)
print("No" if a > c else "Yes")