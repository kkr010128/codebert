n = int(input())

dic = {}
for i in range(n):
    inst, c = input().split()
    if inst[0] == 'i':
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 0
    else:
        if c in dic:
            print('yes')
        else:
            print('no')