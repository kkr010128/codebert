a, b = map(int, input().split())
res = 'No'
if 500*a >= b:
    res = 'Yes'
print(res)