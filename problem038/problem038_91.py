a, b = map(int, input().split())
for ret in ['a < b', 'a > b', 'a == b']:
    if eval(ret):
        print(ret)