def judge(n,a):
    table = {}
    for i in range(n):
        if a[i] in table.keys():
            print('NO')
            return
        else:
            table[a[i]] = 1
    print('YES')
    return
    
n = int(input())
a = list(map(int,input().split()))

judge(n,a)