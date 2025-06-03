x = int(input())
flag = False
for i in range(x, 1000000):
    for j in range(2, i+1):
        #print(i, j)
        if j == i:
            print(i)
            flag = True
            break
        if i % j == 0:
            #print('*', i, j)
            break
    if flag:
        break