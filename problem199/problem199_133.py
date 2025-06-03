li = list(input())
n = len(li)
for i in range(0, n, 2):
    if li[i] == 'h' and li[i + 1] == 'i' and n % 2 == 0:
        pass
    else:
        print('No')
        exit()
print('Yes')
