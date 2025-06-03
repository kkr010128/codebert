a = int(input())
b = int(input())
ans = list(filter(lambda x: x != a and x != b, [1, 2, 3]))
print(ans[0])