n = int(input())
dic = set()
for i in range(n):
    x = input()
    if 'insert' in x:
        dic.add(x.strip('insert '))
    else :
        if x.strip('find ') in dic:
            print('yes')
        else :
            print('no')

