x, y = map(int, input().split())
if(x < y):
    for i in range(0, y):
        print(x, end = '')
else:
    for i in range(0, x):
        print(y, end = '')




