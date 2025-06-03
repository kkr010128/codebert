
D = int(input())
# with open("sample1.in") as f:

last = [0 for i in range(26)]
s = [[0 for j in range(26)] for i in range(D)]
c = list(map(int, input().split(" ")))
result = []
total = 0
# opened = []  #開催したやつを保存
for i in range(D):
    a = list(map(int, input().split(" ")))
    for j, k in enumerate(a):
        #print(i, j, k)
        s[i][j] = int(k)
        # スコア計算
    score_max = 0
    score_index = 0
    for j in range(26):

        if j == 0:
            score_max = s[i][j]  # - (i - last[j]) * c[j]
            for k in range(26):
                if j != k:
                    score_max -= (i + 1 - last[k]) * c[k]
            score_index = 0
        else:
            score = s[i][j]
            for k in range(26):
                if j != k:
                    score -= (i + 1 - last[k]) * c[k]

            if score_max < score:
                score_max = score
                score_index = j
            #print(i, j, score)
    result.append(score_index)
    #print(score_index, score)
    last[score_index] = i + 1
    total += score
    # print(a.index(max(a)))
# print(total)
for i in range(D):
    # print(s.index(max(s[i])))
    print(result[i]+1)
