a = int(input())
b = int(input())

l = {1, 2, 3}
m = {a, b}
ans = list(l ^ m)

print(ans[0])