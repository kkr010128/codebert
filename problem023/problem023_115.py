n = int(input())
dic = set()
for i in range(n):
    order, Str = input().split()
    if order=='insert':
        dic.add(Str)
    if order=='find':
        if Str in dic:
            print('yes')
        else:
            print('no')
