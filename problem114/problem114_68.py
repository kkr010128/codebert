#!/usr/bin/env python3

D = int(input())
c = list(map(int, input().split()))

s = []
for d in range(D):
    s.append(list(map(int, input().split())))

def get_objective_function(output):
    objective_function = 0
    last = [[-1 for i in range(26)] for d in range(D)]

    for d in range(D):
        objective_function += s[d][output[d]]

        last[d][output[d]] = d
        if d < D-1:
            for i in range(26):
                last[d+1][i] = max(last[d][i], last[d+1][i])

        for i in range(26):
            objective_function -= c[i] * (d-last[d][i])
        print(objective_function)

    point = max(10 ** 6 + objective_function, 0)

## outputの作成
# IOに基づくパターン
output = []
for _ in range(D):
    output.append(int(input())-1)

# 最大効用での戦略
#output = []
#for d in range(D):
#    output.append(s[d].index(max(s[d])))
#for d in output:
#    print(d+1)

## 目的関数の確認
get_objective_function(output)