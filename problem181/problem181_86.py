K = int(input())
numbers = set([])
q = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(f'{q=}')

while len(numbers) <= 100000:  # 10**8:
    # print('test')
    qq = set([])
    for i in q:
        # print(f'{i=}')
        if i % 10 != 0:
            n = i * 10 + (i % 10) - 1
            qq.add(n)
        if i % 10 != 9:
            n = i * 10 + (i % 10) + 1
            qq.add(n)
        n = i * 10 + (i % 10)
        qq.add(n)
    numbers |= q
    # print(f'{numbers=}')
    # print(f'{len(numbers)=}')
    q = qq

numbers = sorted(map(int, numbers))
# print(f'{numbers[:30]=}')
ans = numbers[K - 1]
print(ans)
