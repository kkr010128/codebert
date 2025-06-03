N = int(input())

dic = {}
for i in range(N):
    com, s = input().split()
    if com == 'insert':
        dic[s] = True
    elif com == 'find':
        print('yes' if s in dic else 'no')
