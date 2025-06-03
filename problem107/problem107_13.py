def pc(x):
    return format(x, 'b').count('1')


N = int(input())
X = input()
Xo = int(X, 2)

count = 0
ans = 0
ori = pc(Xo)
X = list(X)

Xp = Xo%(ori + 1)
if ori == 1:
    Xm = 0
else:
    Xm = Xo % (ori - 1)

# for i in range(N-1, -1, -1):
for i in range(N):
    if ori == 1 and X[i] == '1':
        print(0)
        continue
    else:
        if X[i] == '1':
            # ans = Xm - pow(2, i, ori - 1)
            ans = Xm - pow(2, N-1-i, ori - 1)
            ans %= ori - 1
        else:
            # ans = Xp - pow(2, i, ori + 1)
            ans = Xp + pow(2, N-1-i, ori + 1)
            ans %= ori + 1
    count = 1
    while ans > 0:
        # count += 1
        # if ans == 1:
        #     break
        ans %= pc(ans)
        count += 1

   
    print(count)
    count = 1
