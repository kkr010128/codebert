K = int(input())
numbers = set([])
q = set(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(f'{q=}')

while len(numbers) <= 100000:  # 10**8:
    # print('test')
    qq = set([])
    for i in q:
        # print(f'{i=}')
        if len(i) == 1:
            if i == '0':
                n = i + '0'
                qq.add(n)
                n = i + '1'
                qq.add(n)
            elif i == '9':
                n = i + '9'
                qq.add(n)
                n = i + '8'
                qq.add(n)
            else:
                v = int(i)
                n = i + str(v - 1)
                qq.add(n)
                n = i + str(v)
                qq.add(n)
                n = i + str(v + 1)
                qq.add(n)
        else:
            if i[-1] == '0':
                n = i + '0'
                qq.add(n)
                n = i + '1'
                qq.add(n)
            elif i[-1] == '9':
                n = i + '9'
                qq.add(n)
                n = i + '8'
                qq.add(n)
            else:
                v = int(i[-1])
                n = i + str(v - 1)
                qq.add(n)
                n = i + str(v)
                qq.add(n)
                n = i + str(v + 1)
                qq.add(n)
    # print(f'{qq=}')
    numbers |= q
    # print(f'{numbers=}')
    # print(f'{len(numbers)=}')
    q = qq

numbers = sorted(map(int, numbers))
# print(f'{numbers[:30]=}')
ans = numbers[K - 1]
print(ans)
