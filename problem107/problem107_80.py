import sys
sys.setrecursionlimit(1000000)

N = int(input())
X = input()
pc = X.count('1')


if pc == 0:
    print(*[1]*N, sep='\n')
    exit()
elif pc == 1:
    if int(X, 2) == 1:
        for i in range(N-1):
            print(2)
        print(0)
        exit()
    else:
        for i in range(N):
            if i == N-1:
                print(2)
            elif X[i] == '0':
                print(1)
            else:
                print(0)
        exit()

mod_plus_1, mod_minus_1 = 0, 0
for i in range(N):
    mod_plus_1 = (mod_plus_1*2+int(X[i])) % (pc+1)
    mod_minus_1 = (mod_minus_1*2+int(X[i])) % (pc-1)


def f(x):
    if x == 0:
        return 0
    else:
        return f(x % bin(x).count('1'))+1


mods_p1, mods_m1 = [1 % (pc+1)], [1 % (pc-1)]
for i in range(N-1):
    mods_p1.append(mods_p1[-1]*2 % (pc+1))
    mods_m1.append(mods_m1[-1]*2 % (pc-1))
mods_p1 = mods_p1[::-1]
mods_m1 = mods_m1[::-1]


for i in range(N):
    if X[i] == '0':
        x = mod_plus_1 + mods_p1[i]
        x %= (pc+1)
    else:
        x = mod_minus_1 - mods_m1[i]
        x %= (pc-1)

    if x == 0:
        print(1)
    else:
        print(f(x)+1)
