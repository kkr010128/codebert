n = int(input())
dic = {}

for i in range(n):
    line = input().split()
    if line[0] == 'insert':
        if dic.get(line[1]):
            dic[line[1]] += 1
        else:
            dic[line[1]] = 1
    elif line[0] == 'find':
        if dic.get(line[1]):
            print('yes')
        else:
            print('no')