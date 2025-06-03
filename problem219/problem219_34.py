def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

N = s_in()[::-1]
n = len(N)

dp1 = [0 for _ in range(n)]
dp1[0] = int(N[0])
# dp1[i] は i桁目を同じ値だけ使ったとしたときの最小値
dp2 = [0 for _ in range(n)]
dp2[0] = 10 - int(N[0])
# dp2[i] は i桁目を繰り上げたとしたときの最小値

for i, s in enumerate(N[1:]):
    i += 1

    m = int(s)
    dp1[i] = min(dp1[i-1] + m,      dp2[i-1] + (m+1))
    dp2[i] = min(dp1[i-1] + (10-m), dp2[i-1] + (10-m-1))

# print(dp1)
# print( dp2)
print(min(dp1[n-1], dp2[n-1]+1))
