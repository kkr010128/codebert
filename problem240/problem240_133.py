N, M = [int(x) for x in input().split()]

P = [0] * (N + 1)           #各問題のペナルティの回数を記録
ok = [False] * (N + 1)      #その問題でACが出たかどうか記録

correct = 0                 #正答数を記録
penalty = 0                 #ペナルティ数を記録
for i in range(M):
    query = input().split()
    p = int(query[0])
    S = query[1]
    if ok[p] == False:
        if S == 'AC':
            ok[p] = True
            correct += 1
            penalty += P[p]
        else: # S = 'WA'
            P[p] += 1

print(correct, end=' ')
print(penalty)