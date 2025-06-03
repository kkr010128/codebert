n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
def f():
    if m == 0:
        if n == 1:
            return 0
        elif n == 2:
            return 10
        elif n == 3:
            return 100
    else:
        for i in range(1000):
            x = str(i)
            if len(x) == n:
                cnt = 0
                for j in range(m):
                    if x[sc[j][0] - 1] == str(sc[j][1]):
                        cnt += 1
                        if cnt == m:
                            return x
                    elif x[sc[j][0] - 1] != str(sc[j][1]):
                        break
    return -1
print(f())