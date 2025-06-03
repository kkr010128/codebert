N = int(input())
S = sorted([input() for x in range(N)])
word = [S[0]]+[""]*(N-1)    #単語のリスト
kaisuu = [0]*N              #単語の出た回数のリスト
k = 0                       #今wordリストのどこを使っているか

for p in range(N):  #wordとkaisuuのリスト作成

    if word[k] != S[p]:
        k += 1
        word[k] = S[p]
        kaisuu[k] += 1
    
    else:
        kaisuu[k] += 1

m = max(kaisuu)     #m:出た回数が最大のもの
ansnum = []         #出た回数が最大のもののwordリストでの位置
for q in range(N):      
    if kaisuu[q] == m:
        ansnum += [q]

for r in range(len(ansnum)):
    print(word[ansnum[r]])