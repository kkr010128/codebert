N = int(input())
A = []
for i in range(N):
    a  = int(input())
    Alst = []
    for j in range(a):
        x,y = map(int,input().split())
        Alst.append([x-1,y])
    A.append(Alst)

honest = 0
  
for i in range(2**N):
    flag = 0
    for j in range(N):
        if (i>>j)&1:
            for x,y in A[j]:
                if (i>>x)&1 != y: # j番目は正直だが矛盾を発見
                    flag = 1
                    break
    if flag == 0:  # 矛盾がある場合はflag == 1になる
        honest = max(honest, bin(i)[2:].count('1'))  # 1の数をカウントし最大となるものを選択
print(honest)