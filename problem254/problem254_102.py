a=int(input())
b=int(input())

ans = set()
ans.add(a)
ans.add(b)
all = {1,2,3}
print((all-ans).pop())