def nanbanme(n, x):
    lst = [1 for i in range(n)]
    ans = 0
    for i in range(n):
        a = x[i]
        count = 0
        for j in range(a - 1):
            if (lst[j] == 1):
                count = count + 1
        tmp = 1
        for k in range(1, n - i):
            tmp = tmp*k
        ans = ans + count*tmp
        lst[a - 1] = 0
    return (ans + 1)

n = int(input())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

a = nanbanme(n, lst1)
b = nanbanme(n, lst2)

print(abs(a - b))
