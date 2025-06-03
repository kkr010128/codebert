def f(d, D):
    i = 0
    while i < 6:
        if d == D[i]:
            return i
        else:
            i += 1

Q0 = [1,2,4,3,1]
Q1 = [0,3,5,2,0]
Q2 = [0,1,5,4,0]
ans = ''
D = list(map(int, input().split(' ')))
n = int(input())
i = 0
while i < n:
    d0, d1 = map(int, input().split(' '))
    L0 = f(d0, D)
    L1 = f(d1, D)
    if L0 == 0:
        q = 0
        while q < 4:
            if L1 == Q0[q]:
                ans += str(D[Q0[q + 1]]) + '\n'
                break
            q += 1
    elif L0 == 1:
        q = 0
        while q < 4:
            if L1 == Q1[q]:
                ans += str(D[Q1[q + 1]]) + '\n'
                break
            q += 1
    elif L0 == 2:
        q = 0
        while q < 4:
            if L1 == Q2[q]:
                ans += str(D[Q2[q + 1]]) + '\n'
                break
            q += 1
    elif L0 == 3:
        q = 0
        while q < 4:
            if L1 == Q2[4-q]:
                ans += str(D[Q2[4-q-1]]) + '\n'
                break
            q += 1
    elif L0 == 4:
        q = 0
        while q < 4:
            if L1 == Q1[4-q]:
                ans += str(D[Q1[4-q-1]]) + '\n'
                break
            q += 1
    elif L0 == 5:
        q = 0
        while q < 4:
            if L1 == Q0[4-q]:
                ans += str(D[Q0[4-q-1]]) + '\n'
                break
            q += 1
    i += 1
if ans != '':
    print(ans[:-1])
