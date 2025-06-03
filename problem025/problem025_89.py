n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
memory = [[-1 for i in range(max(m)+1)]for j in range(n)]

def f(i, m):
    if m == 0:
        return 1
    elif i >= n:
        return 0
    elif memory[i][m] != -1:
        return memory[i][m]
    elif m - a[i] >= 0:
        res0 = f(i+1, m)
        res1 = f(i+1, m-a[i])
        if res0 or res1:
            memory[i][m] = 1
            return 1
        else:
            memory[i][m] = 0
            return 0
    else:
        res = f(i+1, m)
        memory[i][m] = res
        return res

for k in m:
    print('yes' if f(0, k) else 'no')

