def func(n):
    x = []
    for i in range(1,n+1):
        num = i
        if i % 3 == 0:
            x.append(i)
        else:
            while num:
                if int(num % 10) == 3:
                    x.append(i)
                    break
                num = int(num / 10)
    return x

if __name__ == '__main__':
    N = int(input())
    rlt = func(N)
    print(" ", end='')
    for i in range(len(rlt)):
        if rlt[i] == rlt[-1]:
            print(rlt[i], end='')
        else:
            print(rlt[i], end=' ')
print()