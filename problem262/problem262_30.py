N = int(input())
 
testimony = [[] for _ in range(N)]
 
for i in range(N):
    num = int(input())
    for j in range(num):
        person, state = map(int, input().split())
        testimony[i].append([person-1, state])
        
honest = 0
for i in range(2**N):
    flag = 0
    for j in range(N):
        if (i>>j)&1 == 1: # j番目は正直と仮定
            for x,y in testimony[j]:
                if (i>>x)&1 != y: # j番目は正直だが矛盾を発見
                    flag = 1
                    break
    if flag == 0:  # 矛盾がある場合はflag == 1になる
        honest = max(honest, bin(i)[2:].count('1'))  # 1の数をカウントし最大となるものを選択
print(honest)