from sys import exit

x, n = map(int, input().split())
p = list(map(int, input().split()))
for d in range(x+1): #0に達した時点で0を出力して終了するので、大きい側は気にしなくてよい
    for s in [-1, 1]:
        a = x + d*s
        if p.count(a) == 0:
            print(a)
            exit()