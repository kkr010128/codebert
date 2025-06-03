N = int(input().rstrip())
flag = False
for i in range(1,10):
    for j in range(1,10):
        if N == i * j:
            flag = True
            break
    else:
        continue
    break
print('Yes' if flag else 'No')