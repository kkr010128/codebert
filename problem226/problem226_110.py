h,n = map(int, input().split())
a = [int(i) for i in input().split()]
print("No" if sum(a)<h else "Yes")